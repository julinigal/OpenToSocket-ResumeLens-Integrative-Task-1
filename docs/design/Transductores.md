## Trasudcer Formalization (Normalization)

# Objective

Stage 1 returns surface forms (Js, Javascript, React.js, .....), stage 2 maps every surface form to a single canical label (JAVASCRIPT, REACT, ....) so that later stages (automata, grammar) can work over a closed vocabulary. The mapping is implemented with five transducers built with `pyformlang.fst.FST`, one per extracted category.

## Formal definition (7-tuple)

Each transducer is

* T = (Q, Σ, Γ, δ, σ, q₀, F)
 
* Q = {q0, qf} - finite set of states.

* Σ : Is the input alphabet. Every whole token (e.g. `Tensor Flow`) is one input symbol, not a sequence of characters.

* Γ : The output alphabet, the canonical labels.

* δ : Q × Σ → Q - Transition function: `δ(q0, s) = qf` for every `s ∈ Σ`, undefined everywhere else (in particular, `qf` has no outgoing transitions).

* σ : Q x Σ → Γ - Output function: `σ(q0, s) = canonical(s)`.

* $q_0$ = q0 - Initial state.
* F = qf - Final states.

## Properties

* Deterministic and single-valued: Each input symbol has exactly one output.

* Rejection: If a token is not in Σ, translate return no output and `normalize_token` return None.

* Many-to-one: Several surface forms share an output.

## Transition tables

# T_lang - programming

| Output (Γ) | Accepted inputs (Σ) |
|------------|---------------------|
| `JAVASCRIPT` | `JavaScript`, `Javascript`, `JS` |
| `TYPESCRIPT` | `TypeScript` |
| `PYTHON` | `Python` |
| `JAVA` | `Java` |
| `CSHARP` | `C#` |
| `R` | `R` |

# T_fw  framworks and libraries

| Output (Γ) | Accepted inputs (Σ) |
|------------|---------------------|
| `REACT` | `React.js`, `ReactJS`, `React` |
| `ANGULAR` | `Angular` |
| `VUE` | `Vue` |
| `NODE_JS` | `Node.js`, `NodeJS`, `Node` |
| `DJANGO` | `Django` |
| `SPRING_BOOT` | `Spring Boot` |
| `SCIKIT_LEARN` | `Scikit-learn`, `scikit learn`, `sklearn` |
| `TENSORFLOW` | `Tensor Flow`, `TensorFlow` |
| `PYTORCH` | `Py Torch`, `PyTorch` |
| `PANDAS` | `Pandas`, `pandas` |
| `NUMPY` | `NumPy` |
| `MATPLOTLIB` | `Matplotlib` |
| `SEABORN` | `Seaborn` |

# T_db - databases

| Output (Γ) | Accepted inputs (Σ) |
|------------|---------------------|
| `POSTGRESQL` | `PostgreSQL`, `Postgres` |
| `NOSQL` | `NoSQL` |
| `SQL` | `SQL` |

# T_tool - tools

| Output (Γ) | Accepted inputs (Σ) |
|------------|---------------------|
| `REST_API` | `REST APIs`, `REST API` |
| `GRAPHQL` | `GraphQL` |
| `GIT` | `Git` |
| `DOCKER` | `Docker` |
| `KUBERNETES` | `Kubernetes` |
| `AWS` | `AWS` |
| `AZURE` | `Azure` |
| `GCP` | `GCP` |

# T_other - other qualifications

| Output (Γ) | Accepted inputs (Σ) |
|------------|---------------------|
| `DESIGN_PATTERNS` | `Software Design Patterns`, `Design Patterns` |
| `MICROSERVICES` | `Microservices` |
| `STATISTICS` | `Statistics and Probability`, `Statistics`, `Probability` |
| `ML_MODEL_DEVELOPMENT` | `Machine-learning model development`, `Machine learning model development` |

## State diagramas

Edges that share an output are drawn as one arrow whose label lists the inputs (input1 | input2 / OUTPUT). Each arrow stands for one transition per listed input.

## T_lang

![T_lang transducer diagram](img/T_lang.png)

## T _rw

![T_fw transducer diagram](img/T_fw.png)

## T_db

![T_db transducer diagram](img/T_db.png)

## T_tool

![T_tool transducer diagram](img/T_tool.png)

## T _other

![T_other transducer diagram](img/T_other.png)

# How the transucers are applied

* `normalize_token(token, T)`: applies the transducer `T` to one token and returns its canonical label, or `None` if the token is not accepted.

* `normalize_category(tokens, category)`: applies the category's transducer to every token in the list.

* `normalize_qualifications(info)`: joins the five categories (languages, frameworks, databases, tools, other qualifications) into one list, in that fixed order.

The fields `name`, `contact`, `experience_years` and `academic_qualifications` pass through unchanged. Duplicates are kept: `React, ReactJS, React.js` → `REACT, REACT, REACT`.