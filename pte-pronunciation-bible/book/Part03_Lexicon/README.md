# Part III — PTE High Frequency Lexicon

Status: Planned (no entries written yet — see `ROADMAP.md` Stage 5)

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

Entries may be organized as one file per word, or batched into files of
~50 words each (`words_001-050.md`, `words_051-100.md`, ...) — decide
before Stage 5 begins and record the choice here. Either way, every entry
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
| 1 | 1–50 | Not started |

(Add rows as batches are planned/started.)
