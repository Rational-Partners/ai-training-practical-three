"""Tests for Challenge 1: parse_availability"""
import pytest
from datetime import date
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
BASIC_XLSX = os.path.join(DATA_DIR, "basic.xlsx")


def test_returns_dates_and_trainers():
    """parse_availability returns a tuple starting with (dates, trainers).

    Later challenges extend the return to a 4-tuple — so we check len >= 2.
    """
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    assert isinstance(result, tuple)
    assert len(result) >= 2


def test_dates_are_sorted_date_objects():
    """dates is a sorted list of date objects."""
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    dates = result[0]
    assert len(dates) > 0
    for d in dates:
        assert isinstance(d, date)
    assert dates == sorted(dates)


def test_correct_number_of_dates():
    """Should have 20 dates — 4 weeks x 5 working days."""
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    dates = result[0]
    assert len(dates) == 20


def test_five_trainers():
    """Should have 5 trainers."""
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    trainers = result[1]
    assert len(trainers) == 5


def test_trainer_names_present():
    """Known trainer names should be in the result."""
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    trainers = result[1]
    assert "Alice Chen" in trainers
    assert "Bob Smith" in trainers


def test_availability_values_are_booleans():
    """Availability values should be True/False."""
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    dates, trainers = result[0], result[1]
    for name, avail in trainers.items():
        for d in dates:
            assert isinstance(avail[d], bool), f"{name} on {d} is not bool"


def test_alice_available_monday_week1():
    """Alice Chen should be available on Mon 16 Mar 2026."""
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    trainers = result[1]
    assert trainers["Alice Chen"][date(2026, 3, 16)] is True


def test_carol_not_available_monday_week1():
    """Carol Jones should NOT be available on Mon 16 Mar 2026."""
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    trainers = result[1]
    assert trainers["Carol Jones"][date(2026, 3, 16)] is False


def test_all_dates_in_trainer_availability():
    """Every date should appear in every trainer's availability dict."""
    from scheduler import parse_availability
    result = parse_availability(BASIC_XLSX)
    dates, trainers = result[0], result[1]
    for name, avail in trainers.items():
        for d in dates:
            assert d in avail, f"{name} missing date {d}"
