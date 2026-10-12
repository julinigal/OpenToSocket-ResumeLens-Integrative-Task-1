## Canonical Ordering Formalization

### Definition

For a profile p, let `L_p = (l_1, …, l_n)` be its canonical list (`profile_order.py`). The rank of a canonical label q is:

* `rank_p(q) = i - 1` if `q = l_i` (0-based position in `L_p`)
* `rank_p(q) = n` if `q ∉ L_p` (labels the profile does not list)

`sort_qualifications` returns the input list sorted by `rank_p` with Python's stable sort (`sorted(..., key=rank_p)`).

As a result, labels that appear in `L_p` follow the order of the profile, and repeated ones stay together. Labels the profile does not list go to the end, in the same order they had after normalization, nothing is removed from the list.

# Canonical lists

| Profile | n | L_p |
|---------|---|-----|
| `FULL_STACK_DEVELOPER` | 13 | JAVASCRIPT, TYPESCRIPT, REACT, ANGULAR, VUE, NODE_JS, DJANGO, SPRING_BOOT, SQL, NOSQL, POSTGRESQL, REST_API, GIT |
| `MACHINE_LEARNING_ENGINEER` | 9 | PYTHON, PANDAS, NUMPY, SCIKIT_LEARN, TENSORFLOW, PYTORCH, ML_MODEL_DEVELOPMENT, SQL, GIT |
| `DATA_SCIENTIST` | 10 | PYTHON, R, PANDAS, NUMPY, SCIKIT_LEARN, MATPLOTLIB, SEABORN, STATISTICS, SQL, GIT |
| `SOFTWARE_ARCHITECT` | 15 | JAVA, CSHARP, PYTHON, DESIGN_PATTERNS, MICROSERVICES, DOCKER, KUBERNETES, AWS, AZURE, GCP, REST_API, GRAPHQL, SQL, NOSQL, GIT |
