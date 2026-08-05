# Style Guide / 写作规范

This guide is binding for every chapter in `book/`. It operationalizes the
five principles in [PROJECT.md](./PROJECT.md#2-core-philosophy).

## 1. Claim Labeling (Truth First)

Every non-obvious claim must be traceable to one of four categories. Mark
the category inline the first time a claim of that type appears in a
section, using one of these tags:

| Tag | Meaning | Example |
|---|---|---|
| `[Pearson]` | Stated in official Pearson PTE Academic documentation (Score Guide, Test Format, official website) | `[Pearson]` Read Aloud is scored on content, oral fluency, and pronunciation. |
| `[Linguistics]` | Established linguistic/phonetic fact, independent of PTE | `[Linguistics]` English has 24 consonant phonemes in most RP/GA inventories. |
| `[Practice]` | Pattern observed across verified PTE practice material or test-taker reports, not officially documented | `[Practice]` Test-takers report the microphone begins recording ~3 seconds after the beep. |
| `[Hypothesis]` | The author's reasoned inference, explicitly not confirmed by Pearson | `[Hypothesis]` The scoring model likely penalizes long pauses more than short ones, based on fluency sub-score patterns. |

Never present a `[Hypothesis]` or `[Practice]` claim using language that
implies `[Pearson]` certainty ("the AI does X", "PTE requires Y") unless the
tag or surrounding sentence makes the uncertainty explicit.

## 2. Evidence Requirement

Every important claim needs a source. See [REFERENCES.md](./REFERENCES.md)
for the approved source list and citation format. A claim with no traceable
source should be rewritten as a `[Hypothesis]` or removed.

## 3. Prose Rules

- **Simple.** Prefer short sentences. Avoid nested clauses.
- **Professional.** No marketing language ("revolutionary", "secret",
  "guaranteed 90+"). No exclamation points in body text.
- **Evidence-based.** No unsupported "AI bug" or "loophole" claims. If a
  trick is described, explain the mechanism it exploits (or admit the
  mechanism is unknown and label it `[Hypothesis]`).
- **No fake promises.** Never state or imply a guaranteed score outcome.
- **Explain WHY, not just WHAT.** A rule without a mechanism is not
  finished. Bad: "Don't pause too long." Good: "Don't pause too long,
  because the fluency model measures speech-to-silence ratio across the
  whole response `[Pearson]`, and long pauses lower that ratio regardless
  of how correct the words are."

## 4. Tone

Target readers: adult learners, professionals, international students.
Tone: professional, patient, logical, readable. Write to a competent adult,
not down to a beginner and not up to a linguist. Define technical terms
(e.g. "phoneme", "plosive") the first time they are used in a chapter.

## 5. Structural Rules

- Every chapter follows the six-stage template in
  [CONTRIBUTING.md](./CONTRIBUTING.md#chapter-template). Do not skip a
  stage; write "Not applicable to this chapter" if genuinely empty.
- No duplicated explanation across chapters. If a concept is explained
  elsewhere (e.g. "reduction" defined in Part II), link to it — do not
  re-explain it. Exception: a one-sentence reminder is fine; a
  re-derivation is not.
- IPA transcriptions use the International Phonetic Alphabet, General
  American unless a chapter explicitly compares GA vs RP. State which
  accent model is used at the top of any chapter containing IPA.

## 6. Quality Checklist

Before a chapter is marked done, it must pass every item in
[PROJECT.md §5](./PROJECT.md#5-quality-checklist):

- [ ] Grammar
- [ ] IPA verified against a dictionary source (see REFERENCES.md)
- [ ] Stress verified against a dictionary source
- [ ] No duplicated explanation
- [ ] Examples checked (correct, natural, exam-relevant)
- [ ] Suitable for publication (matches this style guide)
