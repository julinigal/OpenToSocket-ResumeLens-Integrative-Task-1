from .automata import AUTOMATA_BY_PROFILE, profile_alphabet


def classify_qualifications(qualifications, profile_name):
    alphabet = profile_alphabet(profile_name)
    relevant_qualifications = [q for q in qualifications if q in alphabet]

    automaton = AUTOMATA_BY_PROFILE[profile_name]
    return "ACCEPTED" if automaton.accepts(relevant_qualifications) else "REJECTED"
