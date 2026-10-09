import unittest
from pathlib import Path

from resumelens.extraction import extract_resume_info

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "resumes"


class TestExtraction(unittest.TestCase):
    def test_full_stack_developer_resume(self):
        text = (DATA_DIR / "juan_jaramillo.txt").read_text()
        info = extract_resume_info(text)

        self.assertEqual(info["name"], "Juan Jaramillo")
        self.assertEqual(info["experience_years"], 3)
        self.assertEqual(info["programming_languages"], ["JS"])
        self.assertEqual(info["frameworks"], ["React.js", "NodeJS"])
        self.assertEqual(info["databases"], ["Postgres"])
        self.assertEqual(info["tools"], ["Git"])

    def test_machine_learning_engineer_resume(self):
        text = (DATA_DIR / "juliana_galvis.txt").read_text()
        info = extract_resume_info(text)

        self.assertEqual(info["name"], "Juliana Galvis")
        self.assertEqual(info["experience_years"], 2)
        self.assertEqual(info["programming_languages"], ["Python"])
        self.assertEqual(
            info["frameworks"], ["Pandas", "NumPy", "Scikit-learn", "TensorFlow"]
        )
        self.assertEqual(info["databases"], ["SQL"])
        self.assertEqual(info["tools"], ["Git"])

    def test_data_scientist_resume(self):
        text = (DATA_DIR / "tony_stark.txt").read_text()
        info = extract_resume_info(text)

        self.assertEqual(info["name"], "Tony Stark")
        self.assertEqual(info["experience_years"], 4)
        self.assertEqual(info["programming_languages"], ["Python"])
        self.assertEqual(
            info["frameworks"], ["Pandas", "Matplotlib", "Seaborn", "Scikit-learn"]
        )
        self.assertEqual(info["databases"], ["SQL"])
        self.assertEqual(info["tools"], ["Git"])
        self.assertEqual(info["other_qualifications"], ["Statistics and Probability"])

    def test_software_architect_resume(self):
        text = (DATA_DIR / "andres_aristizabal.txt").read_text()
        info = extract_resume_info(text)

        self.assertEqual(info["name"], "Andres Aristizabal")
        self.assertEqual(info["experience_years"], 5)
        self.assertEqual(info["programming_languages"], ["Java"])
        self.assertEqual(info["frameworks"], [])
        self.assertEqual(info["databases"], [])
        self.assertEqual(info["tools"], ["Docker", "Kubernetes", "AWS", "REST API", "Git"])
        self.assertEqual(
            info["other_qualifications"], ["Software Design Patterns", "Microservices"]
        )


if __name__ == "__main__":
    unittest.main()