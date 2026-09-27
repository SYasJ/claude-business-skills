"""Hand-written scenarios. A skill listed here overrides the generated example."""

BANK = {}


def put(name, purpose, scenario, data, outcome):
    BANK[name] = {
        "purpose": purpose.strip(),
        "scenario": scenario.strip(),
        "data": data.strip(),
        "outcome": outcome.strip(),
    }
