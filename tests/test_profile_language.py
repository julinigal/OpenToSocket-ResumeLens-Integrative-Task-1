import unittest
from pathlib import Path

from textx.exceptions import TextXSyntaxError

from resumelens.classification import classify_qualifications
from resumelens.classification.profile_patterns import PROFILE_GROUPS
from resumelens.extraction import extract_resume_info
from resumelens.normalization import normalize_resume_info
from resumelens.profile_language import (
    build_candidate_profile,
    parse_candidate_profile,
    render_candidate_profile,
    render_html,
)

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "resumes"


def classify_against_all_profiles(extracted):
    results = {}
    best_qualifications = None
    for profile_name in PROFILE_GROUPS:
        normalized = normalize_resume_info(extracted, profile_name)
        result = classify_qualifications(normalized["qualifications"], profile_name)
        results[profile_name] = result
        if result == "ACCEPTED":
            best_qualifications = normalized["qualifications"]
    return results, best_qualifications or []


class TestDSL(unittest.TestCase):
    def test_render_and_parse_round_trip(self):
        text = render_candidate_profile(
            name="Juan Jaramillo",
            contact={"emails": [], "phones": []},
            experience_years=3,
            qualifications=["JAVASCRIPT", "REACT", "NODE_JS", "GIT"],
            classification_results={
                "FULL_STACK_DEVELOPER": "ACCEPTED",
                "MACHINE_LEARNING_ENGINEER": "REJECTED",
                "DATA_SCIENTIST": "REJECTED",
                "SOFTWARE_ARCHITECT": "REJECTED",
            },
        )
        model = parse_candidate_profile(text)

        self.assertEqual(model.name, "Juan Jaramillo")
        self.assertEqual(model.years, 3)
        self.assertEqual(model.skills, ["JAVASCRIPT", "REACT", "NODE_JS", "GIT"])
        statuses = {r.profile: r.status for r in model.results}
        self.assertEqual(statuses["FULL_STACK_DEVELOPER"], "ACCEPTED")

    def test_contact_information_is_included_when_present(self):
        text = render_candidate_profile(
            name="Juliana Galvis",
            contact={"emails": ["juliana@example.com"], "phones": ["+1-555-123-4567"]},
            experience_years=2,
            qualifications=["PYTHON", "GIT"],
            classification_results={"MACHINE_LEARNING_ENGINEER": "ACCEPTED"},
        )
        model = parse_candidate_profile(text)

        self.assertEqual(model.email, "juliana@example.com")
        self.assertEqual(model.phone, "+1-555-123-4567")

    def test_rejects_invalid_profile_name(self):
        invalid_text = (
            "Candidate Bad Example\n"
            "Experience 2 years\n"
            "Skills PYTHON\n"
            "Classification\n"
            "  NOT_A_REAL_PROFILE = ACCEPTED\n"
        )
        with self.assertRaises(TextXSyntaxError):
            parse_candidate_profile(invalid_text)

    def test_rejects_invalid_status(self):
        invalid_text = (
            "Candidate Bad Example\n"
            "Experience 2 years\n"
            "Skills PYTHON\n"
            "Classification\n"
            "  MACHINE_LEARNING_ENGINEER = MAYBE\n"
        )
        with self.assertRaises(TextXSyntaxError):
            parse_candidate_profile(invalid_text)


class TestEndToEndVisualization(unittest.TestCase):
    def test_juan_jaramillo_full_pipeline_and_html(self):
        text = (DATA_DIR / "juan_jaramillo.txt").read_text()
        extracted = extract_resume_info(text)
        results, qualifications = classify_against_all_profiles(extracted)

        model = build_candidate_profile(
            name=extracted["name"],
            contact=extracted["contact"],
            experience_years=extracted["experience_years"],
            qualifications=qualifications,
            classification_results=results,
        )
        html = render_html(model)

        self.assertEqual(results["FULL_STACK_DEVELOPER"], "ACCEPTED")
        self.assertIn("Juan Jaramillo", html)
        self.assertIn("FULL_STACK_DEVELOPER: ACCEPTED", html)
        self.assertIn("<li>GIT</li>", html)


if __name__ == "__main__":
    unittest.main()
