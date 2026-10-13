from pathlib import Path

from textx import metamodel_from_file

GRAMMAR_PATH = Path(__file__).parent / "candidate.tx"
METAMODEL = metamodel_from_file(str(GRAMMAR_PATH))


def render_candidate_profile(
    name, contact, experience_years, qualifications, classification_results
):
    lines = [f"Candidate {name}"]

    emails = contact.get("emails") or []
    phones = contact.get("phones") or []
    if emails or phones:
        contact_line = "Contact"
        if emails:
            contact_line += f" email: {emails[0]}"
        if phones:
            contact_line += f" phone: {phones[0]}"
        lines.append(contact_line)

    lines.append(f"Experience {experience_years or 0} years")
    lines.append("Skills " + ", ".join(qualifications))
    lines.append("Classification")
    for profile_name, status in classification_results.items():
        lines.append(f"  {profile_name} = {status}")

    return "\n".join(lines)


def parse_candidate_profile(text):
    return METAMODEL.model_from_str(text)


def build_candidate_profile(
    name, contact, experience_years, qualifications, classification_results
):
    text = render_candidate_profile(
        name, contact, experience_years, qualifications, classification_results
    )
    return parse_candidate_profile(text)
