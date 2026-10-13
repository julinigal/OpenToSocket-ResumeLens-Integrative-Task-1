from pyformlang.fst import FST

PROGRAMMING_LANGUAGES_TRANSDUCER = FST()
PROGRAMMING_LANGUAGES_TRANSDUCER.add_transitions([
    ("q0", "JavaScript", "qf", ["JAVASCRIPT"]),
    ("q0", "Javascript", "qf", ["JAVASCRIPT"]),
    ("q0", "JS", "qf", ["JAVASCRIPT"]),
    ("q0", "TypeScript", "qf", ["TYPESCRIPT"]),
    ("q0", "Python", "qf", ["PYTHON"]),
    ("q0", "Java", "qf", ["JAVA"]),
    ("q0", "C#", "qf", ["CSHARP"]),
    ("q0", "R", "qf", ["R"]),
])
PROGRAMMING_LANGUAGES_TRANSDUCER.add_start_state("q0")
PROGRAMMING_LANGUAGES_TRANSDUCER.add_final_state("qf")

FRAMEWORKS_TRANSDUCER = FST()
FRAMEWORKS_TRANSDUCER.add_transitions([
    ("q0", "React.js", "qf", ["REACT"]),
    ("q0", "ReactJS", "qf", ["REACT"]),
    ("q0", "React", "qf", ["REACT"]),
    ("q0", "Angular", "qf", ["ANGULAR"]),
    ("q0", "Vue", "qf", ["VUE"]),
    ("q0", "Node.js", "qf", ["NODE_JS"]),
    ("q0", "NodeJS", "qf", ["NODE_JS"]),
    ("q0", "Node", "qf", ["NODE_JS"]),
    ("q0", "Django", "qf", ["DJANGO"]),
    ("q0", "Spring Boot", "qf", ["SPRING_BOOT"]),
    ("q0", "Scikit-learn", "qf", ["SCIKIT_LEARN"]),
    ("q0", "scikit learn", "qf", ["SCIKIT_LEARN"]),
    ("q0", "sklearn", "qf", ["SCIKIT_LEARN"]),
    ("q0", "Tensor Flow", "qf", ["TENSORFLOW"]),
    ("q0", "TensorFlow", "qf", ["TENSORFLOW"]),
    ("q0", "Py Torch", "qf", ["PYTORCH"]),
    ("q0", "PyTorch", "qf", ["PYTORCH"]),
    ("q0", "Pandas", "qf", ["PANDAS"]),
    ("q0", "pandas", "qf", ["PANDAS"]),
    ("q0", "NumPy", "qf", ["NUMPY"]),
    ("q0", "Matplotlib", "qf", ["MATPLOTLIB"]),
    ("q0", "Seaborn", "qf", ["SEABORN"]),
])
FRAMEWORKS_TRANSDUCER.add_start_state("q0")
FRAMEWORKS_TRANSDUCER.add_final_state("qf")

DATABASES_TRANSDUCER = FST()
DATABASES_TRANSDUCER.add_transitions([
    ("q0", "PostgreSQL", "qf", ["POSTGRESQL"]),
    ("q0", "Postgres", "qf", ["POSTGRESQL"]),
    ("q0", "NoSQL", "qf", ["NOSQL"]),
    ("q0", "SQL", "qf", ["SQL"]),
])
DATABASES_TRANSDUCER.add_start_state("q0")
DATABASES_TRANSDUCER.add_final_state("qf")

TOOLS_TRANSDUCER = FST()
TOOLS_TRANSDUCER.add_transitions([
    ("q0", "REST APIs", "qf", ["REST_API"]),
    ("q0", "REST API", "qf", ["REST_API"]),
    ("q0", "GraphQL", "qf", ["GRAPHQL"]),
    ("q0", "Git", "qf", ["GIT"]),
    ("q0", "Docker", "qf", ["DOCKER"]),
    ("q0", "Kubernetes", "qf", ["KUBERNETES"]),
    ("q0", "AWS", "qf", ["AWS"]),
    ("q0", "Azure", "qf", ["AZURE"]),
    ("q0", "GCP", "qf", ["GCP"]),
])
TOOLS_TRANSDUCER.add_start_state("q0")
TOOLS_TRANSDUCER.add_final_state("qf")

OTHER_QUALIFICATIONS_TRANSDUCER = FST()
OTHER_QUALIFICATIONS_TRANSDUCER.add_transitions([
    ("q0", "Software Design Patterns", "qf", ["DESIGN_PATTERNS"]),
    ("q0", "Design Patterns", "qf", ["DESIGN_PATTERNS"]),
    ("q0", "Microservices", "qf", ["MICROSERVICES"]),
    ("q0", "Statistics and Probability", "qf", ["STATISTICS"]),
    ("q0", "Statistics", "qf", ["STATISTICS"]),
    ("q0", "Probability", "qf", ["STATISTICS"]),
    ("q0", "Machine-learning model development", "qf", ["ML_MODEL_DEVELOPMENT"]),
    ("q0", "Machine learning model development", "qf", ["ML_MODEL_DEVELOPMENT"]),
])
OTHER_QUALIFICATIONS_TRANSDUCER.add_start_state("q0")
OTHER_QUALIFICATIONS_TRANSDUCER.add_final_state("qf")

TRANSDUCERS_BY_CATEGORY = {
    "programming_languages": PROGRAMMING_LANGUAGES_TRANSDUCER,
    "frameworks": FRAMEWORKS_TRANSDUCER,
    "databases": DATABASES_TRANSDUCER,
    "tools": TOOLS_TRANSDUCER,
    "other_qualifications": OTHER_QUALIFICATIONS_TRANSDUCER,
}
