# Part III — PTE High Frequency Lexicon

Status: In progress — Batches 1–3 drafted (90 of 300–500 words; see `ROADMAP.md` Stage 5)

Batches 1–3 (`words_001-030.md`, `words_031-060.md`, `words_061-090.md`)
cover 90 high-frequency academic/PTE words, each with a full lexicon entry
and matching rows in all five `database/*.csv` files. IPA/stress are drawn
from standard dictionary knowledge (Cambridge/Oxford direct fetch returned
403 this session, same limitation as elsewhere in this project) and need
individual cross-check before Done. "AI Recognition Notes" and "PTE
Frequency" fields are author judgment/reasoned extensions, explicitly
tagged `Hypothesis`/`Practice` in the data — not verified PTE
frequency-list or ASR-behavior data. See the sourcing note at the top of
each batch file for full detail.

Running cross-batch threads to keep extending in future batches:
- **Coda-position /v/ pattern**: *comprehensive* (Batch 1) → *perspective*,
  *achieve* (Batch 2) — still pending direct research confirmation.
- **Noun/verb stress pairs** beyond Part II Ch.4's *record*/*present*:
  *increase*/*decrease*, *impact* (Batch 2).
- **"-tion"/"-ic" suffix-stress rule** (Part II Ch.4): 7 "-tion" words plus
  one "-ic" word and a stress-shift pair (*economy*/*economic*, directly
  mirroring Part II Ch.4's *photograph* family) in Batch 3 alone.
- **Spelling-predicted mispronunciation** (Part II Ch.1): *process* (Batch
  2, "o" read as /oʊ/ instead of /ɑː/), *knowledge* (Batch 3, silent "k").
- **Word-final single-consonant deletion/epenthesis** (Part IV Ch.1
  Mistake 3, distinct from the cluster-simplification Mistake 4): now
  explicitly tracked separately starting in Batch 3 (*benefit*, *advantage*,
  *knowledge*).

Target: 300–500 words. Every word must have a complete entry following
`book/_TEMPLATE_LEXICON_ENTRY.md`, with a matching row in each
`database/*.csv` file. This is the highest per-unit verification cost in
the book (IPA + stress + Chinese learner error notes per word) — build it
incrementally in batches rather than all at once, per `ROADMAP.md` Stage 5.

## Entry Fields

Word · IPA · Stress · Part of Speech · Meaning · Chinese Translation ·
Common Mistakes · Chinese Learner Errors · AI Recognition Notes ·
Related Words · Example · Shadowing · Practice · Difficulty · Frequency ·
References

## Structure

Decision (recorded 2026-08-05): entries are batched into files of 30 words
each (`words_001-030.md`, `words_031-060.md`, ...) rather than the
originally planned 50, sized for one authoring pass per batch. Every entry
must also be reflected as one row per relevant field in:

- `database/words.csv`
- `database/ipa.csv`
- `database/stress.csv`
- `database/errors.csv`
- `database/frequency.csv`

See `CONTRIBUTING.md` for the full authoring workflow.

## Progress

| Batch | Words | Status |
|---|---|---|
| 1 | 1–30 | Draft (`words_001-030.md`) |
| 2 | 31–60 | Draft (`words_031-060.md`) |
| 3 | 61–90 | Draft (`words_061-090.md`) |
| 4 | 91–120 | Not started |

(Add rows as batches are planned/started.)
