# Roadmap / 开发路线

This roadmap tracks the build order for the PTE Pronunciation Bible. It is
separate from the [Version Control Plan](./PROJECT.md#7-version-control-plan)
in `PROJECT.md`, which tracks *release* versions of the finished book.
This file tracks *build* stages — what gets written in what order.

## Stage 0 — Scaffold (current)

- [x] Repository layout: `book/`, `database/`, `assets/`
- [x] Governance docs: `PROJECT.md`, `STYLE_GUIDE.md`, `REFERENCES.md`,
      `CONTRIBUTING.md`, `CHANGELOG.md`, `ROADMAP.md`
- [x] Chapter template (`book/_TEMPLATE_CHAPTER.md`)
- [x] Lexicon entry template (`book/_TEMPLATE_LEXICON_ENTRY.md`)
- [x] Empty database CSVs with finalized headers
- [x] Part-level `README.md` placeholders listing planned chapters

## Stage 1 — Part I: Understanding the PTE AI

Conceptual chapters, lowest dependency on verified IPA/audio data. Good
first target for full-quality writing.

- [x] Ch.1 How the PTE AI Scores You (Draft)
- [x] Ch.2 Pronunciation vs Accent (Draft)
- [x] Ch.3 Fluency (Draft)
- [x] Ch.4 Content (Draft)
- [x] Ch.5 Common Myths (Draft)
- [ ] Verify all Ch.1-5 `[Pearson]` claims against the primary Score Guide
      PDF directly (blocked by 403 in the scaffold/draft session — see
      `book/Part01_AI/README.md`) before moving chapters to Done

## Stage 2 — Part II: Pronunciation Foundations

Requires verified IPA against Cambridge/Oxford dictionary entries before
publication.

- [x] IPA (Draft)
- [x] Consonants (Draft)
- [x] Vowels (Draft)
- [x] Word Stress (Draft)
- [x] Sentence Rhythm (Draft)
- [x] Connected Speech (Draft)
- [x] Reduction (Draft)
- [x] Linking (Draft)
- [x] Incomplete Plosion (Draft)
- [ ] Add specific academic citations for the general phonetics/Mandarin-
      phonology claims flagged as placeholders in Ch.2, Ch.5, Ch.6, Ch.7,
      Ch.8, Ch.9 References sections, before moving chapters to Done

## Stage 3 — Part IV: Chinese Error Corpus

Depends on Stage 2 terminology (needs Part II definitions in place first).

- [x] Top pronunciation mistakes (Draft)
- [x] Top stress mistakes (Draft)
- [x] Top rhythm mistakes (Draft)
- [x] Top linking mistakes (Draft)
- [x] Top vowel mistakes (Draft)
- [ ] Ch.5: source direct research on tense/lax pairs beyond /iː/–/ɪ/
      to convert the `[Hypothesis]`-tagged extension into `[Linguistics]`

## Stage 4 — Part V: Question Strategy

Depends on Stage 1 (AI scoring model) and Stage 2 (pronunciation vocabulary).

- [x] Read Aloud (Draft)
- [x] Repeat Sentence (Draft)
- [x] Describe Image (Draft)
- [x] Retell Lecture (Draft)
- [x] Respond to Situation (Draft)
- [x] Summarize Written Text (Draft)
- [x] Write Email (Draft — module-scope unresolved, see below)
- [x] Essay (Draft)
- [x] Reading (Draft)
- [x] Listening (Draft)
- [ ] Re-verify all format/timing figures (prep/response windows, word
      counts, time limits) across Part V against the primary Pearson
      test-format pages once accessible (403 on direct fetch this session)
- [ ] Resolve whether Ch.7 Write Email belongs in PTE Academic or is
      PTE-Core-only; update or remove the chapter accordingly

## Stage 5 — Part III: PTE High Frequency Lexicon (300–500 words)

Highest verification cost per unit (IPA + stress + Chinese learner error
notes per word). Data lives in `database/*.csv`; chapter prose in
`book/Part03_Lexicon/` renders from it. Build incrementally in batches of
30 words at a time (adjusted down from the originally planned 50 — see
`book/Part03_Lexicon/README.md`).

- [x] Batch 1 (words 1–30) — Draft, `words_001-030.md`
- [x] Batch 2 (words 31–60) — Draft, `words_031-060.md`
- [x] Batch 3 (words 61–90) — Draft, `words_061-090.md`
- [x] Batch 4 (words 91–120) — Draft, `words_091-120.md`
- [ ] Individually cross-check Batches 1–4's IPA/stress against Cambridge
      or Oxford Learner's Dictionaries (this session's direct fetch
      attempts returned 403) before marking any batch Done
- [ ] Batch 5 (words 121–150)
- [ ] ... continue in batches of 30 until 300–500 words are covered

## Stage 6 — Part VI: Training System

Depends on all prior parts (references chapters from I, II, III, IV, V).

- [ ] 15-Day Plan
- [ ] 30-Day Plan
- [ ] 60-Day Plan
- [ ] 90-Day Plan

## Stage 7 — Version 1.0 publication pass

- [ ] Run the Quality Checklist (`PROJECT.md` §5) against every chapter
- [ ] Deduplicate explanations across parts
- [ ] External IPA/stress verification pass
- [ ] Freeze as Version 1.0
