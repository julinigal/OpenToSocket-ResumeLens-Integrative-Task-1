# AI Usage Log

**Tool:** Claude.ai (web chat), used by Juan Fernando Jaramillo.
**Conversation link:** https://claude.ai/share/63f83247-230f-4308-8682-319a215ee598

## Prompt 1

> "Actua como profesor que sabe de matematicas discretas y de python,
> explicame que se necesita para desarrollar esta integradora y su
> documentación"

**What Claude suggested:** the pipeline order (Regex → Transducers →
ordering → Automata → DSL/textX → HTML), the theory each stage needs, a
suggested repository layout (`docs/`, `src/` with `extraction/`,
`normalization/`, `recognition/`, `dsl/`, `tests/`, `ui/`), a documentation
checklist (literature review, module design, formalization, test cases,
poster, presentation), and the administrative rules (team size, commits,
IAG level 3).

**What we actually used:**
- The 4-stage pipeline order — this is exactly the order our code follows
  (`extraction` → `normalization` → `classification` → `profile_language`,
  chained in `pipeline.py`).
- The documentation checklist — our `docs/design/` folder follows this
  structure directly: `Literature_review.md`, `Module_Design.md`,
  `Regex.md` / `Transductores.md` / `Canonical_order.md` /
  `Automata_Formalization.md` / `Grammar_Formalization.md` (we split
  "formalization" into one file per stage instead of one combined file),
  and `Test_stage_1_2.md` / `Test_Stage_3_4.md`.

**What we changed or did not use:**
- We named the Stage 3 package `classification`, not `recognition`.
- We did not create a `ui/` folder; our only output is the generated HTML
  from Stage 4, produced by a plain script (`examples/run_example.py`),
  not a separate interface.
- Claude flagged that the project statement's presentation section
  mentions "the security problem... in the context of code repositories",
  which looks like a leftover from a different assignment. We did not
  change anything in our project because of this — it is the professor's
  document, not ours to edit — but it confirmed we were reading the
  statement correctly and not missing a security requirement that applies
  to us.

## Prompt 2

> "ayuda a darme un ejemplo de como deberia realizar la documentación"

**What Claude suggested:** example fragments for `formalization.md`
(an email regex and a worked finite-state transducer example, `js` /
`javascript` → `JAVASCRIPT`), an example `test_cases.md` table, an example
`literature_review.md` structure with one worked citation (Mohri, 1997),
and general advice (link each formal definition to its code and test,
regenerate diagrams from the real code, keep this AI log).

**What we actually used:**
- The general shape of the test cases table (ID, scenario, input, expected
  output) — our actual tables in `Test_stage_1_2.md` and
  `Test_Stage_3_4.md` follow this idea, extended with a `Result` column
  and a separate "edge cases" section per stage.
- The advice to keep diagrams generated from the real code, not hand-drawn
  — our diagrams in `docs/img/` are exported from the actual
  `pyformlang` objects, so they cannot drift from the implementation.

**What we changed or did not use:**
- The example transducer used **character-by-character** transitions
  (one input symbol per letter, built as a prefix tree, with a `$`
  end-of-token marker to decide when to emit the output). We did not use
  this design. Our transducers read a **whole token as one input symbol**
  (for example the single symbol `"JavaScript"`, not the letters
  `J-a-v-a-S-c-r-i-p-t`), which gives a much smaller automaton (2 states:
  `q0`, `qf`) and does not need an end marker. We judged the character
  level design to be unnecessarily complex for our fixed, known vocabulary
  of variant strings.
- The suggested `Mohri, M. (1997)` and `Hopcroft, Motwani & Ullman`
  references do not appear in our `Literature_review.md`. We searched for
  and used our own sources instead (Jurafsky & Martin; Zupon, Crew &
  Ritchie, 2021; Guo, Alamudun & Hammond, 2016 — RésuMatcher; Amdouni &
  Karaa, 2010; Musleh, 2024; Chen, Zhang & Niu, 2018; Vukadin et al.,
  2021; Wosiak, 2021), which are more specific to résumé processing than
  the AI's suggestions.

## Prompt 3

> "Listo, ahora dame un ejemplo de como deberia funcionar el codigo, es
> decir como a partir de una hoja de vida se le puede extraer la
> información"

**What Claude produced:** a complete, runnable single-file script
(`resumelens_demo.py`) covering Stages 1-3 (not Stage 4, which it noted
was missing), including worked regex patterns, a prefix-tree transducer,
and a DFA builder that supported optional profile levels with a
skip-ahead transition. It was run against 3 sample candidates and printed
their stage-by-stage results.

**What we actually used:**
- The overall idea of validating the design by running it end-to-end
  against sample résumés before writing it up — our `test_cases.md`
  documents were built the same way, by running the real code against
  `data/resumes/*.txt` and recording the actual output.
- The suggestion to split the single demo script into separate modules
  per stage for the real repository — this is exactly how
  `src/resumelens/` is organized (`extraction/`, `normalization/`,
  `classification/`, `profile_language/`).

**What we changed or did not use (this is the largest gap between the
demo and our real code):**
- The demo's regex used lookarounds (`(?<![\w.])...(?!\w)`) and built the
  alternation dynamically, sorted by word length. Our `patterns.py` uses
  plain `\b` word boundaries and static, hand-ordered alternations
  (longer variants listed before their prefixes, e.g. `React\.js` before
  `React`) — simpler to read and to verify against the formalization
  docs by hand.
- The demo's transducer used the character-level, prefix-tree design
  described in Prompt 2. We used the token-level design instead, for the
  same reason stated there.
- The demo's DFA allowed **optional** profile levels and could skip over
  them. Our automata (`classification/automata.py`) do not have optional
  groups — every group is required, which matches the simpler
  `G1+ G2+ ... Gn+` pattern we document in `Automata_Formalization.md`,
  and avoids the extra "can this level be skipped" logic entirely.
- The demo's example profiles ("Backend Developer", "Data Analyst") are
  not the profiles we chose. Our four profiles are Full Stack Developer,
  Machine Learning Engineer, Data Scientist and Software Architect.
- We did not reuse any code from this script as-is; we rewrote every
  pattern, transducer, and automaton from scratch for our own vocabulary
  and profiles, matching the simpler designs described above.

## Prompt 4

> "Explicame cada parte del codigo, desde lo mas basico hasta lo mas
> avanzado"

**What Claude produced:** a line-by-line walkthrough of the demo script,
explaining regex syntax, the FST's 7 components mapped to code, why the
DFA is deterministic, and a list of the demo's own limitations (closed
vocabulary, heuristic name/education detection, phone numbers matching
date ranges, no experience-level scoring).

**What we actually used:**
- This explanation is what let us understand the **formal structure**
  well enough to redo it in our own, simpler design (token-level
  transducers, required-only automaton groups) instead of copying the
  demo. Without understanding why each part of the 7-tuple and 5-tuple
  existed, we could not have simplified them correctly.
- The idea of documenting limitations honestly, instead of hiding them,
  is reflected in the "LIMITATION" rows of `Test_stage_1_2.md` and
  `Test_Stage_3_4.md` (for example: accented names, email subdomains, and
  — found independently by us, not suggested by the AI — the `C#` pattern
  never matching a real résumé line, which we later fixed in
  `patterns.py`).

## Summary

The AI conversation was used for **conceptual guidance and a first
working example**, not as a source of final code. Every regular
expression, transducer, automaton and grammar rule in `src/resumelens/`
was written for our own vocabulary and profiles, and in several cases
(the transducer design, the automaton design, the regex style) we
deliberately chose a simpler approach than the one the AI suggested,
after understanding why the AI's version worked the way it did.
