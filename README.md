# ResumeLens

This is our Integrative Task 1 project for Computation and Discrete Structures III.

Each person lists their skills differently (e.g., JS, Javascript, JavaScript), and each position requires a unique combination. Reviewing this manually is slow and inconsistent. ResumeLens reads a resume and checks whether the listed skills match each profile's pattern using formal language theory—regular expressions, transducers, automata, and grammars—yielding one of two outcomes per profile (accepted or rejected). The tool does not rank candidates or make hiring decisions; it only verifies whether the text conforms to a defined pattern.

## Members
* Juan Fernando Jaramillo Gutiérrez - A00407692
* María Juliana Niño Galvis - A00406954

## Technical Stack
* **Language:** Python 3
* **IDE:** Visual Studio Code
* **Libraries:**
  * `pyformlang` — finite-state transducers (Stage 2) and finite automata (Stage 3)
  * `textx` — the candidate profile grammar (Stage 4)
  * `pydot` — diagram generation for transducers and automata

## How to Run It

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

From the project root, with the virtual environment active:

```bash
# run all the tests
PYTHONPATH=src python -m unittest discover -s tests -v

# run the pipeline on the sample resumes and generate their HTML profiles
PYTHONPATH=src python examples/run_example.py
```

The generated HTML files are written to `examples/output/`, one per candidate.

## Project Structure

```
ResumeLens/
├── README.md
├── requirements.txt
├── data/
│   ├── profiles/
│   │   └── profiles.md       
│   └── resumes/   
│        └── andres_aristizabal.txt
│        └── juan_jaramillo.txt
│        └── juliana_galvis.txt
│        └── tony_stark.txt
├── src/
│   └── resumelens/
│       ├── extraction/        
│       ├── normalization/     
│       ├── classification/     
│       ├── profile_language/  
│       └── pipeline.py      
├── tests/                     
└── examples/
    └── run_example.py          
```

----
