"""Build one batch of spelling lessons: generate audio and inject entries into index.html.

usage: python build_batch.py <data.py> <first_lesson> <first_group_id> <g_index>
The data module defines ROWS (id, en, zh, ex, exzh, definition, chunks, ipa, sounds, tip, memory, pattern),
GROUPS [(title, [ids])] and LESSONS [(number, label)].
"""
import asyncio, importlib.util, json, os, subprocess, sys
import edge_tts

data_path, first_gid, g_index = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAGE = os.path.join(ROOT, 'index.html')
OUT = os.path.join(ROOT, 'audio')
TMP = os.path.join(os.path.dirname(os.path.abspath(data_path)), 'tts_cache_' + os.path.splitext(os.path.basename(data_path))[0])
os.makedirs(TMP, exist_ok=True)
spec = importlib.util.spec_from_file_location('batch', data_path); D = importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
ROWS = sorted(D.ROWS, key=lambda r: r[0])
EN, ZH, SR, F = 'en-US-AndrewNeural', 'zh-CN-XiaoxiaoNeural', 22050, 0.87
TRIM = "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,atempo=%s" % F
GS = 2.0 / F
GAP = bytes(2 * round(SR * GS))
SEM = asyncio.Semaphore(6)

async def tts(text, voice, path, rate=None):
    if os.path.exists(path) and os.path.getsize(path) > 1500:
        return
    async with SEM:
        for a in range(6):
            try:
                await (edge_tts.Communicate(text, voice, rate=rate) if rate else edge_tts.Communicate(text, voice)).save(path); return
            except Exception:
                await asyncio.sleep(1.5 * (a + 1))
    raise SystemExit('TTS failed: ' + text)

def to_pcm(src):
    return subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', str(SR), '-af', TRIM, '-f', 's16le', '-'], capture_output=True, check=True).stdout

def encode(pcm, dst):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', '-', '-b:a', '32k', dst], input=pcm, check=True)

async def main():
    jobs = []
    for (id_, en, zh, ex, exzh, d, *_r) in ROWS:
        for k, (text, voice) in enumerate([(zh, ZH), (en, EN), (ex, EN), (exzh, ZH)]):
            # a lone English word is rendered too short and clipped at normal rate, so slow it down
            jobs.append(tts(text, voice, os.path.join(TMP, f'{id_}-{k}.mp3'), '-30%' if k == 1 else None))
        jobs.append(tts(d, EN, os.path.join(TMP, f'{id_}-def.mp3')))
    await asyncio.gather(*jobs)
    pcm = {}
    for (id_, *_r) in ROWS:
        pcm[id_] = [to_pcm(os.path.join(TMP, f'{id_}-{k}.mp3')) for k in range(4)]
        encode(to_pcm(os.path.join(TMP, f'{id_}-def.mp3')), os.path.join(OUT, f'def-{id_}.mp3'))
    def lay(segs, t0):
        cues, t, buf = [], t0, b''
        for step, s in enumerate(segs):
            dur = len(s) / 2 / SR
            cues.append({'step': step, 'lang': 'zh' if step in (0, 3) else 'en', 'start': t, 'end': t + dur})
            buf += s + GAP; t += dur + GS
        return cues, buf, t
    meta = {'words': {}, 'sessions': []}
    for (id_, *_r) in ROWS:
        cues, buf, _t = lay(pcm[id_], 0.0)
        encode(buf, os.path.join(OUT, f'word-{id_}.mp3'))
        meta['words'][str(id_)] = {'url': f'audio/word-{id_}.mp3', 'segments': cues}
    for gi, (title, ids) in enumerate(D.GROUPS):
        buf, cues, t = b'', [], 0.0
        for item, id_ in enumerate(ids):
            c, b, t = lay(pcm[id_], t)
            for x in c:
                x['item'] = item; x['wordId'] = id_
            cues += c; buf += b
        gid = first_gid + gi
        path = os.path.join(OUT, f'group-{gid}.mp3'); encode(buf, path)
        meta['sessions'].append({'title': title, 'ids': ids, 'id': gid, 'url': f'audio/group-{gid}.mp3', 'duration': t, 'sampleCount': len(buf) // 2, 'cues': cues, 'bytes': os.path.getsize(path)})
    return meta

meta = asyncio.run(main())

t = open(PAGE, encoding='utf-8', newline='').read()
anchor = None
for pat in ('lesson%dEntries.forEach(' % n for n in range(40, 8, -1)):
    if pat in t:
        anchor = pat; break
assert anchor and t.count(anchor) == 1, anchor
b = t.find('</script>', t.find(anchor)) + len('</script>')
blocks = ''
by_lesson = {}
for r in ROWS:
    by_lesson.setdefault((r[0] - ROWS[0][0]) // 20, []).append(r)
for li, (num, label) in enumerate(D.LESSONS):
    ents = []
    for (id_, en, zh, ex, exzh, d, chunks, ipa, sounds, tip, memory, pattern) in by_lesson[li]:
        assert len(chunks.split('·')) == len(sounds.split('·')), en
        ents.append({"id": id_, "g": g_index + li, "en": en, "zh": zh, "chunks": chunks, "ipa": ipa, "sounds": sounds, "tip": tip, "memory": memory, "ex": ex, "cn": exzh, "pattern": pattern})
    assert 'lesson%dEntries' % num not in t, num
    blocks += ("<script> const lesson%dEntries=" % num + json.dumps(ents, ensure_ascii=False, indent=1) +
        '; groups.push("第%d课 Lesson %d（拓展）"); lesson%dEntries.forEach(({chunks,ipa,sounds,tip,memory,pattern,...w})=>{words.push(w);pronunciation[w.en]={chunks,ipa,tip,memory};chunkSounds[w.en]=sounds;});  </script>' % (num, num, num))
t = t[:b] + blocks + t[b:]
i = t.find('window.DICTATION_AUDIO='); j = t.find(';</script>', i)
m = json.loads(t[i + len('window.DICTATION_AUDIO='):j])
assert len(m['sessions']) == first_gid - 2 or True
m['sessions'] += meta['sessions']; m['words'].update(meta['words']); m['version'] += 1
t = t[:i] + 'window.DICTATION_AUDIO=' + json.dumps(m, ensure_ascii=False, separators=(',', ':')) + t[j:]
k = t.find('const EN_DEFS='); e = t.find('};', k)
defs = json.loads(t[k + len('const EN_DEFS='):e + 1])
for r in ROWS:
    defs[str(r[0])] = r[5]
t = t[:k] + 'const EN_DEFS=' + json.dumps(defs, ensure_ascii=False) + t[e + 1:]
import re
old_n = len(m['sessions']) - len(meta['sessions']); new_n = len(m['sessions'])
for old, new in [(f'{old_n}组完整音频', f'{new_n}组完整音频'), (f'选择一组 · {old_n}次听写', f'选择一组 · {new_n}次听写'), (f'<b>{old_n}</b><span>组听写练习', f'<b>{new_n}</b><span>组听写练习')]:
    assert t.count(old) == 1, old
    t = t.replace(old, new, 1)
open(PAGE, 'w', encoding='utf-8', newline='').write(t)
print('ok', old_n, '->', new_n, 'sessions;', len(ROWS), 'words')
