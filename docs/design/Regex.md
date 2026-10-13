## Regex Formalization (Data Extraction)

## Convetions:

* Alphabet Σ: Unicode characters (Python `re`, `str` patterns).

* Every pattern is compiled in `patterns.py`and used in `extractor.py`.

* Literal-list paatterns are finite languages delmited by \b.

* In Python the alternation is ordered (first alternative that matches wins, not the longest).

## Pattern catalogue

# R1 - Name

* Regular expression: `^[A-Za-z] + (?: [A-Za-z]+)*`

* Explanation: From the start of the stripped text: one or more letters, followed by any number of single space + letters. It sopts at the first newline, so it captures only the first line

* Function: extract_name -> .match(text.strip()), this returns group(0) pr Noe

* The data is stored in info `["name"]`

# R2 - Email

* Regultar expression : `[\w.+-]@[\w-]+\.[a-zA-Z]{2,}`

* Explantion: Matches local part @ domain. TLD: the local part `[\w.+-]` accepts word characters, ., + and -, then a literal @, the one domain label `[\w-]`, next a literal dot and a TLD of at least 2 letters (`[a-zA-Z]{2,}`)

* Function: `extract_contact_info` -> `findall`

* The data is stored in `info["contact"]["emails"](list[str])`

## R3 - Phone

* Regular expression: `\+?\d[\d \-]{7,}\d`

* Explanation: First it starts with an optional `+`, a digit, 7 or more digits/spaces/hyphens, and a final digit (so ≥ 9 characters, starting and ending with a digit).

* Function : `extract_contact_info` -> `.findall`

* The data is stored in `info["contact"]["phones"]` (`list[str]`)

## R4 - Years of experience

* Regular expression: `(\d+)\s+years?\s+of\s+experience`

* Explanation: `D⁺ W⁺ year s? W⁺ of W⁺ experience`. Group 1 is the number. Case-sensitive, first occurrence only.

* Function : `extract_experience_years` —> `.search`, `int(group(1))`

* The data is stored in `info["experience_years"]` (`int | None`)

# R5 - Programming Languages

* Regular expression: `\b(?:JavaScript|Javascript|TypeScript|Python|Java|C#|JS|R)\b`

* Explanation: A finite set of 8 surface forms that identify programming languages. `(?: ... )` is a non-capturing group, it only groups the alternatives, which are separated by `|`, so `.findall` returns the full matched text. The word boundaries `\b` force each match to be a whole word, so `Java` is not extracted from `JavaScript` and `R` is not extracted from `React`.

* Function : `extract_programming_languages` —> `.findall`

* The data is stored in `info["programming_languages"]` (`list[str]`)

# R6 - Frameworks / libraries

* Regular expression: `\b(?:React\.js|ReactJS|React|Angular|Vue|Node\.js|NodeJS|Node|Django|Spring Boot|Scikit-learn|scikit learn|sklearn|Tensor Flow|TensorFlow|Py Torch|PyTorch|Pandas|pandas|NumPy|Matplotlib|Seaborn)\b`

* Explanation: A finite set of 22 surface forms that identify frameworks and libraries, including spelling and spacing variants such as `React.js`, `ReactJS` and `Tensor Flow`. `(?: ... )` is a non-capturing group, it only groups the alternatives, which are separated by `|` , so `.findall` returns the full matched text. The word boundaries `\b` force each match to be a whole word, so `React` is not extracted from `ReactNative`. The longer variants come first (`React.js` before `React`, `Node.js` before `Node`) because Python tries the alternatives in order, so `React` would otherwise match first and leave `.js` out.

* Function : `extract_frameworks` —> `.findall`

* Where the data is stored: `info["frameworks"]`

# R7 - Databases

* Regular expression: `\b(?:PostgreSQL|Postgres|NoSQL|SQL)\b`

* Explanation: 4 surface forms. `\b` prevents matching `SQL` inside `NoSQL`.

* Function / method: `extract_databases` —> `.findall`
* The data is stored in `info["databases"]`

# R8 - Tools

* Regular expression: `\b(?:REST APIs|REST API|GraphQL|Git|Docker|Kubernetes|AWS|Azure|GCP)\b`

* Explanation: A finite set of 9 surface forms that identify tools and technologies such as `Git`, `Docker` and `AWS`. `(?: ... )` is a non-capturing group: it only groups the alternatives, which are separated by `|` , so `.findall` returns the full matched text. The word boundaries `\b` force each match to be a whole word, so `Git` is not extracted from `GitHub`.

* Function : `extract_tools` —> `.findall`

* The data is stored in `info["tools"]`

# R9 - Other qualif

* Regular expression: `\b(?:Software Design Patterns|Design Patterns|Microservices|Statistics and Probability|Statistics|Probability|Machine-learning model development|Machine learning model development)\b`

* Explanation: A finite set of 8 surface forms that identify qualifications that are not languages, frameworks, databases or tools, such as design patterns, microservices, statistics and machine-learning model development. `(?: ... )` is a non-capturing group, it only groups the alternatives, which are separated by `|` ("or"), so `.findall` returns the full matched text. The word boundaries `\b` force each match to be a whole word or phrase. `Statistics and Probability` goes before `Statistics` because both start at the same position and Python tries the alternatives in order; otherwise the phrase would be split into two separate matches, `Statistics` and `Probability`.

* Function: `extract_other_qualifications` ->`.findall`

* The data is stored in `info["other_qualifications"]`

# R10 - Academic qualifications

* Regular expression: `\b(?:Bachelor|Master|PhD|Ingenier[ií]a|Licenciatura)[^.\n]*`

* Explanation: Follows the same logic as the previous patterns: `(?: ... )` groups the alternatives, which are separated by `|`, and the initial `\b` makes the keyword start at a word boundary. The difference is that the alternatives are only the start of a degree (5 keywords: `Bachelor`, `Master`, `PhD`, `Ingenier[ií]a`, `Licenciatura`; the class `[ií]` accepts the word with or without accent), and then `[^.\n]*` consumes everything up to the next period or newline, so the match is the whole degree description, for example `Bachelor of Science in Systems Engineering`. There is no closing `\b` because the match continues after the keyword.

* Function : `extract_academic_qualifications` -> `.findall`

* Where the data is stored: `info["academic_qualifications"]`