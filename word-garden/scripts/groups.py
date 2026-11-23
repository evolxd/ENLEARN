"""Group (dictation) audio layout, shared by build_batch.py and rebuild_groups.py.

Per word:  zh meaning | word | EN example | ZH example | 10 s silence | EN example again | ZH example again
Cue steps: 0 zh meaning, 1 word, 2 EN example, 3 ZH example, 4 EN example (repeat), 5 ZH example (repeat).
Single-word files (word-<id>.mp3) keep steps 0-3 only; their segments are the source for the group audio.
"""
import base64, os, subprocess
SR = 22050
GS = 2.0 / 0.87          # normal gap between steps
EX_GAP = 10.0            # silence between the first and second reading of the example
LANG = {0: 'zh', 1: 'en', 2: 'en', 3: 'zh', 4: 'en', 5: 'zh'}

def silence(sec):
    return bytes(2 * round(SR * sec))

def load_pcm(root, url):
    if url.startswith('data:'):
        raw = base64.b64decode(url.split(',', 1)[1])
        return subprocess.run(['ffmpeg', '-v', 'error', '-i', 'pipe:0', '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], input=raw, capture_output=True, check=True).stdout
    return subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(root, url), '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True, check=True).stdout

def cut(pcm, seg):
    a, b = round(seg['start'] * SR) * 2, round(seg['end'] * SR) * 2
    return pcm[a:b]

def lay_word(pieces, t0):
    """pieces: 4 pcm clips (steps 0-3). Returns cues, pcm, end time."""
    order = [0, 1, 2, 3, 4, 5]
    src = {0: pieces[0], 1: pieces[1], 2: pieces[2], 3: pieces[3], 4: pieces[2], 5: pieces[3]}
    cues, buf, t = [], b'', t0
    for step in order:
        s = src[step]; dur = len(s) / 2 / SR
        cues.append({'step': step, 'lang': LANG[step], 'start': t, 'end': t + dur})
        gap = EX_GAP if step == 3 else GS
        buf += s + silence(gap); t += dur + gap
    return cues, buf, t

def encode(pcm, dst):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 's16le', '-ar', str(SR), '-ac', '1', '-i', '-', '-b:a', '32k', dst], input=pcm, check=True)

def build_session(root, words, title, ids, gid):
    """words: manifest 'words' dict. Writes audio/group-<gid>.mp3, returns the session manifest entry."""
    buf, cues, t = b'', [], 0.0
    for item, id_ in enumerate(ids):
        w = words[str(id_)]
        pcm = load_pcm(root, w['url'])
        pieces = [cut(pcm, w['segments'][k]) for k in range(4)]
        c, b, t = lay_word(pieces, t)
        for x in c:
            x['item'] = item; x['wordId'] = id_
        cues += c; buf += b
    path = os.path.join(root, 'audio', f'group-{gid}.mp3'); encode(buf, path)
    return {'title': title, 'ids': ids, 'id': gid, 'url': f'audio/group-{gid}.mp3', 'duration': t, 'sampleCount': len(buf) // 2, 'cues': cues, 'bytes': os.path.getsize(path)}
