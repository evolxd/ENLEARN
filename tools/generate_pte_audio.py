#!/usr/bin/env python3
"""
PTE Describe Image 配音生成器 — 用 Gemini TTS 为每道题的范文朗读生成清晰的英语音频，
直接覆盖写入 pte-describe-image/audio/itemNN.mp3。

用法：
  pip install requests lameenc
  export GEMINI_API_KEY="你的key"          # Windows: set GEMINI_API_KEY=你的key
  python tools/generate_pte_audio.py pte-describe-image/index.html

可选参数：
  --dry-run          只列出每题字数，不调用 API
  --model MODEL       默认 gemini-3.1-flash-tts-preview
  --voice VOICE       默认 Charon
  --only 3,7          只重新生成指定题号（其余用缓存跳过）
  --delay SECONDS     每次成功调用后的等待秒数，默认 3

输出：
  pte-describe-image/audio/itemNN.mp3   按题号覆盖写入
  tts_cache/                             按内容哈希缓存；中途失败重跑会自动跳过已完成的题目
"""
import argparse, base64, hashlib, html, os, re, sys, time
import requests, lameenc

API = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
RATE = 24000  # Gemini TTS 输出：24kHz / 16-bit / 单声道 PCM

STYLE = (
    "Clear, natural, moderately paced spoken English, as a fluent, confident PTE Speaking "
    "model-answer narrator. Standard neutral international English accent, natural stress "
    "and short pauses at commas and full stops, no dramatization or theatrical flair. "
    "This will be used by a language learner to study pronunciation and rhythm."
)

def build_prompt(text):
    return (
        "Synthesize speech for the transcript below. Read ONLY the transcript, never these notes.\n\n"
        "### DIRECTOR'S NOTES\n"
        f"Style: {STYLE}\n\n"
        "### TRANSCRIPT\n" + text
    )

def call_tts(key, model, voice, prompt, tries=6):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}},
        },
    }
    wait = 8
    for n in range(1, tries + 1):
        try:
            r = requests.post(API.format(model=model), json=body, timeout=300,
                              headers={"x-goog-api-key": key, "Content-Type": "application/json"})
        except requests.RequestException as e:
            print(f"    网络错误：{e}；{wait}s 后重试 ({n}/{tries})"); time.sleep(wait); wait = min(wait * 2, 120); continue
        if r.status_code == 200:
            try:
                parts = r.json()["candidates"][0]["content"]["parts"]
                data = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
                return base64.b64decode(data)
            except Exception:
                print(f"    返回里没有音频（可能被判为文本输出），重试 ({n}/{tries})")
        elif r.status_code in (429, 500, 502, 503, 504):
            ra = r.headers.get("retry-after")
            w = int(ra) if ra and ra.isdigit() else wait
            print(f"    HTTP {r.status_code}，{w}s 后重试 ({n}/{tries})"); time.sleep(w); wait = min(wait * 2, 120); continue
        else:
            sys.exit(f"API 错误 HTTP {r.status_code}：{r.text[:500]}")
        time.sleep(wait); wait = min(wait * 2, 120)
    sys.exit("多次重试仍失败，请稍后再跑（已完成的题目会保留在 tts_cache/ 和 audio/ 里）。")

def trim_silence(pcm, thresh=350, keep_ms=180):
    """去掉首尾过长的静音，保留一点呼吸感。"""
    import array
    s = array.array("h"); s.frombytes(pcm[: len(pcm) // 2 * 2])
    if sys.byteorder == "big": s.byteswap()
    i, j = 0, len(s) - 1
    while i < j and abs(s[i]) < thresh: i += 1
    while j > i and abs(s[j]) < thresh: j -= 1
    pad = RATE * keep_ms // 1000
    i, j = max(0, i - pad), min(len(s), j + pad)
    out = s[i:j]
    if sys.byteorder == "big": out.byteswap()
    return out.tobytes()

def to_mp3(pcm, kbps=96):
    enc = lameenc.Encoder()
    enc.set_bit_rate(kbps); enc.set_in_sample_rate(RATE); enc.set_channels(1); enc.set_quality(2)
    return enc.encode(pcm) + enc.flush()

def extract_items(html_text):
    """从 index.html 里按题号取出每题 .text 区块的纯文本（去标签，段落间保留换行）。"""
    items = []
    for m in re.finditer(r'<section class="card" id="item(\d+)">(.*?)</section>', html_text, re.S):
        num = int(m.group(1))
        block = m.group(2)
        tm = re.search(r'<div class="text">(.*?)</div>\s*<div class="meta">', block, re.S)
        if not tm:
            sys.exit(f"item{num}: 找不到 .text 区块")
        raw = tm.group(1)
        raw = raw.replace('<mark class="skel">', "").replace("</mark>", "")
        paras = re.findall(r"<p>(.*?)</p>", raw, re.S)
        paras = [re.sub(r"<[^>]+>", "", p).strip() for p in paras]
        paras = [html.unescape(p) for p in paras if p]
        items.append({"num": num, "text": "\n\n".join(paras)})
    items.sort(key=lambda x: x["num"])
    return items

def main():
    ap = argparse.ArgumentParser(description="用 Gemini TTS 为 PTE Describe Image 范文生成朗读音频")
    ap.add_argument("html")
    ap.add_argument("--model", default="gemini-3.1-flash-tts-preview")
    ap.add_argument("--voice", default="Charon")
    ap.add_argument("--only", default="")
    ap.add_argument("--delay", type=float, default=3.0)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    html_text = open(a.html, encoding="utf-8").read()
    items = extract_items(html_text)
    audio_dir = os.path.join(os.path.dirname(a.html), "audio")

    total = sum(len(it["text"]) for it in items)
    print(f"共 {len(items)} 题，{total} 字符  模型：{a.model}  声音：{a.voice}")
    if a.dry_run:
        for it in items:
            print(f"  [item{it['num']:02d}] {len(it['text']):>4} 字符")
        return

    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key: sys.exit("请先设置环境变量 GEMINI_API_KEY。")
    only = {int(x) for x in a.only.split(",") if x.strip()}
    os.makedirs("tts_cache", exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    for it in items:
        if only and it["num"] not in only:
            continue
        prompt = build_prompt(it["text"])
        h = hashlib.sha1(f"{a.model}|{a.voice}|{prompt}".encode()).hexdigest()[:16]
        cache_path = os.path.join("tts_cache", f"item{it['num']:02d}_{h}.pcm")
        out_path = os.path.join(audio_dir, f"item{it['num']:02d}.mp3")
        if os.path.exists(cache_path):
            pcm = open(cache_path, "rb").read(); tag = "缓存"
        else:
            print(f"  [item{it['num']:02d}/{len(items)}] 生成中…（{len(it['text'])} 字符）")
            pcm = trim_silence(call_tts(key, a.model, a.voice, prompt))
            open(cache_path, "wb").write(pcm); tag = "完成"
            time.sleep(a.delay)
        open(out_path, "wb").write(to_mp3(pcm))
        dur = len(pcm) / 2 / RATE
        print(f"  [item{it['num']:02d}] {tag}  {dur:5.1f}s  -> {out_path}")

    print("\n✓ 全部完成。")

if __name__ == "__main__":
    main()
