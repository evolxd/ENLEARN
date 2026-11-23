"""Rebuild every group-<id>.mp3 and its cues from the single-word audio (see groups.py for the layout).
usage: python rebuild_groups.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import groups
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'index.html')
t = open(PAGE, encoding='utf-8', newline='').read()
i = t.find('window.DICTATION_AUDIO='); j = t.find(';</script>', i)
m = json.loads(t[i + len('window.DICTATION_AUDIO='):j])
m['sessions'] = [groups.build_session(ROOT, m['words'], s['title'], s['ids'], s['id']) for s in m['sessions']]
m['version'] += 1
t = t[:i] + 'window.DICTATION_AUDIO=' + json.dumps(m, ensure_ascii=False, separators=(',', ':')) + t[j:]
open(PAGE, 'w', encoding='utf-8', newline='').write(t)
print('rebuilt', len(m['sessions']), 'sessions; version', m['version'])
