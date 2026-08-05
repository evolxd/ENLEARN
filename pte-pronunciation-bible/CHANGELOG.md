# Changelog / 更新日志

All notable changes to the PTE Pronunciation Bible are logged here, newest
first. This tracks the book's content history; see `ROADMAP.md` for planned
work and `PROJECT.md` §7 for release-version scope.

## [Unreleased]

### Added

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
