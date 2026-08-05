# Changelog / 更新日志

All notable changes to the PTE Pronunciation Bible are logged here, newest
first. This tracks the book's content history; see `ROADMAP.md` for planned
work and `PROJECT.md` §7 for release-version scope.

## [Unreleased]

### Changed

- Scoped Part IV (Chinese Error Corpus) to Mandarin only, per user
  direction (this project does not need Cantonese coverage — it is for
  personal use). Removed the Cantonese-vs-Mandarin sourcing caveats and
  the ROADMAP task to find a Mandarin-specific replacement for the
  Cantonese-sourced connected-speech study in Ch.3/Ch.4; that source is
  now cited plainly as related Chinese-L1 evidence. Updated
  `book/Part04_ErrorCorpus/README.md`, `01_top-pronunciation-mistakes.md`,
  `03_top-rhythm-mistakes.md`, `04_top-linking-mistakes.md`,
  `_TEMPLATE_LEXICON_ENTRY.md`, `ROADMAP.md`, and `REFERENCES.md`
  accordingly.

### Added

- Part V — Question Strategy: all 10 chapters written in Draft status,
  applying Part I's scoring model and Part II/IV's pronunciation and error
  mechanisms to each PTE Academic item type:
  - `01_read-aloud.md`, `02_repeat-sentence.md`, `03_describe-image.md`,
    `04_retell-lecture.md`, `05_respond-to-situation.md` (speaking items —
    this book's core focus)
  - `06_summarize-written-text.md`, `07_write-email.md`, `08_essay.md`,
    `09_reading.md` (writing/reading items, intentionally lighter-touch,
    each with an explicit scope note)
  - `10_listening.md` (connects directly back to Part II's connected-speech
    mechanisms, applied to decoding rather than production)
  Format/timing details throughout are secondary-sourced (primary Pearson
  pages returned 403 this session) and flagged for re-verification. Ch.7
  (Write Email) carries an unresolved PTE Academic vs PTE Core module-scope
  question — see `book/Part05_Strategy/README.md` and `ROADMAP.md` Stage 4.
- Part IV — Chinese Error Corpus: all 5 chapters written in Draft status,
  each cataloguing documented Mandarin-L1 error patterns with mechanism,
  examples, and correction targets, cross-referenced back to Part II
  definitions rather than re-deriving them:
  - `01_top-pronunciation-mistakes.md`
  - `02_top-stress-mistakes.md`
  - `03_top-rhythm-mistakes.md`
  - `04_top-linking-mistakes.md`
  - `05_top-vowel-mistakes.md`
  Grounded in peer-reviewed/research-literature sources (JASA, ScienceDirect,
  Frontiers/PMC, Cambridge Core, ERIC, ResearchGate) found and cited
  directly in this session — a stronger evidence base than Part II's
  general-phonetics placeholders. Two open items flagged for the Stage 7
  verification pass: Ch.4's primary source studied Cantonese, not Mandarin,
  speakers; Ch.5 extends a directly-researched finding to other vowel pairs
  as a tagged `[Hypothesis]`. See `book/Part04_ErrorCorpus/README.md` and
  `ROADMAP.md` Stage 3.
- Part II — Pronunciation Foundations: all 9 chapters written in Draft
  status (same bilingual format as Part I), each with the full six-section
  template and evidence tags:
  - `01_ipa.md`
  - `02_consonants.md`
  - `03_vowels.md`
  - `04_word-stress.md`
  - `05_sentence-rhythm.md`
  - `06_connected-speech.md`
  - `07_reduction.md`
  - `08_linking.md`
  - `09_incomplete-plosion.md`
  Core IPA/phonetics facts are well-established linguistics, cross-checked
  against the IPA chart and Cambridge/Oxford dictionaries. Several
  general-phonetics and Mandarin-phonology claims are tagged `[Linguistics]`
  with a placeholder note requesting a specific academic citation during
  the Stage 7 verification pass — see `book/Part02_Pronunciation/README.md`
  and `ROADMAP.md` Stage 2.
- Part I — Understanding the PTE AI: all 5 chapters written in Draft status
  (bilingual: English prose with Chinese glosses on key terms), each with
  Learning Objectives, Theory, Examples, Exam Strategy, Exercises, Summary,
  and References:
  - `01_how-the-pte-ai-scores-you.md`
  - `02_pronunciation-vs-accent.md`
  - `03_fluency.md`
  - `04_content.md`
  - `05_common-myths.md`
  Claims are tagged per `STYLE_GUIDE.md` (`[Pearson]`/`[Linguistics]`/
  `[Practice]`/`[Hypothesis]`). Sources logged in `REFERENCES.md`. Note:
  the official Pearson Score Guide PDF and accent-policy article could not
  be fetched directly in this session (403 from the fetch tool); band
  descriptors were cross-verified against multiple independent secondary
  sources instead. This is flagged in each chapter's References and in
  `book/Part01_AI/README.md` as outstanding verification work before any
  chapter is marked Done.
- Initial project scaffold:
  - Governance docs: `PROJECT.md`, `ROADMAP.md`, `STYLE_GUIDE.md`,
    `REFERENCES.md`, `CONTRIBUTING.md`, `CHANGELOG.md`
  - `book/` directory with one folder per Part (I–VI), each with a
    `README.md` listing planned chapters
  - Chapter template: `book/_TEMPLATE_CHAPTER.md`
  - Lexicon entry template: `book/_TEMPLATE_LEXICON_ENTRY.md`
  - `database/` with empty, header-only CSVs: `words.csv`, `ipa.csv`,
    `stress.csv`, `errors.csv`, `frequency.csv`
  - `assets/images/`, `assets/diagrams/`, `assets/audio/` placeholders

No chapter content has been written yet — this release is scaffold-only.
