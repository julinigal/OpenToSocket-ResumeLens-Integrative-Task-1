# Test Case - Stage 3 and 4

Stae 3 is classification with the porfile automata. Stage 4 is the DSL and the HTML visualization. The test are in `tests/test_classification.py` and `tests/test_profile_language.py`.

## Stage 3 - Classification : suite test

| ID | Test (method) | Input | Expected output | Result |
|----|---------------|-------|-----------------|--------|
| 3.01 | `test_full_stack_developer_accepts_required_pattern` | `JAVASCRIPT, REACT, NODE_JS, GIT` | accepted by the full-stack automaton | PASS |
| 3.02 | `test_full_stack_developer_rejects_missing_git` | `JAVASCRIPT, REACT` | rejected (ends in a non-final state) | PASS |
| 3.03 | `test_full_stack_developer_rejects_wrong_order` | `GIT, JAVASCRIPT, REACT` | rejected (wrong order) | PASS |
| 3.04 | `test_full_stack_developer_rejects_missing_language` | `REACT, GIT` | rejected (no language) | PASS |
| 3.05 | `test_juan_jaramillo_accepted_as_full_stack_developer` | `juan_jaramillo.txt`, FULL_STACK_DEVELOPER | `ACCEPTED` | PASS |
| 3.06 | `test_juliana_galvis_accepted_as_machine_learning_engineer` | `juliana_galvis.txt`, MACHINE_LEARNING_ENGINEER | `ACCEPTED` | PASS |
| 3.07 | `test_tony_stark_accepted_as_data_scientist` | `tony_stark.txt`, DATA_SCIENTIST | `ACCEPTED` | PASS |
| 3.08 | `test_andres_aristizabal_accepted_as_software_architect` | `andres_aristizabal.txt`, SOFTWARE_ARCHITECT | `ACCEPTED` | PASS |
| 3.09 | `test_juan_jaramillo_rejected_as_machine_learning_engineer` | `juan_jaramillo.txt`, MACHINE_LEARNING_ENGINEER | `REJECTED` | PASS |
| 3.10 | `test_juliana_galvis_rejected_as_software_architect` | `juliana_galvis.txt`, SOFTWARE_ARCHITECT | `REJECTED` | PASS |
| 3.11 | `test_andres_aristizabal_rejected_as_data_scientist` | `andres_aristizabal.txt`, DATA_SCIENTIST | `REJECTED` | PASS |

## Stage 3 - Classification: results for the four resumes

| Resume | FULL_STACK_DEVELOPER | MACHINE_LEARNING_ENGINEER | DATA_SCIENTIST | SOFTWARE_ARCHITECT |
|--------|----------------------|---------------------------|----------------|--------------------|
| `juan_jaramillo.txt` | ACCEPTED | REJECTED | REJECTED | REJECTED |
| `juliana_galvis.txt` | REJECTED | ACCEPTED | REJECTED | REJECTED |
| `tony_stark.txt` | REJECTED | ACCEPTED | ACCEPTED | REJECTED |
| `andres_aristizabal.txt` | REJECTED | REJECTED | REJECTED | ACCEPTED |

Each resume is accepted for its own profile. Tony Stark is also accepted as machine learning engineer because he has Python, a machine-learning library (`PANDAS`, `SCIKIT_LEARN`) and `GIT`.


## Stage 3 - Classification: edge cases

| ID | Aspect | Input | Observed output | Status |
|----|--------|-------|-----------------|--------|
| 3.12 | Order matters | `REACT, JAVASCRIPT, GIT` (full-stack automaton) | rejected | PASS (by design) |
| 3.13 | Repeated skills | `JAVASCRIPT, JAVASCRIPT, REACT, REACT, NODE_JS, GIT` | accepted (self-loops) | PASS |
| 3.14 | Minimum accepted | `TYPESCRIPT, VUE, GIT` | accepted (one skill per group is enough) | PASS |
| 3.15 | Empty list | `[]` | rejected | PASS |
| 3.16 | Skills outside the alphabet are ignored | `JAVASCRIPT, REACT, SQL, GIT` through `classify_qualifications` | `ACCEPTED` | PASS |
| 3.17 | Missing group (infrastructure) | `JAVA, DESIGN_PATTERNS, GIT`, SOFTWARE_ARCHITECT | `REJECTED` | PASS |
| 3.18 | Minimum for software architect | `JAVA, DESIGN_PATTERNS, DOCKER, GIT` | `ACCEPTED` | PASS |
| 3.19 | Missing group (statistics) | `PYTHON, PANDAS, GIT`, DATA_SCIENTIST | `REJECTED` | PASS |
| 3.20 | Unsorted input through the classifier | `GIT, JAVASCRIPT, REACT`, FULL_STACK_DEVELOPER | `REJECTED` (the classifier does not sort; it trusts the canonical ordering of stage 2) | PASS (documented behavior) |

## Stage 4 - DSL and visualization: suite test

| ID | Test (method) | Input | Expected output | Result |
|----|---------------|-------|-----------------|--------|
| 4.01 | `test_render_and_parse_round_trip` | Juan Jaramillo, 3 years, `JAVASCRIPT, REACT, NODE_JS, GIT`, four results | parsed model with the same name, years, skills and statuses | PASS |
| 4.02 | `test_contact_information_is_included_when_present` | email `juliana@example.com`, phone `+1-555-123-4567` | `model.email` and `model.phone` have those values | PASS |
| 4.03 | `test_rejects_invalid_profile_name` | `NOT_A_REAL_PROFILE = ACCEPTED` | `TextXSyntaxError` | PASS |
| 4.04 | `test_rejects_invalid_status` | `MACHINE_LEARNING_ENGINEER = MAYBE` | `TextXSyntaxError` | PASS |
| 4.05 | `test_juan_jaramillo_full_pipeline_and_html` | `juan_jaramillo.txt` through extraction, normalization, classification, DSL and HTML | HTML contains `Juan Jaramillo`, `FULL_STACK_DEVELOPER: ACCEPTED` and `<li>GIT</li>` | PASS |

##  Stage 4 - DSL and visualization: edge cases

| ID | Aspect | Input | Observed output | Status |
|----|--------|-------|-----------------|--------|
| 4.06 | Missing years | `experience_years = None` | written as `Experience 0 years`, parsed with `years = 0` | PASS |
| 4.07 | Missing name | `name = None` | text becomes `Candidate None`, parsed with name `"None"` | LIMITATION |
| 4.08 | No skills | `qualifications = []` | `TextXSyntaxError` | LIMITATION |
| 4.09 | No classification results | `classification_results = {}` | `TextXSyntaxError` (at least one result is required) | PASS (by design) |
| 4.10 | Accented name | `María` | `TextXSyntaxError` | LIMITATION |
| 4.11 | Skill with a digit or in lowercase | `PYTHON3`, `python` | `TextXSyntaxError` | LIMITATION |
| 4.12 | Only a phone, no email | phone `+57 300 123 4567` | parsed, `model.phone` set | PASS |
| 4.13 | Email with subdomain | `a@mail.example.com` | parsed correctly (the grammar accepts it) | PASS |
| 4.14 | Full pipeline on the four resumes | `run_pipeline` for each resume with its profile | the four rows of the results table above | PASS |
| 4.15 | Pipeline with a resume that has no recognized skills | `Ana Perez` + `1 year of experience.` | `TextXSyntaxError` | LIMITATION |

