"""Tests for Challenge 3: schedule_greedy"""
import pytest
from datetime import date
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
BASIC_XLSX = os.path.join(DATA_DIR, "basic.xlsx")


def _get_schedule():
    from scheduler import parse_availability, generate_slots, schedule_greedy
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    return schedule_greedy(dates, trainers, slots), trainers, slots


def test_returns_list_of_dicts():
    schedule, _, _ = _get_schedule()
    assert isinstance(schedule, list)
    for entry in schedule:
        assert "slot" in entry
        assert "trainers" in entry


def test_each_bootcamp_has_two_trainers():
    schedule, _, _ = _get_schedule()
    for entry in schedule:
        assert len(entry["trainers"]) == 2, f"Bootcamp {entry['slot']} has {len(entry['trainers'])} trainers"


def test_trainers_available_on_both_days():
    from scheduler import parse_availability, generate_slots, schedule_greedy
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    schedule = schedule_greedy(dates, trainers, slots)
    for entry in schedule:
        d1, d2 = entry["slot"]
        for name in entry["trainers"]:
            assert trainers[name].get(d1, False), f"{name} not available on {d1}"
            assert trainers[name].get(d2, False), f"{name} not available on {d2}"


def test_no_trainer_double_booked():
    from scheduler import parse_availability, generate_slots, schedule_greedy
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    schedule = schedule_greedy(dates, trainers, slots)
    # Build day -> set of trainers
    day_bookings = {}
    for entry in schedule:
        d1, d2 = entry["slot"]
        for name in entry["trainers"]:
            assert name not in day_bookings.get(d1, set()), f"{name} double-booked on {d1}"
            assert name not in day_bookings.get(d2, set()), f"{name} double-booked on {d2}"
            day_bookings.setdefault(d1, set()).add(name)
            day_bookings.setdefault(d2, set()).add(name)


def test_schedules_at_least_four_bootcamps():
    schedule, _, _ = _get_schedule()
    assert len(schedule) >= 4, f"Only scheduled {len(schedule)} bootcamps — greedy should find at least 4"
