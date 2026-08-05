# Part III — PTE High Frequency Lexicon

Status: In progress — Batch 1 drafted (30 of 300–500 words; see `ROADMAP.md` Stage 5)

Batch 1 (`words_001-030.md`) covers 30 high-frequency academic/PTE words,
each with a full lexicon entry and matching rows in all five
`database/*.csv` files. IPA/stress are drawn from standard dictionary
knowledge (Cambridge/Oxford direct fetch returned 403 this session, same
limitation as elsewhere in this project) and need individual cross-check
before Done. "AI Recognition Notes" and "PTE Frequency" fields are author
judgment/reasoned extensions, explicitly tagged `Hypothesis`/`Practice` in
the data — not verified PTE frequency-list or ASR-behavior data. See the
sourcing note at the top of `words_001-030.md` for full detail.

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
| 2 | 31–60 | Not started |

(Add rows as batches are planned/started.)
