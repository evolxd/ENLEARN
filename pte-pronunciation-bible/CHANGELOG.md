# Changelog / 更新日志

All notable changes to the PTE Pronunciation Bible are logged here, newest
first. This tracks the book's content history; see `ROADMAP.md` for planned
work and `PROJECT.md` §7 for release-version scope.

## [Unreleased]

### Fixed (Part VI)

- Re-checked all four Part VI training plans' Part III lexicon batch
  references now that the lexicon is final (500 words, 12 batches, as
  of the previous commit). The plans were originally written assuming
  the lexicon might grow to as many as 16 batches, so several
  contained stale placeholders: the 30-Day Plan's "remaining 200
  words (Batches 9–16)" is now correctly "Batches 9–12"; the 60-Day
  and 90-Day Plans' "sixteen batches (Batches 1–16)" and vague
  "remaining lexicon batches through the current end of Part III"
  phrasing now name Batch 12 (`words_481-500.md`) explicitly and move
  it into the week where it actually fits given the real 12-batch
  total. Updated `ROADMAP.md` Stage 6 and `Part06_Training/README.md`
  to record this as resolved.

### Resolved (Part V)

- Ch.7 Write Email's module-scope caution is resolved: confirmed via
  WebSearch cross-reference against multiple independent sources
  (direct Cambridge/Pearson fetch still 403) that Write Email is a
  **PTE Core–only** item type, not part of PTE Academic. PTE Academic's
  writing task is Write Essay (Ch.8), unchanged by this finding. Ch.7
  is retitled and reframed as supplementary material for readers also
  preparing for PTE Core, rather than core PTE Academic curriculum —
  kept, not removed, since Pearson runs both tests and some readers
  may need it. Updated the chapter itself, `Part05_Strategy/README.md`,
  and `ROADMAP.md` Stage 4 accordingly; added corroborating sources to
  the chapter's own References section.

### Verified (Part III)

- Spot-check verification pass (2026-08-06) against the ~19
  highest-risk lexicon words/pairs flagged across all 12 batches'
  Source Log entries (stress-variable words, French loanwords,
  heteronyms, noun/verb and adjective/noun stress-shift pairs). Direct
  WebFetch to Cambridge Dictionary and Oxford Learner's Dictionaries
  still returned HTTP 403; WebSearch cross-reference against the same
  sources' aggregated snippets was used instead. 17 of 19 confirmed
  correct as documented; 1 correction made — *employee*'s
  `database/ipa.csv` and `database/stress.csv` rows now note the
  second attested stress variant (syllable 2) that the markdown entry
  already carried but the CSVs omitted; 2 items (*rehabilitation*'s
  precise stress detail, the general velar-nasal `[Hypothesis]` claim)
  remain unresolved. Full detail and per-word results in
  `REFERENCES.md`. This is a targeted spot check of the highest-risk
  fraction of the lexicon, not an exhaustive pass — the remaining
  ~480 entries are still flagged "cross-check pending."

### Added (Part VI)

- Part VI — Training System: all four chapters drafted
  (`book/Part06_Training/01_15-day-plan.md` through
  `04_90-day-plan.md`), completing Stage 6. Each plan sequences Part II
  (mechanism) and Part IV (matching Chinese-learner error) before
  Part V (item-type strategy), scaled by length: the 15-Day Plan
  triages to the highest-frequency errors and the first ~150–210
  lexicon words; the 30-Day Plan covers Part II/IV/V fully and reaches
  the lexicon's original 300-word floor; the 60-Day Plan adds a second
  Part II/IV review pass, the full lexicon as it currently stands, and
  three mock-test checkpoints; the 90-Day Plan adds a third,
  data-driven review cycle and five mock-test checkpoints with
  cross-checkpoint error comparison. All `[Hypothesis]`-tagged
  pedagogical claims (spaced repetition, review-day placement, taper
  weeks) are flagged as the author's general learning-science
  reasoning, not Pearson-sourced. Updated `ROADMAP.md` Stage 6 and
  `book/Part06_Training/README.md` to reflect completion.

### Added (Part III)

- Part III — PTE High Frequency Lexicon: Batch 12 drafted, the final 20
  words (`book/Part03_Lexicon/words_481-500.md`, words 481–500) —
  **the lexicon reaches its 500-word ceiling and is now complete**.
  Matching rows appended to all five `database/*.csv` files
  (re-verified as well-formed CSV, exactly 500 word rows total, no
  duplicates). Emotions/personality traits theme (anxious, anxiety,
  confident, confidence, enthusiastic, enthusiasm, curious, curiosity,
  ambitious, ambition, humble, humility, optimistic, optimism,
  resilient, resilience, empathy, empathetic, gratitude, grateful),
  deliberately organized as adjective/noun pairs to close out several
  cross-batch threads at once: a new stress-shift mechanism
  (adjective-to-noun via "-ety"/"-ity": anxious/anxiety,
  humble/humility, curious/curiosity — the latter also the seventh
  "-ity" data point); the fifth, sixth, and seventh "-ic" family shift
  pairs (enthusiasm/enthusiastic, optimism/optimistic,
  empathy/empathetic), bringing that thread to seven total pairs; the
  eighth and final "-ity" data point (humility); three stress-stable
  "-ent"/"-ence" and related pairs (confident/confidence,
  ambitious/ambition, resilient/resilience) as a negative-data-point
  set alongside "-ship"; and the sixth/seventh velar-nasal /ŋ/
  examples (anxious, anxiety), closing that thread at seven data
  points.
- Part III — PTE High Frequency Lexicon: Batch 11 drafted, 60 more words
  (`book/Part03_Lexicon/words_421-450.md` + `words_451-480.md`, words
  421–480) — **480 of the 300–500 target complete, only 20 words
  remain**. Matching rows appended to all five `database/*.csv` files
  (re-verified as well-formed CSV, 480 word rows total, no
  duplicates). Air travel/transportation theme (airport, passenger,
  luggage, departure, arrival, boarding, terminal, customs,
  immigration, passport, transit, delay, route, traffic, congestion)
  plus weather/natural disasters (weather, forecast, humidity,
  precipitation, drought, flood, hurricane, thunderstorm, wind,
  rainfall, storm, disaster, earthquake, wildfire, tornado) plus
  careers/workplace (interview, resume, application, promotion,
  recruit, recruitment, onboarding, teamwork, freelance, remote,
  overtime, appraisal, feedback, mentor, internship) plus
  computing/internet technology (password, username, upload, download,
  browser, website, encryption, cybersecurity, malware, firewall,
  cloud, streaming, subscription, app, notification). Adds a second
  explicit medial /ð/ example (weather); sixteen more
  compound-noun-stress examples, the largest single-batch addition to
  that thread; the third through fifth velar-nasal /ŋ/ examples
  (boarding, onboarding, streaming); a new heteronym-caution pattern
  (resume, covering two unrelated words sharing one spelling, with the
  CV sense also being a fourth French-origin final-stress loanword); a
  third confirmation that "-ship" is stress-neutral (internship); a
  sixth "-ity" data point in two words in one batch (humidity,
  cybersecurity — the latter also this lexicon's longest compound
  word); and a GA-vs-variant pronunciation caution (route).
- Part III — PTE High Frequency Lexicon: Batch 10 drafted, 60 more words
  (`book/Part03_Lexicon/words_361-390.md` + `words_391-420.md`, words
  361–420) — **420 of the 300–500 target complete, 80 words remain**.
  Matching rows appended to all five `database/*.csv` files (re-verified
  as well-formed CSV, 420 word rows total, no duplicates). Scientific
  research methodology theme (experiment, laboratory, observe,
  observation, survey, questionnaire, verify, verification, empirical,
  quantitative, qualitative, statistics, discover, discovery, invention,
  breakthrough, simulate, simulation, calculate, calculation,
  measurement, measure, assess, assessment) plus family/relationships
  (household, family, relative, sibling, parent, spouse, marriage,
  divorce, childhood, elderly, guardian, upbringing, ancestor,
  descendant) plus health/medical care (diet, appetite, allergy,
  therapy, therapist, hospital, clinic, patient, physician, surgeon,
  prescription, medication, recovery, rehabilitation, wellness,
  hygiene). Adds four more "-tion" shift-from-base-word pairs
  (observe/observation, verify/verification, simulate/simulation,
  calculate/calculation); a new noun/verb stress-shift pair
  (survey); a second and third /ʒ/ example (measurement, measure); a
  third French-origin final-stress loanword (questionnaire); a new
  pattern flagging velar nasal /ŋ/ reduced to /n/ (sibling, upbringing);
  a first "-cian" example showing the "-tion" rule extends to that
  suffix spelling (physician); a fourth reduction-thread example
  (family, plus laboratory as a fifth in the same batch); the longest
  "-tion" word in the lexicon so far at six syllables (rehabilitation);
  and a second "-ical" family example (empirical).
- Part III — PTE High Frequency Lexicon: Batch 9 drafted, 60 more words
  (`book/Part03_Lexicon/words_301-330.md` + `words_331-360.md`, words
  301–360) — **first batch past the 300-word floor**, continuing toward
  the 500-word ceiling per user direction ("继续下一个60个"). Matching
  rows appended to all five `database/*.csv` files (re-verified as
  well-formed CSV, 360 word rows total). Law/justice theme (law, legal,
  illegal, legislation, justice, judge, court, crime, criminal, penalty,
  regulation, authority) plus politics/civics (election, candidate,
  campaign, democracy, citizen, constitution, parliament, senate,
  diplomat) plus arts/literature (literature, novel, poetry, author,
  narrative, fiction, character, theater, performance, exhibition,
  gallery, sculpture, architecture, architect) plus sports (athlete,
  athletic, championship, tournament, stadium, spectator) plus
  travel/leisure (leisure, hobby, recreation, tourism, tourist,
  destination, accommodation, itinerary, souvenir). Adds a third "-tion"
  shift-from-base-verb pair (regulate→regulation), a second and third
  "-ic" family shift pair (democracy/democratic, diplomat/diplomatic),
  and a fourth (athlete/athletic); confirms "-ship" as stress-neutral —
  the first negative data point in the suffix-stress family
  (citizen/citizenship, championship); introduces this lexicon's first
  /ʒ/ example (leisure, flagged with extra `[Hypothesis]` caution since
  the substitution pattern isn't directly documented in Part IV); adds a
  sixth and seventh spelling-mismatch example (character,
  architecture/architect — Greek-origin "ch" = /k/); and a second
  French-origin final-stress loanword (souvenir, alongside
  entrepreneur).
- Part III — PTE High Frequency Lexicon: Batch 8 drafted, 60 more words
  (`book/Part03_Lexicon/words_241-270.md` + `words_271-300.md`, words
  241–300) — **reaches 300 words, the original minimum target for this
  Part.** Matching rows appended to all five `database/*.csv` files
  (re-verified as well-formed CSV, 300 word rows total). Business/finance
  theme (budget, investment, market, competition, currency, inflation,
  entrepreneur) plus geography/media/technology (region, urban, rural,
  journalism, broadcast, platform, network, software, hardware, database,
  bandwidth). Introduces compound noun stress as a new pattern (stress on
  the first element: NETwork, SOFTware, HARDware, DATAbase, BANDwidth,
  share/stakeholder) — distinct from every suffix-stress rule tracked so
  far since it applies to compounding, not suffixation. Adds a third
  "-ial" shift example (industry→industrial), a fifth "-ity" example
  (connectivity), a second "-tion" shift-from-base-verb pair
  (publish→publication, repeating organize→organization), a third/fourth
  GA-vs-variant stress caution (finance/financial, advertisement), and
  this lexicon's first word-final-position /θ/ example (bandwidth,
  completing a three-position set with word-initial and medial cases).
  **Next step: confirm with the user whether to stop the lexicon at 300
  words or continue toward the 500-word ceiling before starting Batch 9.**
- Part III — PTE High Frequency Lexicon: Batch 7 drafted, 60 words this
  time (`book/Part03_Lexicon/words_181-210.md` +
  `words_211-240.md`, words 181–240) — **batch size increased from 30 to
  60 per user direction**, effective this batch onward (recorded in
  `book/Part03_Lexicon/README.md`). Matching rows appended to all five
  `database/*.csv` files (re-verified as well-formed CSV, 240 word rows
  total). Widest topical spread yet: science/technology/environment
  (climate, sustainability, artificial intelligence, algorithm) plus
  health/psychology (medicine, diagnosis, psychology, behavior, emotion)
  plus history/culture (history, civilization, tradition, religion).
  Establishes "-ity" as a third confirmed suffix-stress rule alongside
  "-tion"/"-ic" (*sustainability*, *biodiversity*), confirms "-ical"
  extends the existing "-ic" rule rather than being a new one
  (*history*→*historical* shifts, contrasted with *culture*/*cultural*
  which doesn't), adds a medial-position /ð/ example (*algorithm*, vs.
  prior word-initial-only cases), a third and fourth silent-letter example
  (*psychology*, continuing *process*/*knowledge*/*vehicle*), and a new
  near-minimal pair (*quantity*/*quality*).
- Part III — PTE High Frequency Lexicon: Batch 6 drafted, 30 more words
  (`book/Part03_Lexicon/words_151-180.md`, words 151–180), same format and
  sourcing caveats as prior batches, with matching rows appended to all
  five `database/*.csv` files (re-verified as well-formed CSV, 180 word
  rows total). Organized around an academic/workplace theme. Establishes
  a second confirmed suffix-stress rule — "-ee"/"-eer" (stress lands *on*
  the suffix, unlike "-tion"/"-ic" which pull stress to the syllable
  *before* it) — with *employee* directly contrasted against
  *employ*/*employer*/*employment*, and *career*/*volunteer* confirming
  the pattern for "-eer." Adds a fourth data point for the adjective/verb
  suffix-vowel alternation (*graduate*) and two more stress-stable
  non-shift pairs (*management*/*manage*, *participate*/*participant*).
- Part III — PTE High Frequency Lexicon: Batch 5 drafted, 30 more words
  (`book/Part03_Lexicon/words_121-150.md`, words 121–150) — the lexicon's
  halfway point toward the 300-word floor. Same format and sourcing
  caveats as prior batches, with matching rows appended to all five
  `database/*.csv` files (re-verified as well-formed CSV, 150 word rows
  total). Organized around an Essay discourse-connector theme, the
  counterpart to Batch 4's Describe Image cluster. Adds three more
  stress-stability non-shift checks (*argue*/*argument*,
  *consequence*/*consequently*, *improve*/*improvement*) and a
  prefix-stability check (*encourage*/*discourage*), introduces the
  lexicon's first /ɔɪ/ diphthong example (*avoid*), and flags *address*
  as a stress-variability caution rather than a confirmed stress pair —
  explicitly distinguished from *increase/decrease*, *impact*, *contrast*.
- Part III — PTE High Frequency Lexicon: Batch 4 drafted, 30 more words
  (`book/Part03_Lexicon/words_091-120.md`, words 91–120), same format and
  sourcing caveats as prior batches, with matching rows appended to all
  five `database/*.csv` files (re-verified as well-formed CSV, 120 word
  rows total). Organized around a Describe Image data-description theme
  (trend and comparison vocabulary) — the first batch built around a
  single item type's vocabulary rather than general academic frequency.
  Introduces a new pattern (adjective/verb suffix-vowel alternation:
  *appropriate*, *approximate*), a confirmed stress-shift pair (*contrast*)
  alongside a flagged non-example (*decline*, same stress in both forms),
  and a new cautiously-tagged z→s devoicing extension (*reasonable*,
  *represent*).
- Part III — PTE High Frequency Lexicon: Batch 3 drafted, 30 more words
  (`book/Part03_Lexicon/words_061-090.md`, words 61–90), same format and
  sourcing caveats as prior batches, with matching rows appended to all
  five `database/*.csv` files (re-verified as well-formed CSV, 90 word
  rows total). Introduces the "-tion"/"-ic" suffix-stress rule as a
  cross-cutting batch note (Part II Ch.4), including a stress-shift pair
  (*economy*/*economic*) that directly mirrors Part II Ch.4's *photograph*
  family example, and separates word-final single-consonant
  deletion/epenthesis (Part IV Ch.1 Mistake 3) from cluster simplification
  (Mistake 4) as a distinct tracked pattern going forward.
- Part III — PTE High Frequency Lexicon: Batch 2 drafted, 30 more words
  (`book/Part03_Lexicon/words_031-060.md`, words 31–60), same format and
  sourcing caveats as Batch 1, with matching rows appended to all five
  `database/*.csv` files (re-verified as well-formed CSV, 60 word rows
  total). Batch 2 continues two cross-batch threads: a coda-position /v/
  pattern (extending Batch 1's *comprehensive* to *perspective* and
  *achieve*) and noun/verb stress pairs beyond Part II Ch.4's
  *record*/*present* (*increase*/*decrease*, *impact*).
- Part III — PTE High Frequency Lexicon: Batch 1 drafted, 30 words
  (`book/Part03_Lexicon/words_001-030.md`), each with a full 16-field
  lexicon entry, plus matching rows added to all five `database/*.csv`
  files (`words.csv`, `ipa.csv`, `stress.csv`, `errors.csv`,
  `frequency.csv`) — verified to parse as well-formed CSV. Batch size set
  to 30 words (adjusted down from the originally planned 50) for
  practical single-pass authoring; recorded in
  `book/Part03_Lexicon/README.md`. IPA/stress data is standard dictionary
  knowledge pending individual Cambridge/Oxford cross-check (direct fetch
  returned 403 this session); "AI Recognition Notes" and PTE-frequency
  ratings are explicitly tagged as author judgment/`Hypothesis`, not
  verified frequency-list or ASR-behavior data.

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
