# Contributing / 编写规范

Rules for adding or editing content in this book. Read
[PROJECT.md](./PROJECT.md) and [STYLE_GUIDE.md](./STYLE_GUIDE.md) first —
this file covers the mechanics: templates, file naming, and where things go.

## Where content goes

| Content type | Location |
|---|---|
| A new chapter | `book/PartNN_Name/NN_chapter-slug.md`, copied from `book/_TEMPLATE_CHAPTER.md` |
| A new lexicon word | One row in each relevant `database/*.csv`, plus prose entry in `book/Part03_Lexicon/` copied from `book/_TEMPLATE_LEXICON_ENTRY.md` |
| A new Chinese error pattern | `book/Part04_ErrorCorpus/`, following the same chapter template |
| Images / diagrams | `assets/images/` or `assets/diagrams/`, referenced by relative path from the chapter file |
| Audio (shadowing, examples) | `assets/audio/`, referenced by relative path; filename must match the word/sentence slug it belongs to |

## File naming

- Chapters: `NN_kebab-case-title.md` (e.g. `01_how-the-pte-ai-scores-you.md`)
- Keep the numeric prefix two digits, matching the chapter's position in
  that Part's `README.md` chapter list.
- Lexicon word files (if split one-file-per-word): `word-in-lowercase.md`

## Chapter Template

Every chapter file starts from `book/_TEMPLATE_CHAPTER.md` and must contain
all six sections, in this order:

1. **Learning Objectives** — 3–6 bullet points, each starting with a verb
   ("Explain", "Identify", "Apply"), stating what the reader can do after
   finishing the chapter.
2. **Theory** — the WHY. Grounded in evidence per STYLE_GUIDE.md §1–2.
3. **Examples** — concrete PTE-relevant examples illustrating the theory.
4. **Exam Strategy** — how to apply the theory under exam conditions.
5. **Exercises** — practice tasks the reader can self-check.
6. **Summary** — 3–6 bullets recapping the chapter; no new information.

Do not merge or reorder these sections. If a section genuinely does not
apply, keep the heading and write "Not applicable to this chapter" plus a
one-sentence reason, rather than deleting it — this keeps the format
machine-parseable for the AI/flashcard/course export use case described in
PROJECT.md §2.3.

## Lexicon Entry Template

Every word entry in Part III follows the fields in
`book/_TEMPLATE_LEXICON_ENTRY.md`, matching the columns in `database/*.csv`:

`Word · IPA · Stress · Part of Speech · Meaning · Chinese Translation ·
Common Mistakes · Chinese Learner Errors · AI Recognition Notes ·
Related Words · Example · Shadowing · Practice · Difficulty · Frequency ·
References`

When adding a word:

1. Add one row to `database/words.csv`, `ipa.csv`, `stress.csv`,
   `errors.csv`, and `frequency.csv` (see each file's header for exact
   columns).
2. Add the prose entry under `book/Part03_Lexicon/`.
3. Verify IPA and stress against a dictionary source listed in
   `REFERENCES.md` before marking the entry done — do not transcribe IPA
   from memory.

## Before marking anything "done"

Run the Quality Checklist in `PROJECT.md` §5 / `STYLE_GUIDE.md` §6 against
the content. Update `CHANGELOG.md` with what was added. Update the relevant
`ROADMAP.md` checkbox.
