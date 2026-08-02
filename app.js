// ENLEARN PWA - app.js - V7.6 (FINAL: Range = 1 Session, auto start/end, keep classic UI)
// 目标：保留你喜欢的旧版版面/风格，同时支持：范围统计、曲线、分段统计与导出
// V7.6 PATCH: 全局开关 - 看答案开关, 发音开关
// 规则：看答案立即生效 - 发音延时触发 - 连点短于 0.5 秒自动取消发音

const $ = (id) => document.getElementById(id);

const LS_KEY = "enlearn_pwa_v7_6";
const CACHE_NAME = "enlearn-tts-cache-v1";

// 自动行为参数
const AUTO_SHOW_DOM_DELAY_MS = 80;     // 只为等渲染稳定
const AUTO_SPEAK_DELAY_MS = 300;       // 题目出现后 0.3s 再尝试发音
const AUTO_SPEAK_CANCEL_MS = 500;      // 连点阈值 0.5s - 小于这个就不发音
const AUTO_SPEAK_MIN_STAY_MS = 200;    // 题目停留不足 0.2s - 不发音

let state = JSON.parse(localStorage.getItem(LS_KEY)) || {
  deckId: "",
  mode: "ordered",
  asked: 0,                 // 累计完成题数（按“切到下一题/上一题”计）
  effectiveSec: 0,          // 累计有效用时（上限 30s/题）
  stats: {},                // 可扩展（目前不强依赖）
  currentId: null,
  showingAnswer: false,

  // 全局开关
  autoShowAnswer: false,    // 开 - 每题自动显示答案
  autoSpeak: false,         // 开 - 每题自动发音

  // 随机
  shuffledDeck: [],

  // Session 训练统计：范围即一次训练
  sessions: [],             // [{ts, deckId, deckName, mode, rangeStart, rangeEnd, questions, sec, avg}]
  sessionActive: false,
  sessionStartAsked: 0,
  sessionStartSec: 0,
  sessionStartTs: 0,
  lastSessionMsg: ""
};

let t0 = null, DECKS = [], audioEl = null, myChart = null;

// 自动发音的取消与节奏控制
let qToken = 0;
let lastNavTs = 0;
let questionShownAt = 0;
let pendingSpeakTimer = null;

function saveState() { localStorage.setItem(LS_KEY, JSON.stringify(state)); }

function clearPendingSpeak() {
  if (pendingSpeakTimer) {
    clearTimeout(pendingSpeakTimer);
    pendingSpeakTimer = null;
  }
}

// ---------- 范围过滤 ----------
function getRange() {
  const rawStart = ($("rangeStart")?.value ?? "").trim();
  const rawEnd = ($("rangeEnd")?.value ?? "").trim();
  const s = rawStart === "" ? 1 : Math.max(1, parseInt(rawStart, 10) || 1);
  const e = rawEnd === "" ? 999999 : Math.max(s, parseInt(rawEnd, 10) || 999999);
  return { s, e, rawStart: rawStart || "1", rawEnd: rawEnd || "Max" };
}

function getFilteredItems() {
  const deck = DECKS.find(d => d.id === state.deckId);
  if (!deck) return [];
  const { s, e } = getRange();

  return deck.items.filter(it => {
    // 兼容 id 含字母：取数字部分
    const idNum = parseInt(String(it.id).replace(/\D/g, ""), 10) || 0;
    return idNum >= s && idNum <= e;
  });
}

// ---------- 抽题 ----------
function createShuffledDeck(items) {
  const indices = items.map((_, i) => i);
  for (let i = indices.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [indices[i], indices[j]] = [indices[j], indices[i]];
  }
  return indices;
}

function getCurrentIndex(items) {
  if (!items.length) return 0;
  const idx = items.findIndex(x => String(x.id) === String(state.currentId));
  return idx >= 0 ? idx : 0;
}

function nextItem(step = 1) {
  const items = getFilteredItems();
  if (!items.length) return null;

  let pick = null;

  if (state.mode === "random") {
    if (!state.shuffledDeck || state.shuffledDeck.length === 0) {
      state.shuffledDeck = createShuffledDeck(items);
    }
    const idx = state.shuffledDeck.pop();
    pick = items[idx] || items[0];
  } else if (state.mode === "smart") {
    const scored = items.map(it => {
      const s = state.stats[String(it.id)] || { shown: 0, avgSec: 0 };
      return { it, score: (s.shown * 3) - s.avgSec };
    });
    scored.sort((a, b) => a.score - b.score);
    pick = scored[0].it;
  } else {
    // ordered：以当前题在过滤列表中的位置为基准移动
    const cur = getCurrentIndex(items);
    let next = cur;
    if (state.currentId == null) next = 0;
    else next = (cur + (step >= 0 ? 1 : -1) + items.length) % items.length;
    pick = items[next];
  }

  if (!pick) return null;
  state.currentId = pick.id;
  return pick;
}

// ---------- 统计：只在“切题”时统计，不把“看答案/发音”算作完成 ----------
function finalizePrevQuestionIfNeeded(countAsFinished) {
  if (t0 === null) return;

  const duration = (performance.now() - t0) / 1000;
  // 防抖：刚切题的瞬间不算
  if (duration < 0.3) {
    t0 = performance.now();
    return;
  }

  const capped = Math.min(duration, 30);
  state.effectiveSec += capped;

  if (countAsFinished) {
    state.asked += 1;
    // 可扩展：记录每题统计（目前不强依赖）
    const id = String(state.currentId);
    if (!state.stats[id]) state.stats[id] = { shown: 0, avgSec: 0 };
    state.stats[id].shown += 1;
    state.stats[id].avgSec = (state.stats[id].avgSec * 0.7) + (capped * 0.3);
  }

  t0 = performance.now();
  saveState();
}

// ---------- 全局开关行为 ----------
function updateToggleUIOnly() {
  if ($("btnShow")) $("btnShow").textContent = state.autoShowAnswer ? "隐藏答案" : "看答案";
  if ($("btnPron")) $("btnPron").textContent = state.autoSpeak ? "不发音" : "发音";
}

function scheduleAutoSpeakForCurrent(tokenAtSchedule) {
  clearPendingSpeak();

  if (!state.autoSpeak) return;

  pendingSpeakTimer = setTimeout(() => {
    // 题目已变
    if (tokenAtSchedule !== qToken) return;

    const now = performance.now();

    // 停留太短
    if ((now - questionShownAt) < AUTO_SPEAK_MIN_STAY_MS) return;

    // 连点太快 - 还没超过 0.5s 的静默期
    const sinceNav = now - lastNavTs;
    if (sinceNav < AUTO_SPEAK_CANCEL_MS) {
      const waitMore = (AUTO_SPEAK_CANCEL_MS - sinceNav) + 30;
      scheduleAutoSpeakForCurrent(tokenAtSchedule);
      // 重新安排时要把延时变成 waitMore
      clearPendingSpeak();
      pendingSpeakTimer = setTimeout(() => {
        if (tokenAtSchedule !== qToken) return;
        const now2 = performance.now();
        if ((now2 - questionShownAt) < AUTO_SPEAK_MIN_STAY_MS) return;
        if ((now2 - lastNavTs) < AUTO_SPEAK_CANCEL_MS) return;
        speakCurrentSafe();
      }, waitMore);
      return;
    }

    speakCurrentSafe();
  }, AUTO_SPEAK_DELAY_MS);
}

function applyAutoBehaviors(it, tokenAtSchedule) {
  // 看答案 - 全局开立即生效
  state.showingAnswer = !!state.autoShowAnswer;
  updateUI(it);

  // 给 DOM 一点稳定时间
  if (state.autoShowAnswer) {
    setTimeout(() => {
      if (tokenAtSchedule !== qToken) return;
      const items = getFilteredItems();
      const cur = items.find(x => String(x.id) === String(state.currentId));
      if (cur) updateUI(cur);
    }, AUTO_SHOW_DOM_DELAY_MS);
  }

  // 发音 - 延时 + 连点取消
  scheduleAutoSpeakForCurrent(tokenAtSchedule);

  saveState();
}

function startQuestion(it, step = 1) {
  // step != 0 表示切题，才算完成上一题
  if (t0 !== null) finalizePrevQuestionIfNeeded(step !== 0);

  // 切题时间戳 - 用于连点取消
  if (step !== 0) lastNavTs = performance.now();

  // 新题 token
  qToken += 1;
  const tokenAtSchedule = qToken;
  questionShownAt = performance.now();

  // 默认把 per-question 答案显示交给全局开关
  state.showingAnswer = !!state.autoShowAnswer;

  if (it) {
    state.currentId = it.id;
    t0 = performance.now();
    updateUI(it);
    applyAutoBehaviors(it, tokenAtSchedule);
  } else {
    updateUI(null);
    clearPendingSpeak();
  }

  saveState();
}

// ---------- UI ----------
function updateUI(it) {
  const items = getFilteredItems();
  const total = items.length;

  let currentIdx = items.findIndex(x => String(x.id) === String(state.currentId)) + 1;
  if (currentIdx <= 0 && total > 0) currentIdx = 1;

  const m = Math.floor(state.effectiveSec / 60);
  const s = Math.floor(state.effectiveSec % 60);
  const avg = state.asked ? (state.effectiveSec / state.asked).toFixed(1) : "0.0";

  const { rawStart, rawEnd } = getRange();

  const sessionBadge = state.sessionActive ? " - 训练中" : "";
  const last = state.lastSessionMsg ? `<div style="opacity:.75; margin-top:6px;">${state.lastSessionMsg}</div>` : "";
  $("progressText").innerHTML =
  `范围 <span style="color:#fff; font-weight:400;">${rawStart}-${rawEnd}</span> - 进度 <span style="color:#fff; font-weight:400;">${currentIdx}/${total}</span>${sessionBadge}<br>` +
  `累计 <span style="color:#fff; font-weight:400;">${m}分${s}秒</span> - 完成 <span style="color:#fff; font-weight:400;">${state.asked}</span> 题 - 平均 <span style="color:#fff; font-weight:400;">${avg}s</span>/句` +
  last;

  const q = it ? [it.prompt_fr, it.prompt_zh || it.prompt_en || it.prompt].filter(Boolean).join("\n\n") : "超出范围 - 请调整范围";
  const a = it ? [it.answer_fr || it.answer || it.answer_en, it.answer_zh].filter(Boolean).join("\n\n") : "";

  $("qText").textContent = q || "—";
  $("aText").textContent = state.showingAnswer ? a : ". . .";

  // 两个按钮现在是全局开关
  updateToggleUIOnly();
}

// ---------- 发音 ----------
function speakCurrentSafe() {
  try {
    if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    if (audioEl) {
      audioEl.pause();
      audioEl.currentTime = 0;
    }
  } catch (e) {}
  pronounce();
}

function pronounceQuestion() {
  const items = getFilteredItems();
  const it = items.find(x => String(x.id) === String(state.currentId));
  if (!it?.prompt_audio_url) return;
  try {
    if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    if (audioEl) {
      audioEl.pause();
      audioEl.src = "";
    }
  } catch (e) {}
  audioEl = new Audio(it.prompt_audio_url);
  audioEl.preload = "auto";
  audioEl.onerror = () => console.error("老师问句音频加载失败", it.prompt_audio_url);
  audioEl.play().catch(error => console.error("老师问句音频播放失败", error));
}

async function pronounce() {
  const deck = DECKS.find(d => d.id === state.deckId);
  const items = getFilteredItems();
  const it = items.find(x => String(x.id) === String(state.currentId));
  if (!it) return;

  // 发音时 - 如果答案没显示 - 先显示
  if (!state.showingAnswer) {
    state.showingAnswer = true;
    updateUI(it);
    saveState();
  }

  // 读答案
  const raw = String(it.answer_fr || it.answer || it.answer_en || "");
  const text = raw.replace(/[^a-zA-Z0-9\u00C0-\u017F\s']/g, "").replace(/\s+/g, " ").trim();
  if (!text) return;

  if (it.audio_url) {
    if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    if (audioEl) {
      audioEl.pause();
      audioEl.src = "";
    }
    audioEl = new Audio(it.audio_url);
    audioEl.preload = "auto";
    audioEl.onerror = () => console.error("ElevenLabs 音频加载失败", it.audio_url);
    audioEl.play().catch(error => console.error("ElevenLabs 音频播放失败", error));
    return;
  }

  console.warn("这条题目没有 ElevenLabs 音频", it.id);
}

// ---------- 曲线（每次 Session 的平均耗时） ----------
function renderChart() {
  const canvas = $("historyChart");
  if (!canvas || typeof Chart === "undefined") return;

  const ctx = canvas.getContext("2d");
  if (myChart) myChart.destroy();

  const sess = state.sessions || [];
  const labels = sess.map((_, i) => String(i + 1));
  const avgs = sess.map(s => s.avg);
  const secs = sess.map(s => s.sec);

  myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels,
      datasets: [
        { label: "每次训练平均耗时 (s/题)", data: avgs, tension: 0.25 },
        { label: "每次训练总用时 (s)", data: secs, type: "bar", yAxisID: "y1" }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: { type: "linear", position: "left" },
        y1: { type: "linear", position: "right", grid: { display: false } }
      }
    }
  });
}

// ---------- Session 训练统计（范围即一次训练） ----------
function startSession() {
  const deck = DECKS.find(d => d.id === state.deckId);
  const { rawStart, rawEnd } = getRange();
  const total = getFilteredItems().length;

  state.sessionActive = true;
  state.sessionStartAsked = state.asked;
  state.sessionStartSec = state.effectiveSec;
  state.sessionStartTs = Date.now();
  state.lastSessionMsg = `训练开始 - ${deck?.name || state.deckId} - 范围 ${rawStart}-${rawEnd} - ${total}题`;
  saveState();
}

function endSessionIfNeeded() {
  if (!state.sessionActive) return;

  const deck = DECKS.find(d => d.id === state.deckId);
  const { rawStart, rawEnd } = getRange();
  const questions = getFilteredItems().length;

  const askedDelta = Math.max(0, state.asked - state.sessionStartAsked);
  const secDelta = Math.max(0, state.effectiveSec - state.sessionStartSec);
  const avg = askedDelta ? (secDelta / askedDelta) : 0;

  // 严格：必须完成整段题数才记录（防止误触）
  if (askedDelta < questions) return;

  state.sessions.push({
    ts: Date.now(),
    deckId: state.deckId,
    deckName: deck?.name || state.deckId,
    mode: state.mode,
    rangeStart: rawStart,
    rangeEnd: rawEnd,
    questions,
    sec: Number(secDelta.toFixed(1)),
    avg: Number(avg.toFixed(2))
  });

  if (state.sessions.length > 80) state.sessions.shift();

  state.sessionActive = false;
  state.lastSessionMsg = `训练完成 - ${questions}题 - 用时 ${secDelta.toFixed(1)}s - 平均 ${avg.toFixed(2)}s/题`;
  saveState();

  renderSessions();
  renderChart();
}

function renderSessions() {
  const box = $("sessionsList");
  if (!box) return;

  const sess = state.sessions || [];
  if (!sess.length) {
    box.innerHTML = `<div style="opacity:.7;">暂无记录</div>`;
    return;
  }

  box.innerHTML = sess
    .slice()
    .reverse()
    .map((seg, i) => {
      const dt = new Date(seg.ts);
      const mm = String(dt.getMinutes()).padStart(2, "0");
      const stamp = `${dt.getMonth() + 1}/${dt.getDate()} ${dt.getHours()}:${mm}`;
      return `
        <div style="border:1px solid rgba(255,255,255,.08); border-radius:12px; padding:10px 12px; margin:10px 0;">
          <div style="display:flex; justify-content:space-between; gap:10px; align-items:baseline;">
            <div style="font-weight:600; color:#fff;">第 ${sess.length - i} 次 - ${seg.deckName}</div>
            <div style="opacity:.7; font-size:.9em;">${stamp}</div>
          </div>
          <div style="opacity:.85; margin-top:6px; line-height:1.6;">
            模式 ${seg.mode} - 范围 ${seg.rangeStart}-${seg.rangeEnd}<br>
            题数 <b style="color:#fff;">${seg.questions}</b> - 用时 <b style="color:#fff;">${seg.sec}s</b> - 平均 <b style="color:#fff;">${seg.avg}s</b>/题
          </div>
        </div>
      `;
    })
    .join("");
}

function exportSessionsCSV() {
  const sess = state.sessions || [];
  if (!sess.length) { alert("暂无训练记录可导出"); return; }

  const header = ["timestamp","deckId","deckName","mode","rangeStart","rangeEnd","questions","sec","avg"];
  const lines = [header.join(",")];

  for (const seg of sess) {
    const row = [
      new Date(seg.ts).toISOString(),
      seg.deckId,
      seg.deckName.replace(/"/g,'""'),
      seg.mode,
      seg.rangeStart,
      seg.rangeEnd,
      seg.questions,
      seg.sec,
      seg.avg
    ].map(v => `"${String(v)}"`);
    lines.push(row.join(","));
  }

  const blob = new Blob([lines.join("\n")], { type: "text/csv;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "enlearn_sessions.csv";
  document.body.appendChild(a);
  a.click();
  a.remove();
}

// ---------- 事件 ----------
function bindEvents() {
  $("btnApplyRange").onclick = () => {
    const items = getFilteredItems();
    if (!items.length) {
      state.currentId = null;
      state.sessionActive = false;
      updateUI(null);
      saveState();
      return;
    }

    // 重新开始一次训练：从范围第一题开始
    state.currentId = items[0].id;
    t0 = performance.now();

    // 开启 Session
    startSession();

    // 进入第一题，按全局开关自动行为
    startQuestion(items[0], 0);

    renderSessions();
    renderChart();
    saveState();
  };

  $("deckSelect").onchange = (e) => {
    state.deckId = e.target.value;

    // 切题库会破坏可比性：清空本题库的训练记录，并停止当前训练
    state.asked = 0;
    state.effectiveSec = 0;
    state.stats = {};
    state.shuffledDeck = [];
    state.currentId = null;

    state.sessionActive = false;
    state.sessions = [];
    state.lastSessionMsg = "题库已切换 - 请设置范围并点「开始计时」开始训练";

    clearPendingSpeak();

    saveState();

    // 只刷新 UI，不自动开训（训练必须由“开始计时”启动）
    renderChart();
    renderSessions();

    const items = getFilteredItems();
    if (items.length) {
      state.currentId = items[0].id;
      t0 = null; // 直到“开始计时”才开始计时
      startQuestion(items[0], 0);
    } else {
      updateUI(null);
    }
    saveState();
  };

  $("modeSelect").onchange = (e) => {
    state.mode = e.target.value;
    state.shuffledDeck = [];
    // 模式变化会破坏可比性：结束当前训练，要求重新“开始计时”开始新一轮
    state.sessionActive = false;
    state.lastSessionMsg = "模式已切换 - 请点「开始计时」开始新一轮训练";
    clearPendingSpeak();
    saveState();

    const it = getFilteredItems().find(x => String(x.id) === String(state.currentId)) || getFilteredItems()[0];
    if (it) startQuestion(it, 0);
  };

  // 看答案按钮 - 现在是全局开关
  $("btnShow").onclick = () => {
    state.autoShowAnswer = !state.autoShowAnswer;

    const it = getFilteredItems().find(x => String(x.id) === String(state.currentId));
    if (it) {
      qToken += 1;
      const tokenAtSchedule = qToken;
      questionShownAt = performance.now();
      state.showingAnswer = !!state.autoShowAnswer;
      updateUI(it);
      applyAutoBehaviors(it, tokenAtSchedule);
    }

    saveState();
  };

  $("btnNext").onclick = () => {
    const items = getFilteredItems();
    if (!items.length) return;

    const curIdx = items.findIndex(x => String(x.id) === String(state.currentId));
    const isLast = (curIdx === items.length - 1);

    // 正常切题（会结算上一题并把其算作完成）
    startQuestion(nextItem(1), 1);

    // 如果刚刚完成的是最后一题：结束 Session，记录一次，并自动回到第一题开始下一轮
    if (isLast) {
      endSessionIfNeeded();

      // 自动进入下一轮同范围训练
      const first = getFilteredItems()[0];
      if (first) {
        state.currentId = first.id;
        t0 = performance.now();
        startSession();
        startQuestion(first, 0);
        saveState();
      }
    }
  };

  $("btnPrev").onclick = () => startQuestion(nextItem(-1), -1);

  // 发音按钮 - 现在是全局开关
  $("btnPron").onclick = () => {
    state.autoSpeak = !state.autoSpeak;
    updateToggleUIOnly();
    saveState();

    // 打开后 - 当前题也按规则尝试自动发音
    if (state.autoSpeak) {
      qToken += 1;
      const tokenAtSchedule = qToken;
      questionShownAt = performance.now();
      scheduleAutoSpeakForCurrent(tokenAtSchedule);
    } else {
      clearPendingSpeak();
    }
  };

  // 点击答案区域 - 永远当作手动播放一次
  $("aText").onclick = () => {
    clearPendingSpeak();
    speakCurrentSafe();
  };

  $("qText").onclick = pronounceQuestion;
  $("btnQuestionPron").onclick = pronounceQuestion;

  $("btnExportSessions").onclick = exportSessionsCSV;

  $("btnReset").onclick = () => {
    if (confirm("重置所有记录与缓存？")) {
      if (typeof caches !== "undefined") caches.delete(CACHE_NAME);
      localStorage.removeItem(LS_KEY);
      location.reload();
    }
  };
}

// ---------- CSV 解析 ----------
function parseCSV(text) {
  text = (text || "").replace(/^\uFEFF/, "");
  const rows = [];
  let cur = "", line = [], inQuotes = false;

  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (inQuotes) {
      if (ch === '"' && text[i + 1] === '"') { cur += '"'; i++; }
      else if (ch === '"') inQuotes = false;
      else cur += ch;
    } else {
      if (ch === '"') inQuotes = true;
      else if (ch === ",") { line.push(cur); cur = ""; }
      else if (ch === "\n") { line.push(cur); rows.push(line); cur = ""; line = []; }
      else if (ch !== "\r") cur += ch;
    }
  }
  line.push(cur);
  rows.push(line);

  const headers = (rows.shift() || []).map(h => h.trim().replace(/^\uFEFF/, ""));
  return rows
    .filter(r => r.some(c => String(c || "").trim()))
    .map(r => {
      const o = {};
      headers.forEach((h, i) => { o[h] = String(r[i] || "").trim(); });
      return o;
    });
}

function normalizeItem(obj, idx = 0) {
  const id = String(obj.id || obj.ID || (idx + 1)).trim();
  return {
    id,
    prompt_zh: String(obj.prompt_zh || obj.prompt_cn || obj.zh || obj.cn || "").trim(),
    prompt_en: String(obj.prompt_en || obj.en || "").trim(),
    prompt_fr: String(obj.prompt_fr || obj.question_fr || "").trim(),
    // 兼容 answer/answer_fr/fr
    answer_fr: String(obj.answer_fr || obj.fr || obj.answer || "").trim(),
    answer: String(obj.answer || "").trim(),
    answer_en: String(obj.answer_en || "").trim(),
    answer_zh: String(obj.answer_zh || obj.answer_cn || "").trim(),
    prompt: String(obj.prompt || "").trim(),
    audio_url: String(obj.audio_url || obj.audio || "").trim(),
    prompt_audio_url: String(obj.prompt_audio_url || obj.question_audio_url || "").trim()
  };
}

function judgeLang(deck) {
  if (/a1|fr|法语|conj|变位/i.test(deck.id) || /a1|法语|变位/i.test(deck.name)) return "fr";
  return "en";
}

// ---------- 启动 ----------
async function boot() {
  DECKS = [];

  const CSV_FILES = [
    { id: "tcf_oral_b2", name: "🔥 TCF Oral B2 CEO (176句)", file: "TCF_Oral_B2_CEO_176.csv" },
    { id: "tcf_oral_b2_dialogue", name: "🎤 TCF Oral B2 考官问答 (40组)", file: "TCF_Oral_B2_考官问答_40.csv" }
  ];

  for (const f of CSV_FILES) {
    const file = f.file_alt || f.file;
    if (!file || !String(file).toLowerCase().endsWith(".csv")) continue;

    try {
      const res = await fetch(file, { cache: "no-store" });
      if (res.ok) {
        const raw = parseCSV(await res.text());
        const items = raw.map((row, i) => normalizeItem(row, i))
          .filter(it => it.prompt_zh || it.prompt_en || it.prompt || it.answer_fr || it.answer);
        if (items.length) DECKS.push({ id: f.id, name: f.name, file, items });
      }
    } catch (e) { console.warn("Skip", file, e); }
  }

  if (!DECKS.length) {
    $("qText").textContent = "没有加载到题库 - 请检查 CSV 文件是否在同目录";
    $("aText").textContent = "";
    return;
  }

  DECKS.forEach(d => d.fixedLang = judgeLang(d));

  const ds = $("deckSelect");
  ds.innerHTML = "";
  DECKS.forEach(d => {
    const opt = document.createElement("option");
    opt.value = d.id;
    opt.textContent = `${d.name} [${d.items.length}]`;
    ds.appendChild(opt);
  });

  if (!state.deckId || !DECKS.some(d => d.id === state.deckId)) {
    state.deckId = DECKS[0].id;
  }
  ds.value = state.deckId;

  $("modeSelect").value = state.mode;

  bindEvents();
  renderChart();
  renderSessions();

  // 进入第一题：不算完成（训练需点“开始计时”启动）
  const first = getFilteredItems()[0];
  if (first) startQuestion(first, 0);
  else updateUI(null);
}

document.addEventListener("DOMContentLoaded", boot);
