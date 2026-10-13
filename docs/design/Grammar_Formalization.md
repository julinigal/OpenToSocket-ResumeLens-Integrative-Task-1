# Grammar Formalization (DSL)

## Purpose

The DSL describes a candidate profile in a small readable language, who the candidate is, how much experience they have, which canonical skills they have and whether each profile accepted or rejected them. The grammar lives in `profile_language/candidate.tx` and is written for textX, a Python library that builds a parser and an object model from a grammar.

## Gramar in EBNF

The same rules as in `candidate.tx`, written in plain EBNF (`?` optional, `*` zero or more, `+` one or more):
 
```
CandidateProfile ::= 'Candidate' Name
                     ( 'Contact' ( 'email' ':' Email )? ( 'phone' ':' Phone )? )?
                     'Experience' INT 'years'
                     'Skills' Skill ( ',' Skill )*
                     'Classification' ProfileResult+
 
ProfileResult    ::= ProfileName '=' Status
 
ProfileName      ::= 'FULL_STACK_DEVELOPER' | 'MACHINE_LEARNING_ENGINEER'
                   | 'DATA_SCIENTIST' | 'SOFTWARE_ARCHITECT'
 
Status           ::= 'ACCEPTED' | 'REJECTED'
 
Name             ::= /[A-Za-z]+( [A-Za-z]+)*/
Email            ::= /[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}/
Phone            ::= /\+?[\d\- ]{7,}/
Skill            ::= /[A-Z][A-Z_]*/
```

## Terminals
 
* Keywords and symbols: `Candidate`, `Contact`, `email`, `phone`, `Experience`, `years`, `Skills`, `Classification`, `:`, `,`, `=`.

* Fixed values (6): the four profile names (`FULL_STACK_DEVELOPER`, `MACHINE_LEARNING_ENGINEER`, `DATA_SCIENTIST`, `SOFTWARE_ARCHITECT`) and the two statuses (`ACCEPTED`, `REJECTED`).

* Pattern terminals (5): `Name`, `Email`, `Phone`, `Skill` and `INT`.


## Non-terminals
 
* `CandidateProfile`: the start symbol, the whole document.

* `ProfileResult`: one line of the classification, `profile = status`.

* `ProfileName`: one of the four profiles.

* `Status`: `ACCEPTED` or `REJECTED`.

## How the DSL is used in the code
 
1. `render_candidate_profile(...)` writes the DSL text from the pipeline data. It uses the first email and the first phone found, and writes `Experience 0 years` if the years are missing.

2. `parse_candidate_profile(text)` parses the text with the grammar. If the text breaks the grammar, it raises `TextXSyntaxError`.

3. `render_html(model)` turns the parsed model into an HTML page (name, experience, contact, skills and classification).