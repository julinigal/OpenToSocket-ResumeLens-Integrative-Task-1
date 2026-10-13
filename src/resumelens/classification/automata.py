from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol

from .profile_patterns import PROFILE_GROUPS


def build_profile_automaton(groups):
    n_groups = len(groups)
    states = {State(f"q{i}") for i in range(n_groups + 1)}
    symbols = {Symbol(s) for _, group_symbols in groups for s in group_symbols}

    automaton = DeterministicFiniteAutomaton(
        states=states,
        input_symbols=symbols,
        start_state=State("q0"),
        final_states={State(f"q{n_groups}")},
    )

    transitions = []
    for i, (_, group_symbols) in enumerate(groups):
        before_state = State(f"q{i}")
        after_state = State(f"q{i + 1}")
        for symbol in group_symbols:
            transitions.append((before_state, symbol, after_state))
            transitions.append((after_state, symbol, after_state))
    automaton.add_transitions(transitions)
    return automaton


AUTOMATA_BY_PROFILE = {
    profile_name: build_profile_automaton(groups)
    for profile_name, groups in PROFILE_GROUPS.items()
}


def profile_alphabet(profile_name):
    groups = PROFILE_GROUPS[profile_name]
    return {s for _, group_symbols in groups for s in group_symbols}
