# Part III — PTE High Frequency Lexicon

Status: In progress — 240 of 300–500 words drafted; see `ROADMAP.md` Stage 5

**Batch size changed to 60 words per pass, per user direction (this
session)**, effective Batch 7 onward. Batch 7 (`words_181-210.md` +
`words_211-240.md`, split across two files for editing convenience but
counted as one 60-word batch) covers words 181–240. Batches 1–6 remain
30 words each, unchanged retroactively.

Batches 1–7 (`words_001-030.md` through `words_211-240.md`) cover 240
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
- **Science/tech/environment + health/psychology/history cluster**
  (Batch 7, 60 words): *climate, species, ecosystem, sustainable,
  emission, pollution, molecule, organism, artificial intelligence,
  algorithm* / *medicine, treatment, diagnosis, disease, virus, vaccine,
  psychology, behavior, emotion, memory* / *history, culture, century,
  ancient, civilization, tradition, religion* — the widest topical spread
  of any batch so far, matching Read Aloud's actual passage-topic variety.
- **"-ity" joins the suffix-stress family** (Batch 7): *sustainability*,
  *biodiversity* — first concrete data points, following the same
  before-the-suffix stress pattern as "-tion"/"-ic".
- **"-ical" confirmed as an extension of "-ic," not a new rule** (Batch 7):
  *history* (stress 1) → *historical* (stress 2, shifts) is the first
  concrete shift example; contrasted directly with *culture*/*cultural*
  (no shift) to show "-al" alone doesn't trigger it.
- **Medial-position /ð/ and third/fourth silent-letter examples** (Batch
  7): *algorithm* (medial /ð/, vs. prior word-initial-only examples);
  *psychology* (silent "p"), alongside *process* (Batch 2) and
  *knowledge*/*vehicle* (Batches 3, 7).
- **New near-minimal pair**: *quantity*/*quality* (Batch 7) — distinguished
  by a single medial consonant, both extremely high-frequency in Describe
  Image/Essay.
- **z→s devoicing thread continues**: *organism*, *mechanism*, *disease*
  (Batch 7, the last with /z/ in two positions) join *reasonable*,
  *represent*, *organization*.

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

Decision (recorded 2026-08-05, revised same day): entries were initially
batched into files of 30 words each (Batches 1–6), then changed to 60
words per pass per user direction, effective Batch 7 onward. A 60-word
batch may be split across two `words_NNN-NNN.md` files for editing
convenience (e.g. Batch 7 = `words_181-210.md` + `words_211-240.md`) but
is tracked as a single batch in the Progress table below. Every entry
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
| 7 | 181–240 (60 words) | Draft (`words_181-210.md` + `words_211-240.md`) |
| 8 | 241–300 (60 words) | Not started |

(Add rows as batches are planned/started. Batch size is 60 words from
Batch 7 onward.)
