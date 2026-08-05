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

- [ ] Ch.1 How the PTE AI Scores You
- [ ] Ch.2 Pronunciation vs Accent
- [ ] Ch.3 Fluency
- [ ] Ch.4 Content
- [ ] Ch.5 Common Myths

## Stage 2 — Part II: Pronunciation Foundations

Requires verified IPA against Cambridge/Oxford dictionary entries before
publication.

- [ ] IPA
- [ ] Consonants
- [ ] Vowels
- [ ] Word Stress
- [ ] Sentence Rhythm
- [ ] Connected Speech
- [ ] Reduction
- [ ] Linking
- [ ] Incomplete Plosion

## Stage 3 — Part IV: Chinese Error Corpus

Depends on Stage 2 terminology (needs Part II definitions in place first).

- [ ] Top pronunciation mistakes
- [ ] Top stress mistakes
- [ ] Top rhythm mistakes
- [ ] Top linking mistakes
- [ ] Top vowel mistakes

## Stage 4 — Part V: Question Strategy

Depends on Stage 1 (AI scoring model) and Stage 2 (pronunciation vocabulary).

- [ ] Read Aloud
- [ ] Repeat Sentence
- [ ] Describe Image
- [ ] Retell Lecture
- [ ] Respond to Situation
- [ ] Summarize Written Text
- [ ] Write Email
- [ ] Essay
- [ ] Reading
- [ ] Listening

## Stage 5 — Part III: PTE High Frequency Lexicon (300–500 words)

Highest verification cost per unit (IPA + stress + Chinese learner error
notes per word). Data lives in `database/*.csv`; chapter prose in
`book/Part03_Lexicon/` renders from it. Build incrementally in batches
(e.g., 50 words at a time) rather than all at once.

- [ ] Batch 1 (words 1–50)
- [ ] Batch 2 (words 51–100)
- [ ] ... continue in batches of 50 until 300–500 words are covered

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
