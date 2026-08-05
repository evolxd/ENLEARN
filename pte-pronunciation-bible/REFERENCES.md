# References / 参考资料

This file lists the approved evidence sources for claims tagged in
[STYLE_GUIDE.md §1](./STYLE_GUIDE.md#1-claim-labeling-truth-first), and the
citation format used throughout `book/`.

## Approved Source Categories

### `[Pearson]` — Official Pearson documentation

- PTE Academic Score Guide (official, Pearson)
- PTE Academic Test Format / Item type descriptions (official, Pearson)
- Pearson official website and score reporting documentation
- Official Pearson practice materials (Scored Practice Tests, Official Guide)

### `[Linguistics]` — Linguistic and phonetic facts

- IPA Chart, International Phonetic Association
- Cambridge Dictionary (pronunciation, IPA, definitions)
- Oxford Dictionary / Oxford Learner's Dictionaries (pronunciation, IPA, definitions)
- Academic Word List (Averil Coxhead, 2000)
- Peer-reviewed phonetics/phonology and second-language acquisition literature

### `[Practice]` — Verified practical evidence

- Patterns cross-confirmed across multiple independent, verified PTE
  practice questions or test-taker score reports
- Must be reproducible/observable, not a single anecdote

### `[Hypothesis]` — Author inference

- No external source. Must be explicitly labeled as inference in text,
  per STYLE_GUIDE.md §1.

## Citation Format

Inline citation, placed at the end of the sentence it supports:

```
[Pearson] Read Aloud scores oral fluency, pronunciation, and content. (PTE Academic Score Guide)
[Linguistics] /θ/ and /ð/ are dental fricatives absent from Mandarin's phoneme inventory. (IPA Chart; Cambridge Dictionary)
```

Full source list per chapter goes in a `## References` section at the end
of the chapter file, using this format:

```
## References

1. Pearson. *PTE Academic Score Guide.*
2. Cambridge Dictionary. Entry: "schedule". https://dictionary.cambridge.org/
3. Coxhead, A. (2000). *A New Academic Word List.* TESOL Quarterly.
```

## Source Log

Maintainers: as sources are actually consulted while writing chapters, log
them here with the date added, so the reference list stays auditable across
the whole book instead of just per-chapter.

| Date | Source | Used In |
|---|---|---|
| 2026-08-05 | Pearson, *PTE Academic Test Taker Score Guide* (July 2025) — 403 on direct fetch this session; content verified via secondary sources below | Part I, Ch.1–4 |
| 2026-08-05 | Pearson PTE, "How does PTE Academic mark different accents?" — 403 on direct fetch this session; content verified via secondary sources below | Part I, Ch.2 |
| 2026-08-05 | Gurully, "Guide for Oral Fluency of PTE Speaking Section to Score High" | Part I, Ch.1, Ch.3 |
| 2026-08-05 | PTE Exam Preparation, "PTE Speaking Scoring Criteria – Importance of Pronunciation and Fluency" | Part I, Ch.1 |
| 2026-08-05 | PTE Exam Preparation, "Oral Fluency Assessment in PTE Exam – Marking Scheme or Weightage of Marks" | Part I, Ch.3 |
| 2026-08-05 | Gradding, "Read Aloud PTE: Practice Sample Questions with Expert Tips" | Part I, Ch.1, Ch.4 |
| 2026-08-05 | Leap Scholar, "PTE Read Aloud: Tips, Examples & Free Practice Samples" | Part I, Ch.4 |
| 2026-08-05 | onePTE, "New format PTE Academic tests" (Aug 2025 item-type update) | Part I, Ch.1 |
| 2026-08-05 | PTE Smart, "Accent x PTE Academic – does my accent influence my score?" | Part I, Ch.2 |
| 2026-08-05 | Sumlingo, "How PTE Academic Evaluates Different English Accents" | Part I, Ch.2 |
| 2026-08-05 | Top Pro English, "Is Your Speaking Accent Really Stopping You from Scoring, or Is It Something Else?" | Part I, Ch.2 |

| 2026-08-05 | International Phonetic Association, *IPA Chart* | Part II, Ch.1, 2, 9 |
| 2026-08-05 | Cambridge Dictionary (IPA transcriptions, GA vs RP) | Part II, Ch.1, 2, 3, 4, 6, 8 |
| 2026-08-05 | Oxford Learner's Dictionaries | Part II, Ch.1, 3, 4 |
| 2026-08-05 | General phonetics literature (stress-timing, coarticulation/assimilation/elision, weak forms, unreleased stops, Mandarin phonology) — placeholder, specific academic citations not yet added | Part II, Ch.2, 5, 6, 7, 8, 9 |

**Outstanding verification task:** the two primary Pearson sources above
returned HTTP 403 when fetched directly in this session (see
`book/Part01_AI/README.md`). Every `[Pearson]`-tagged claim in Part I was
cross-checked against 2+ independent secondary sources that quote the
primary documents, but has not been confirmed against the primary PDF/
article text directly. Re-verify before marking any Part I chapter Done.
