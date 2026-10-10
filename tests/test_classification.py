import unittest
from pathlib import Path

from resumelens.classification import classify_qualifications
from resumelens.classification.automata import AUTOMATA_BY_PROFILE
from resumelens.extraction import extract_resume_info
from resumelens.normalization import normalize_resume_info

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "resumes"


class TestProfileAutomata(unittest.TestCase):
    def test_full_stack_developer_accepts_required_pattern(self):
        dfa = AUTOMATA_BY_PROFILE["FULL_STACK_DEVELOPER"]
        self.assertTrue(dfa.accepts(["JAVASCRIPT", "REACT", "NODE_JS", "GIT"]))

    def test_full_stack_developer_rejects_missing_git(self):
        dfa = AUTOMATA_BY_PROFILE["FULL_STACK_DEVELOPER"]
        self.assertFalse(dfa.accepts(["JAVASCRIPT", "REACT"]))

    def test_full_stack_developer_rejects_wrong_order(self):
        dfa = AUTOMATA_BY_PROFILE["FULL_STACK_DEVELOPER"]
        self.assertFalse(dfa.accepts(["GIT", "JAVASCRIPT", "REACT"]))

    def test_full_stack_developer_rejects_missing_language(self):
        dfa = AUTOMATA_BY_PROFILE["FULL_STACK_DEVELOPER"]
        self.assertFalse(dfa.accepts(["REACT", "GIT"]))


class TestClassifyResumes(unittest.TestCase):
    def _classify(self, resume_file, profile_name):
        text = (DATA_DIR / resume_file).read_text()
        extracted = extract_resume_info(text)
        normalized = normalize_resume_info(extracted, profile_name)
        return classify_qualifications(normalized["qualifications"], profile_name)

    def test_juan_jaramillo_accepted_as_full_stack_developer(self):
        result = self._classify("juan_jaramillo.txt", "FULL_STACK_DEVELOPER")
        self.assertEqual(result, "ACCEPTED")

    def test_juliana_galvis_accepted_as_machine_learning_engineer(self):
        result = self._classify("juliana_galvis.txt", "MACHINE_LEARNING_ENGINEER")
        self.assertEqual(result, "ACCEPTED")

    def test_tony_stark_accepted_as_data_scientist(self):
        result = self._classify("tony_stark.txt", "DATA_SCIENTIST")
        self.assertEqual(result, "ACCEPTED")

    def test_andres_aristizabal_accepted_as_software_architect(self):
        result = self._classify("andres_aristizabal.txt", "SOFTWARE_ARCHITECT")
        self.assertEqual(result, "ACCEPTED")

    def test_juan_jaramillo_rejected_as_machine_learning_engineer(self):
        result = self._classify("juan_jaramillo.txt", "MACHINE_LEARNING_ENGINEER")
        self.assertEqual(result, "REJECTED")

    def test_juliana_galvis_rejected_as_software_architect(self):
        result = self._classify("juliana_galvis.txt", "SOFTWARE_ARCHITECT")
        self.assertEqual(result, "REJECTED")

    def test_andres_aristizabal_rejected_as_data_scientist(self):
        result = self._classify("andres_aristizabal.txt", "DATA_SCIENTIST")
        self.assertEqual(result, "REJECTED")


if __name__ == "__main__":
    unittest.main()
