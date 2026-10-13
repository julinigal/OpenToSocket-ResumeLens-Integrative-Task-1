## Test Case - Stage 1 and 2
 
Stage 1 is extraction (regular expressions). Stage 2 is normalization (transducers) and canonical ordering. Reference inputs are in `data/resumes/*.txt` and the existing tests are in `tests/test_extraction.py` and `tests/test_normalization.py`.
 
Last run: `python -m unittest tests.test_extraction tests.test_normalization` gave 11 tests, all OK. The edge cases below were run by hand against the current code and are not yet in the test suite.
 
### Reference resumes
 
| File | Content (abridged) | Target profile |
|------|--------------------|----------------|
| `juan_jaramillo.txt` | `Juan Jaramillo` · `3 years of experience developing web applications.` · `JS, React.js, NodeJS, Postgres, Git.` | FULL_STACK_DEVELOPER |
| `juliana_galvis.txt` | `Juliana Galvis` · `2 years of experience developing predictive models…` · `Python, Pandas, NumPy, Scikit-learn, TensorFlow, SQL, Git.` | MACHINE_LEARNING_ENGINEER |
| `tony_stark.txt` | `Tony Stark` · `4 years of experience performing statistical analysis…` · `Python, Pandas, Matplotlib, Seaborn, Scikit-learn, Statistics and Probability, SQL, Git.` | DATA_SCIENTIST |
| `andres_aristizabal.txt` | `Andres Aristizabal` · `5 years of experience designing distributed systems.` · `Java, Software Design Patterns, Microservices, Docker, Kubernetes, AWS, REST API, Git.` | SOFTWARE_ARCHITECT |
 
### Stage 1 — Extraction: suite tests
 
| ID | Test (method) | Input | Expected output | Result |
|----|---------------|-------|-----------------|--------|
| 1.01 | `test_full_stack_developer_resume` | `juan_jaramillo.txt` | name `Juan Jaramillo`; years `3`; languages `["JS"]`; frameworks `["React.js","NodeJS"]`; databases `["Postgres"]`; tools `["Git"]` | PASS |
| 1.02 | `test_machine_learning_engineer_resume` | `juliana_galvis.txt` | name `Juliana Galvis` (file has a blank line after the name); years `2`; languages `["Python"]`; frameworks `["Pandas","NumPy","Scikit-learn","TensorFlow"]`; databases `["SQL"]`; tools `["Git"]` | PASS |
| 1.03 | `test_data_scientist_resume` | `tony_stark.txt` | name `Tony Stark`; years `4`; languages `["Python"]`; frameworks `["Pandas","Matplotlib","Seaborn","Scikit-learn"]`; databases `["SQL"]`; tools `["Git"]`; other `["Statistics and Probability"]` | PASS |
| 1.04 | `test_software_architect_resume` | `andres_aristizabal.txt` | name `Andres Aristizabal`; years `5`; languages `["Java"]`; frameworks `[]`; databases `[]`; tools `["Docker","Kubernetes","AWS","REST API","Git"]`; other `["Software Design Patterns","Microservices"]` | PASS |
 
### Stage 1 — Extraction: edge cases (run manually)
 
| ID | Pattern | Input | Observed output | Status |
|----|---------|-------|-----------------|--------|
| 1.05 | R2 email | `ana@mail.com` | `["ana@mail.com"]` | PASS |
| 1.06 | R3 phones | `+57 300 123 4567, 301-555-0199` | `["+57 300 123 4567", "301-555-0199"]` | PASS |
| 1.07 | R5/R7 boundaries | `Skills: C#, Java, JavaScript, SQL, NoSQL.` | languages `["Java","JavaScript"]`; databases `["SQL","NoSQL"]` (`Java` is not matched inside `JavaScript`, `SQL` not inside `NoSQL`) | PASS |
| 1.08 | R6 variants | `Tensor Flow, Py Torch, sklearn, scikit learn, Spring Boot` | all five returned as written | PASS |
| 1.09 | R9 | `Probability, Statistics` | `["Probability","Statistics"]` | PASS |
| 1.10 | R10 | `Bachelor of Science in Systems Engineering. Ingeniería de Sistemas, Universidad Icesi.` + `Master in Data Science` | three strings, each cut at the period/newline | PASS |
| 1.11 | R4 first match | `10 Years of Experience` then `5 years of experience` | `5` (capitalized form ignored, first lowercase match used) | PASS (case-sensitive by design) |
| 1.12 | Empty input | `""` | name `None`, years `None`, all lists empty | PASS |
| 1.13 | R2 sub-domain | `ana.perez+cv@mail.example.com` | `ana.perez+cv@mail.example` | LIMITATION L2 |
| 1.14 | R5 `C#` | `Skills: C#, Java` | languages `["Java"]` (`C#` lost) | LIMITATION L1 |
| 1.15 | R1 accents | `María Pérez` | name `Mar` | LIMITATION L3 |
| 1.16 | R5 false positive | `Worked on R&D with R and Python.` | languages `["R","R","Python"]` | LIMITATION L4 |
 
### Stage 2 — Normalization and canonical ordering
 
#### Suite tests
 
| ID | Test (method) | Input | Expected output | Result |
|----|---------------|-------|-----------------|--------|
| 2.01 | `test_programming_language_variants` | `JS`, `Javascript` through T_lang | `JAVASCRIPT` for both | PASS |
| 2.02 | `test_framework_variants` | `React.js`, `ReactJS`, `NodeJS`, `Node.js` through T_fw | `REACT`, `REACT`, `NODE_JS`, `NODE_JS` | PASS |
| 2.03 | `test_database_variants` | `Postgres`, `PostgreSQL` through T_db | `POSTGRESQL` for both | PASS |
| 2.04 | `test_unknown_token_is_rejected` | `COBOL` through T_lang | `None` (the transducer has no transition) | PASS |
| 2.05 | `test_full_stack_developer_matches_project_statement_example` | `juan_jaramillo.txt`, profile FULL_STACK_DEVELOPER | `["JAVASCRIPT","REACT","NODE_JS","POSTGRESQL","GIT"]` | PASS |
| 2.06 | `test_machine_learning_engineer` | `juliana_galvis.txt`, profile MACHINE_LEARNING_ENGINEER | `["PYTHON","PANDAS","NUMPY","SCIKIT_LEARN","TENSORFLOW","SQL","GIT"]` | PASS |
| 2.07 | `test_software_architect_reorders_other_qualifications` | `andres_aristizabal.txt`, profile SOFTWARE_ARCHITECT | `["JAVA","DESIGN_PATTERNS","MICROSERVICES","DOCKER","KUBERNETES","AWS","REST_API","GIT"]` (the "other" labels move before the tools) | PASS |
 
#### Additional cases (run manually)
 
| ID | Aspect | Input | Observed output | Status |
|----|--------|-------|-----------------|--------|
| 2.08 | Data scientist ordering | `tony_stark.txt`, DATA_SCIENTIST | `["PYTHON","PANDAS","SCIKIT_LEARN","MATPLOTLIB","SEABORN","STATISTICS","SQL","GIT"]` | PASS |
| 2.09 | Merge many-to-one | `Probability` through T_other | `STATISTICS` | PASS |
| 2.10 | Spacing variant | `Tensor Flow` through T_fw | `TENSORFLOW` | PASS |
| 2.11 | Case sensitivity of FST | `js` (lower case) through T_lang | `None` (not in Σ) | PASS (by design) |
| 2.12 | Duplicates kept | `React, ReactJS, React.js, Node, Node.js`, FULL_STACK_DEVELOPER | `["REACT","REACT","REACT","NODE_JS","NODE_JS"]` | PASS (documented behavior; no de-duplication) |
| 2.13 | Same resume, different profile | `Python, JS, R, Pandas, Tensor Flow, SQL, Docker, Git, REST APIs, Statistics` | FSD: `JAVASCRIPT, SQL, REST_API, GIT, PYTHON, R, PANDAS, TENSORFLOW, DOCKER, STATISTICS`; MLE: `PYTHON, PANDAS, TENSORFLOW, SQL, GIT, JAVASCRIPT, R, DOCKER, REST_API, STATISTICS`; DS: `PYTHON, R, PANDAS, STATISTICS, SQL, GIT, JAVASCRIPT, TENSORFLOW, DOCKER, REST_API`; SA: `PYTHON, DOCKER, REST_API, SQL, GIT, JAVASCRIPT, R, PANDAS, TENSORFLOW, STATISTICS` | PASS |
| 2.14 | Labels outside the profile go last (stable) | Case 2.13 under DATA_SCIENTIST | `JAVASCRIPT, TENSORFLOW, DOCKER, REST_API` appear last in normalization order | PASS |