import unittest
from pathlib import Path

from resumelens.extraction import extract_resume_info
from resumelens.normalization import normalize_resume_info
from resumelens.normalization.transducers import (
    DATABASES_TRANSDUCER,
    FRAMEWORKS_TRANSDUCER,
    PROGRAMMING_LANGUAGES_TRANSDUCER,
)
from resumelens.normalization.normalizer import normalize_token

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "resumes"


class TestTransducers(unittest.TestCase):
    def test_programming_language_variants(self):
        self.assertEqual(
            normalize_token("JS", PROGRAMMING_LANGUAGES_TRANSDUCER), "JAVASCRIPT"
        )
        self.assertEqual(
            normalize_token("Javascript", PROGRAMMING_LANGUAGES_TRANSDUCER),
            "JAVASCRIPT",
        )

    def test_framework_variants(self):
        self.assertEqual(normalize_token("React.js", FRAMEWORKS_TRANSDUCER), "REACT")
        self.assertEqual(normalize_token("ReactJS", FRAMEWORKS_TRANSDUCER), "REACT")
        self.assertEqual(normalize_token("NodeJS", FRAMEWORKS_TRANSDUCER), "NODE_JS")
        self.assertEqual(normalize_token("Node.js", FRAMEWORKS_TRANSDUCER), "NODE_JS")

    def test_database_variants(self):
        self.assertEqual(
            normalize_token("Postgres", DATABASES_TRANSDUCER), "POSTGRESQL"
        )
        self.assertEqual(
            normalize_token("PostgreSQL", DATABASES_TRANSDUCER), "POSTGRESQL"
        )

    def test_unknown_token_is_rejected(self):
        self.assertIsNone(normalize_token("COBOL", PROGRAMMING_LANGUAGES_TRANSDUCER))


class TestNormalizeResumeInfo(unittest.TestCase):
    def test_full_stack_developer_matches_project_statement_example(self):
        text = (DATA_DIR / "juan_jaramillo.txt").read_text()
        extracted = extract_resume_info(text)
        normalized = normalize_resume_info(extracted, "FULL_STACK_DEVELOPER")

        self.assertEqual(
            normalized["qualifications"],
            ["JAVASCRIPT", "REACT", "NODE_JS", "POSTGRESQL", "GIT"],
        )

    def test_machine_learning_engineer(self):
        text = (DATA_DIR / "juliana_galvis.txt").read_text()
        extracted = extract_resume_info(text)
        normalized = normalize_resume_info(extracted, "MACHINE_LEARNING_ENGINEER")

        self.assertEqual(
            normalized["qualifications"],
            ["PYTHON", "PANDAS", "NUMPY", "SCIKIT_LEARN", "TENSORFLOW", "SQL", "GIT"],
        )

    def test_software_architect_reorders_other_qualifications(self):
        text = (DATA_DIR / "andres_aristizabal.txt").read_text()
        extracted = extract_resume_info(text)
        normalized = normalize_resume_info(extracted, "SOFTWARE_ARCHITECT")

        self.assertEqual(
            normalized["qualifications"],
            [
                "JAVA",
                "DESIGN_PATTERNS",
                "MICROSERVICES",
                "DOCKER",
                "KUBERNETES",
                "AWS",
                "REST_API",
                "GIT",
            ],
        )


if __name__ == "__main__":
    unittest.main()
