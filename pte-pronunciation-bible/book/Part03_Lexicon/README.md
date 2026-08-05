# Part III — PTE High Frequency Lexicon

Status: In progress — Batches 1–6 drafted (180 of 300–500 words; see `ROADMAP.md` Stage 5)

Batches 1–6 (`words_001-030.md` through `words_151-180.md`) cover 180
high-frequency academic/PTE words, each with a full lexicon entry and
matching rows in all five `database/*.csv` files. IPA/stress are drawn
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
- **Noun/verb stress-shift pairs** beyond Part II Ch.4's *record*/*present*:
  *increase*/*decrease*, *impact* (Batch 2), *contrast* (Batch 4) — with
  *decline* (Batch 4) flagged as a **non-example** (same stress in both
  forms), useful for testing whether the rule is over-applied.
- **Adjective/verb suffix-vowel alternation** (new pattern, Batch 4):
  *appropriate*, *approximate* — same stress position, different final
  vowel by grammatical role; distinct mechanism from the stress-shift
  pairs above.
- **"-tion"/"-ic" suffix-stress rule** (Part II Ch.4): 7 "-tion" words plus
  "-ic" words (*economic*, Batch 3; *dramatic*, Batch 4) and a stress-shift
  pair (*economy*/*economic*, directly mirroring Part II Ch.4's
  *photograph* family).
- **Spelling-predicted mispronunciation** (Part II Ch.1): *process* (Batch
  2), *knowledge* (Batch 3).
- **Word-final single-consonant deletion/epenthesis** (Part IV Ch.1
  Mistake 3, distinct from cluster-simplification Mistake 4): *benefit*,
  *advantage*, *knowledge* (Batch 3); *rapid*, *percentage*, *average*
  (Batch 4).
- **z→s devoicing** (new `[Hypothesis]`-tagged extension, Batch 4,
  *reasonable*, *represent*): Mandarin's lack of a phonemic voiced/
  voiceless fricative contrast — not directly researched in this book's
  sources, flagged with extra caution.
- **Describe Image data-description cluster** (Batch 4): trend words
  (*dramatic, gradual, steady, rapid, decline, fluctuate*) and comparison
  words (*proportion, percentage, majority, minority, average, overall,
  compare, contrast, similar, differ, equivalent, correspond, represent*)
  — the first batch organized around a single PTE item type's vocabulary.
- **Essay discourse-connector cluster** (Batch 5): *thus, despite,
  nevertheless, furthermore, moreover, in addition, regarding* — the
  counterpart to Batch 4's Describe Image cluster, oriented toward Part V
  Ch.8.
- **Stress-stability non-shift checks** (extending Batch 4's *decline*):
  *argue*/*argument*, *consequence*/*consequently*, *improve*/
  *improvement* all keep the same stressed syllable across the word
  family; *encourage*/*discourage* confirm that "en-"/"dis-" prefixes
  don't move stress off the root either.
- **First /ɔɪ/ diphthong example**: *avoid* (Batch 5) — none of the prior
  120 words used this diphthong.
- **Stress-variability caution vs. confirmed stress pairs**: *address*
  (Batch 5) is flagged as uncertain/variable across dictionary sources,
  explicitly distinguished from the confirmed stress-shift pairs
  (*increase/decrease*, *impact*, *contrast*) — a reminder not to overstate
  confidence where sources actually disagree.
- **Academic/workplace cluster** (Batch 6): *university, institution,
  curriculum, assignment, lecture, seminar, graduate, degree, career,
  employment/employee/employer, workplace, management, organization,
  academic*, etc. — high-frequency across Read Aloud, Retell Lecture, and
  Essay; thematically fitting since the book's own test is "PTE Academic."
- **Second confirmed suffix-stress rule — "-ee"/"-eer"** (Batch 6):
  unlike "-tion"/"-ic" (stress lands *before* the suffix), "-ee"/"-eer"
  pull stress *onto* the suffix itself. *Employee* (shifted) contrasts
  directly with *employ*/*employer*/*employment* (not shifted); *career*
  and *volunteer* confirm the same pattern for "-eer."
- Fourth data point for the adjective/verb suffix-vowel alternation:
  *graduate* (Batch 6), alongside *appropriate*/*approximate* (Batch 4).
- More stress-stable non-shift pairs (Batch 6): *management*/*manage*,
  *participate*/*participant*.

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
| 4 | 91–120 | Draft (`words_091-120.md`) |
| 5 | 121–150 | Draft (`words_121-150.md`) |
| 6 | 151–180 | Draft (`words_151-180.md`) |
| 7 | 181–210 | Not started |

(Add rows as batches are planned/started.)
