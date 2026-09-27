"""Shared helpers for Practice Skills catalog records."""

from __future__ import annotations


def skill(
    name,
    title,
    job,
    artifact,
    triggers,
    inputs,
    steps,
    anti,
    example,
    example_out,
    related=None,
    avoid=None,
    outputs=None,
    checks=None,
):
    if not isinstance(steps, (list, tuple)) or len(steps) < 5:
        raise ValueError(f"{name}: need at least 5 steps")
    if not isinstance(triggers, (list, tuple)) or len(triggers) < 3:
        raise ValueError(f"{name}: need at least 3 triggers")
    if not isinstance(anti, (list, tuple)) or len(anti) < 3:
        raise ValueError(f"{name}: need at least 3 anti-patterns")
    return {
        "name": name,
        "title": title,
        "job": job,
        "artifact": artifact,
        "triggers": list(triggers),
        "inputs": list(inputs),
        "steps": list(steps),
        "anti": list(anti),
        "example": example,
        "example_out": example_out,
        "related": list(related or []),
        "avoid": list(avoid or []),
        "outputs": list(outputs or []),
        "checks": list(checks or []),
    }
