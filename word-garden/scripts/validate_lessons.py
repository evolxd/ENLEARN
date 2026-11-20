"""Automatic acceptance checks (A1-A9) for newly added spelling lessons. See docs/ACCEPTANCE_STANDARD.md.

usage: python validate_lessons.py [first_id] [last_id]   (default 200..)
"""
import json, os, re, statistics, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lo = int(sys.argv[1]) if len(sys.argv) > 1 else 200
hi = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6
t = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
errs = []
def bad(code, msg): errs.append(f'{code}: {msg}')

entries = []
for m in re.finditer(r'const lesson(\d+)Entries=', t):
    try:
        arr, _end = json.JSONDecoder().raw_decode(t[m.end():])
    except ValueError:
        continue
    entries += [dict(e, _lesson=int(m.group(1))) for e in arr]
new = sorted([e for e in entries if lo <= e['id'] <= hi], key=lambda e: e['id'])
old_words = set(x.lower() for x in re.findall(r'"en":\s*"([^"]+)"', t))
for line in re.findall(r'^\s*([A-Za-z\' ]+)\|[^|\n]+\|[^|\n]+\|[^|\n]+$', t, re.M): old_words.add(line.strip().lower())
i = t.find('window.DICTATION_AUDIO='); j = t.find(';</script>', i)
M = json.loads(t[i + len('window.DICTATION_AUDIO='):j])
k = t.find('const EN_DEFS='); e2 = t.find('};', k); DEFS = json.loads(t[k + len('const EN_DEFS='):e2 + 1])

def dur(f):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout or 0)

# A1 structure
ids = [e['id'] for e in new]
if not new: bad('A1', 'no entries in range')
if len(ids) != len(set(ids)): bad('A1', 'duplicate ids')
if ids and ids != list(range(ids[0], ids[0] + len(ids))): bad('A1', 'ids not consecutive')
if len(new) % 20: bad('A1', f'{len(new)} words is not a multiple of 20')
sess = [s for s in M['sessions'] if s['ids'] and lo <= s['ids'][0] <= hi]
if len(sess) * 10 != len(new) or any(len(s['ids']) != 10 for s in sess): bad('A1', 'sessions are not 10 words each / count mismatch')
# A2 duplicates
seen = {}
for e in new:
    w = e['en'].lower()
    if w in old_words and sum(1 for x in re.findall(r'"en":\s*"%s"' % re.escape(e['en']), t)) > 1: bad('A2', f'{w} duplicates an existing entry')
    if w in seen: bad('A2', f'{w} repeated in batch')
    seen[w] = 1
# A3-A6 fields
def variants(w):
    w = w.lower(); out = {w, w + 's', w + 'es', w + 'ed', w + 'ing', w + 'd', w + 'ly', w + 'er', w + 'est'}
    if w.endswith('e'): out |= {w[:-1] + 'ing', w[:-1] + 'ed'}
    if w.endswith('y'): out |= {w[:-1] + 'ies', w[:-1] + 'ied', w[:-1] + 'ier', w[:-1] + 'ily'}
    if w.endswith('ght'): pass
    return out
for e in new:
    w = e['en']; tag = f'{w}({e["id"]})'
    for f in ('en', 'zh', 'chunks', 'ipa', 'sounds', 'tip', 'memory', 'ex', 'cn', 'pattern'):
        if not str(e.get(f, '')).strip(): bad('A3', f'{tag} empty {f}')
    if len(e['chunks'].split('·')) != len(e['sounds'].split('·')): bad('A4', f'{tag} chunks/sounds mismatch')
    if e['chunks'].replace('·', '').lower() != w.lower(): bad('A4', f'{tag} chunks do not spell the word: {e["chunks"]}')
    if len(e['chunks'].split('·')) > 1 and not any(c.isupper() for c in e['chunks']): bad('A4', f'{tag} no stressed syllable')
    toks = re.findall(r"[A-Za-z']+", e['ex'].lower())
    if len(toks) > 12: bad('A5', f'{tag} example has {len(toks)} words')
    if not (set(toks) & variants(w)): bad('A5', f'{tag} example lacks the word')
    d = DEFS.get(str(e['id']), '')
    dt = re.findall(r"[A-Za-z']+", d.lower())
    if not d: bad('A6', f'{tag} no definition')
    if len(dt) > 15: bad('A6', f'{tag} definition has {len(dt)} words')
    if w.lower() in dt: bad('A6', f'{tag} definition contains the word')
# A7-A9 audio
rates = []
for e in new:
    for p in (f'audio/word-{e["id"]}.mp3', f'audio/def-{e["id"]}.mp3'):
        f = os.path.join(ROOT, p)
        if not os.path.exists(f) or os.path.getsize(f) < 1500: bad('A7', f'missing/empty {p}')
    wm = M['words'].get(str(e['id']))
    if not wm: bad('A8', f'{e["en"]} has no word manifest'); continue
    sg = wm['segments']
    if len(sg) != 4 or any(sg[x]['end'] <= sg[x]['start'] for x in range(4)) or any(sg[x + 1]['start'] < sg[x]['end'] for x in range(3)): bad('A8', f'{e["en"]} bad segments')
    df = os.path.join(ROOT, f'audio/def-{e["id"]}.mp3')
    if os.path.exists(df):
        dd = dur(df); n = len(re.findall(r"[A-Za-z']+", DEFS.get(str(e['id']), '')))
        if dd > 0: rates.append(n / dd)
for s in sess:
    f = os.path.join(ROOT, s['url'])
    if not os.path.exists(f) or os.path.getsize(f) < 1500: bad('A7', f'missing {s["url"]}'); continue
    if abs(dur(f) - s['duration']) > 0.2: bad('A8', f'{s["url"]} duration {dur(f):.2f} vs manifest {s["duration"]:.2f}')
    if len(s['cues']) != 40: bad('A8', f'{s["url"]} has {len(s["cues"])} cues')
if rates:
    med = statistics.median(rates)
    ref = [len(re.findall(r"[A-Za-z']+", DEFS[str(i)])) / dur(os.path.join(ROOT, f'audio/def-{i}.mp3')) for i in (181, 184, 188, 191, 195, 198) if os.path.exists(os.path.join(ROOT, f'audio/def-{i}.mp3'))]
    if ref:
        rm = statistics.median(ref)
        if not (0.6 * rm <= med <= 1.2 * rm): bad('A9', f'definition pace {med:.2f} w/s vs reference {rm:.2f}')
        print(f'pace: batch {med:.2f} w/s, reference {rm:.2f} w/s')
print(f'{len(new)} words, {len(sess)} sessions checked')
if errs:
    print('\n'.join(errs)); sys.exit(1)
print('ALL AUTOMATIC CHECKS PASSED')
