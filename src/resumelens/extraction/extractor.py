import json
from pathlib import Path

from . import patterns


def extract_name(text):
    match = patterns.NAME_PATTERN.match(text.strip())
    return match.group(0) if match else None


def extract_contact_info(text):
    return {
        "emails": patterns.EMAIL_PATTERN.findall(text),
        "phones": patterns.PHONE_PATTERN.findall(text),
    }


def extract_experience_years(text):
    match = patterns.EXPERIENCE_YEARS_PATTERN.search(text)
    return int(match.group(1)) if match else None


def extract_programming_languages(text):
    return patterns.PROGRAMMING_LANGUAGES_PATTERN.findall(text)


def extract_frameworks(text):
    return patterns.FRAMEWORKS_PATTERN.findall(text)


def extract_databases(text):
    return patterns.DATABASES_PATTERN.findall(text)


def extract_tools(text):
    return patterns.TOOLS_PATTERN.findall(text)


def extract_academic_qualifications(text):
    return patterns.ACADEMIC_PATTERN.findall(text)


def extract_other_qualifications(text):
    return patterns.OTHER_QUALIFICATIONS_PATTERN.findall(text)


def extract_resume_info(text):
    return {
        "name": extract_name(text),
        "contact": extract_contact_info(text),
        "experience_years": extract_experience_years(text),
        "programming_languages": extract_programming_languages(text),
        "frameworks": extract_frameworks(text),
        "databases": extract_databases(text),
        "tools": extract_tools(text),
        "academic_qualifications": extract_academic_qualifications(text),
        "other_qualifications": extract_other_qualifications(text),
    }


def save_extracted_info(info, output_path):
    Path(output_path).write_text(json.dumps(info, indent=2))
