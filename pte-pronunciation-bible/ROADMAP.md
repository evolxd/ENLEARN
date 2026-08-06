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
- [x] Write Email (Draft — **module-scope resolved 2026-08-06**: confirmed
      PTE Core–only, kept as supplementary content; see below)
- [x] Essay (Draft)
- [x] Reading (Draft)
- [x] Listening (Draft)
- [ ] Re-verify all format/timing figures (prep/response windows, word
      counts, time limits) across Part V against the primary Pearson
      test-format pages once accessible (403 on direct fetch this session)
- [x] **Resolved (2026-08-06)**: Ch.7 Write Email is PTE Core–only, not
      part of PTE Academic. Confirmed via WebSearch cross-reference
      against multiple independent sources (Cambridge fetch still 403 —
      see `REFERENCES.md` Source Log). PTE Academic uses Write Essay
      (Ch.8) instead. Chapter kept, retitled, and reframed as
      supplementary rather than core curriculum — not removed, since
      readers may also be preparing for PTE Core.

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
- [x] Batch 5 (words 121–150) — Draft, `words_121-150.md` (halfway to the 300 floor)
- [x] Batch 6 (words 151–180) — Draft, `words_151-180.md`
- [x] Batch 7 (words 181–240, 60 words — batch size increased to 60 per
      user direction) — Draft, `words_181-210.md` + `words_211-240.md`
- [x] Batch 8 (words 241–300, 60 words) — Draft, `words_241-270.md` +
      `words_271-300.md` — **300-word floor of the 300–500 target reached**
- [x] Batch 9 (words 301–360, 60 words) — Draft, `words_301-330.md` +
      `words_331-360.md` — user confirmed continuing past 300 toward 500
- [x] Batch 10 (words 361–420, 60 words) — Draft, `words_361-390.md` +
      `words_391-420.md` — 420 of 500 words complete, 80 remain
- [x] Batch 11 (words 421–480, 60 words) — Draft, `words_421-450.md` +
      `words_451-480.md` — 480 of 500 words complete, only 20 remain
- [x] Batch 12 (words 481–500, 20 words) — Draft, `words_481-500.md`
      — **500-word ceiling reached, lexicon complete**
- [x] Spot-check verification pass (2026-08-06): the ~19 highest-risk
      words/pairs flagged across all 12 batches' Source Log entries
      (stress-variable words, loanwords, heteronyms, shift pairs) were
      cross-checked via WebSearch against Cambridge Dictionary/
      Wiktionary aggregation (direct fetch still 403). 17 confirmed,
      1 corrected (*employee*, `database/ipa.csv` and `stress.csv`
      updated), 2 unresolved. See `REFERENCES.md`'s "Verification
      Pass — Lexicon Spot-Check" section for the full table.
- [ ] Full word-by-word cross-check of the remaining ~480 entries
      against Cambridge or Oxford Learner's Dictionaries before
      marking any batch Done — see Stage 7 for the final verification
      pass; recommend direct (non-403) dictionary access for this

## Stage 6 — Part VI: Training System

Depends on all prior parts (references chapters from I, II, III, IV, V).

- [x] 15-Day Plan (Draft) — triages toward Part II/IV mechanism +
      the first ~150–210 lexicon words, given the short timeframe
- [x] 30-Day Plan (Draft) — full Part II/IV/V coverage, lexicon
      through the original 300-word floor (Batches 1–8)
- [x] 60-Day Plan (Draft) — full lexicon as it currently stands
      (Batches 1–16), a second Part II/IV review pass, 3 mock tests
- [x] 90-Day Plan (Draft) — three review cycles (comprehensive,
      targeted, intensive mock-cycling), 5 mock-test checkpoints
- [ ] Re-check all four plans' lexicon batch references once Part III
      reaches its final word count (currently 480/500, see
      `book/Part03_Lexicon/README.md`)

## Stage 7 — Version 1.0 publication pass

- [ ] Run the Quality Checklist (`PROJECT.md` §5) against every chapter
- [ ] Deduplicate explanations across parts
- [ ] External IPA/stress verification pass
- [ ] Freeze as Version 1.0
