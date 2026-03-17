"""Tests for Challenge 2: generate_slots"""
import pytest
from datetime import date
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
BASIC_XLSX = os.path.join(DATA_DIR, "basic.xlsx")


def test_slots_are_tuples_of_date_pairs():
    """Each slot should be a (date, date) tuple."""
    from scheduler import parse_availability, generate_slots
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    assert isinstance(slots, list)
    for slot in slots:
        assert isinstance(slot, tuple)
        assert len(slot) == 2
        assert isinstance(slot[0], date)
        assert isinstance(slot[1], date)


def test_slots_follow_mon_tue_thu_fri_pattern():
    """All slots should be Mon-Tue or Thu-Fri pairs."""
    from scheduler import parse_availability, generate_slots
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    for d1, d2 in slots:
        assert (d1.weekday(), d2.weekday()) in [(0, 1), (3, 4)], \
            f"Slot {d1}–{d2} is not Mon-Tue or Thu-Fri"


def test_each_slot_has_at_least_two_trainers_available():
    """Each slot must have at least 2 trainers available on both days."""
    from scheduler import parse_availability, generate_slots
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    for d1, d2 in slots:
        available_both = [
            name for name, avail in trainers.items()
            if avail.get(d1, False) and avail.get(d2, False)
        ]
        assert len(available_both) >= 2, \
            f"Slot {d1}–{d2} has only {len(available_both)} trainers available both days"


def test_week1_mon_tue_slot_exists():
    """Mon 16 Mar – Tue 17 Mar should be a valid slot."""
    from scheduler import parse_availability, generate_slots
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    assert (date(2026, 3, 16), date(2026, 3, 17)) in slots


def test_week3_thu_fri_not_a_slot():
    """Thu 2 Apr – Fri 3 Apr (Good Friday) should NOT be valid — only Diana available both days."""
    from scheduler import parse_availability, generate_slots
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    assert (date(2026, 4, 2), date(2026, 4, 3)) not in slots


def test_pattern_filter_mon_tue_only():
    """When pattern='mon-tue', only Mon-Tue slots returned."""
    from scheduler import parse_availability, generate_slots
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers, pattern="mon-tue")
    for d1, d2 in slots:
        assert d1.weekday() == 0, f"Slot starts on {d1.strftime('%A')}, not Monday"
        assert d2.weekday() == 1


def test_seven_total_slots():
    """Should find exactly 7 valid slots across 4 weeks."""
    from scheduler import parse_availability, generate_slots
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    assert len(slots) == 7
