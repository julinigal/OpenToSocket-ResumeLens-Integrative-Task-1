import re

NAME_PATTERN = re.compile(r"^[A-Za-z]+(?: [A-Za-z]+)*")

EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}")

PHONE_PATTERN = re.compile(r"\+?\d[\d \-]{7,}\d")

EXPERIENCE_YEARS_PATTERN = re.compile(r"(\d+)\s+years?\s+of\s+experience")

PROGRAMMING_LANGUAGES_PATTERN = re.compile(
    r"\b(?:JavaScript|Javascript|TypeScript|Python|Java|C#|JS|R)\b"
)

FRAMEWORKS_PATTERN = re.compile(
    r"\b(?:React\.js|ReactJS|React|Angular|Vue|Node\.js|NodeJS|Node|Django|"
    r"Spring Boot|Scikit-learn|scikit learn|sklearn|Tensor Flow|TensorFlow|"
    r"Py Torch|PyTorch|Pandas|pandas|NumPy|Matplotlib|Seaborn)\b"
)

DATABASES_PATTERN = re.compile(r"\b(?:PostgreSQL|Postgres|NoSQL|SQL)\b")

TOOLS_PATTERN = re.compile(
    r"\b(?:REST APIs|REST API|GraphQL|Git|Docker|Kubernetes|AWS|Azure|GCP)\b"
)

OTHER_QUALIFICATIONS_PATTERN = re.compile(
    r"\b(?:Software Design Patterns|Design Patterns|Microservices|"
    r"Statistics and Probability|Statistics|Probability|"
    r"Machine-learning model development|Machine learning model development)\b"
)

ACADEMIC_PATTERN = re.compile(
    r"\b(?:Bachelor|Master|PhD|Ingenier[ií]a|Licenciatura)[^.\n]*"
)
