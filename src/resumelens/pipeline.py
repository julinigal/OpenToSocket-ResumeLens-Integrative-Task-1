from resumelens.classification import classify_qualifications
from resumelens.classification.profile_patterns import PROFILE_GROUPS
from resumelens.extraction import extract_resume_info
from resumelens.normalization import normalize_resume_info
from resumelens.profile_language import build_candidate_profile, render_html

ALL_PROFILES = list(PROFILE_GROUPS)


def run_pipeline(resume_text, target_profile):
    extracted = extract_resume_info(resume_text)

    classification_results = {}
    target_qualifications = []
    for profile_name in ALL_PROFILES:
        normalized = normalize_resume_info(extracted, profile_name)
        classification_results[profile_name] = classify_qualifications(
            normalized["qualifications"], profile_name
        )
        if profile_name == target_profile:
            target_qualifications = normalized["qualifications"]

    model = build_candidate_profile(
        name=extracted["name"],
        contact=extracted["contact"],
        experience_years=extracted["experience_years"],
        qualifications=target_qualifications,
        classification_results=classification_results,
    )
    html = render_html(model)

    return classification_results, html