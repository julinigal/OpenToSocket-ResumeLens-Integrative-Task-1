from .profile_order import PROFILE_ORDER
from .transducers import TRANSDUCERS_BY_CATEGORY

QUALIFICATION_CATEGORIES = (
    "programming_languages",
    "frameworks",
    "databases",
    "tools",
    "other_qualifications",
)


def normalize_token(token, transducer):
    outputs = list(transducer.translate([token]))
    return outputs[0][0] if outputs else None


def normalize_category(tokens, category):
    transducer = TRANSDUCERS_BY_CATEGORY[category]
    return [normalize_token(token, transducer) for token in tokens]


def normalize_qualifications(extracted_info):
    normalized = []
    for category in QUALIFICATION_CATEGORIES:
        normalized.extend(normalize_category(extracted_info[category], category))
    return normalized


def sort_qualifications(qualifications, profile_name):
    order = PROFILE_ORDER[profile_name]

    def sort_key(qualification):
        return order.index(qualification) if qualification in order else len(order)

    return sorted(qualifications, key=sort_key)


def normalize_resume_info(extracted_info, profile_name):
    qualifications = normalize_qualifications(extracted_info)
    return {
        "name": extracted_info["name"],
        "contact": extracted_info["contact"],
        "experience_years": extracted_info["experience_years"],
        "academic_qualifications": extracted_info["academic_qualifications"],
        "qualifications": sort_qualifications(qualifications, profile_name),
    }
