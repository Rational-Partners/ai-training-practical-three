"""Tests for Challenge 5: CP-SAT optimal solver"""
import pytest
from datetime import date
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
BASIC_XLSX = os.path.join(DATA_DIR, "basic.xlsx")

CONFIG = {
    "experienced": {"Alice Chen", "Bob Smith", "Diana Müller"},
    "trainees": {"Carol Jones"},
}


def _get_schedule():
    from scheduler import parse_availability, generate_slots, schedule_optimal
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    return schedule_optimal(dates, trainers, slots, config=CONFIG), trainers, slots


def test_returns_list_of_dicts():
    schedule, _, _ = _get_schedule()
    assert isinstance(schedule, list)


def test_each_bootcamp_has_two_trainers():
    schedule, _, _ = _get_schedule()
    for entry in schedule:
        assert len(entry["trainers"]) == 2


def test_trainers_available_both_days():
    from scheduler import parse_availability, generate_slots, schedule_optimal
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    schedule = schedule_optimal(dates, trainers, slots, config=CONFIG)
    for entry in schedule:
        d1, d2 = entry["slot"]
        for name in entry["trainers"]:
            assert trainers[name].get(d1, False)
            assert trainers[name].get(d2, False)


def test_no_trainer_double_booked():
    from scheduler import parse_availability, generate_slots, schedule_optimal
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    schedule = schedule_optimal(dates, trainers, slots, config=CONFIG)
    day_bookings = {}
    for entry in schedule:
        d1, d2 = entry["slot"]
        for name in entry["trainers"]:
            assert name not in day_bookings.get(d1, set())
            assert name not in day_bookings.get(d2, set())
            day_bookings.setdefault(d1, set()).add(name)
            day_bookings.setdefault(d2, set()).add(name)


def test_experience_rules_enforced():
    schedule, _, _ = _get_schedule()
    for entry in schedule:
        names = set(entry["trainers"])
        assert names & CONFIG["experienced"], f"No experienced trainer in {entry['slot']}: {names}"
        for trainee in names & CONFIG["trainees"]:
            assert names & CONFIG["experienced"]


def test_optimal_finds_more_than_greedy():
    """Solver should find at least as many bootcamps as greedy (often more)."""
    from scheduler import parse_availability, generate_slots, schedule_greedy, schedule_optimal
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    greedy = schedule_greedy(dates, trainers, slots, config=CONFIG)
    optimal = schedule_optimal(dates, trainers, slots, config=CONFIG)
    assert len(optimal) >= len(greedy), \
        f"Solver ({len(optimal)}) found fewer bootcamps than greedy ({len(greedy)})"


def test_optimal_finds_at_least_five_bootcamps():
    schedule, _, _ = _get_schedule()
    assert len(schedule) >= 5
