# PTE Pronunciation Bible

> Publication-grade knowledge base for PTE Academic
>
> 中文名称：《PTE 发音圣经》

**Version:** 1.0
**Status:** In Development (scaffold stage)

---

## 1. Project Vision

Create the highest-quality PTE pronunciation and speaking handbook available.

This project is **NOT** intended to be another template book. It aims to become
a complete knowledge base that explains:

- how the PTE AI evaluates speech
- how Chinese learners lose marks
- how pronunciation actually works
- how to train efficiently
- why common "PTE tricks" work (or don't)

The final product should be suitable for:

- Students (65–90+ target score band)
- Teachers
- Course creators
- Publishers

---

## 2. Core Philosophy

This project follows five principles. Every contributor and every chapter
must be checked against them before publication.

### 2.1 Truth First

Never invent rules. Separate:

- Official Pearson information
- Linguistic facts
- Practical experience
- Personal hypotheses

Never mix them together. See [STYLE_GUIDE.md](./STYLE_GUIDE.md) for how each
category must be labeled in text.

### 2.2 Evidence Driven

Every important claim should have evidence. See [REFERENCES.md](./REFERENCES.md)
for the approved evidence sources and citation format.

### 2.3 AI Friendly

Every chapter should be reusable for: PDF, Website, App, Flashcards, Course,
GPT knowledge base — with no duplicated content between formats.

### 2.4 Modular Architecture

Every chapter is independent and follows the same six-stage structure:

```
Learning Objectives
      ↓
   Theory
      ↓
  Examples
      ↓
Exam Strategy
      ↓
 Exercises
      ↓
  Summary
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the chapter template.

### 2.5 Publication Standard

Target quality: Cambridge / Oxford / MIT Press.
**Not:** typical AI-generated ebook.

---

## 3. Book Structure

```
Part I    — Understanding the PTE AI
Part II   — Pronunciation Foundations
Part III  — PTE High Frequency Lexicon
Part IV   — Chinese Error Corpus
Part V    — Question Strategy
Part VI   — Training System
```

Full chapter-level breakdown lives in each part's own `README.md` under
`book/`.

---

## 4. Writing Style & Tone

Simple, professional, evidence-based. No exaggerated marketing language, no
fake promises, no unsupported "AI bug" claims. Every chapter must explain
WHY, not just WHAT. Full detail in [STYLE_GUIDE.md](./STYLE_GUIDE.md).

---

## 5. Quality Checklist

Every chapter must pass before it is considered done:

- [ ] Grammar
- [ ] IPA verified
- [ ] Stress verified
- [ ] No duplicated explanation
- [ ] Examples checked
- [ ] Suitable for publication

---

## 6. Repository Map

```
pte-pronunciation-bible/
├── PROJECT.md            # This file — project charter
├── ROADMAP.md            # Development roadmap
├── STYLE_GUIDE.md         # Writing rules
├── REFERENCES.md          # Approved evidence sources & citation format
├── CHANGELOG.md           # Version history
├── CONTRIBUTING.md        # Chapter / lexicon templates and authoring rules
│
├── book/
│   ├── Part01_AI/                 # Understanding the PTE AI
│   ├── Part02_Pronunciation/      # Pronunciation Foundations
│   ├── Part03_Lexicon/            # PTE High Frequency Lexicon
│   ├── Part04_ErrorCorpus/        # Chinese Error Corpus
│   ├── Part05_Strategy/           # Question Strategy
│   └── Part06_Training/           # Training System
│
├── database/               # Structured data backing the Lexicon & Error Corpus
│   ├── words.csv
│   ├── ipa.csv
│   ├── stress.csv
│   ├── errors.csv
│   └── frequency.csv
│
└── assets/
    ├── images/
    ├── diagrams/
    └── audio/
```

---

## 7. Version Control Plan

| Version | Scope |
|---|---|
| 1.0 | Publication draft (text content complete) |
| 1.1 | More examples |
| 2.0 | Audio, exercises, teacher notes |

---

## 8. Future Expansion

Website · Audio Book · Flashcards · Anki · Mobile App · GPT Knowledge Base ·
Video Course · Teacher Edition

---

## 9. Ultimate Goal

When someone finishes this book, they should understand not only how to
pronounce English better, but also how the PTE exam evaluates spoken
English, and how to train efficiently using first principles, instead of
relying on memorized tricks.
