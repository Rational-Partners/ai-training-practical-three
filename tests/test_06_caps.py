"""Tests for Challenge 6: caps and limits"""
import pytest
from datetime import date
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
INTERMEDIATE_XLSX = os.path.join(DATA_DIR, "intermediate.xlsx")

CONFIG = {
    "experienced": {"Alice Chen", "Bob Smith", "Diana Müller"},
    "trainees": {"Carol Jones"},
}


def test_parse_returns_trainer_info():
    """parse_availability on intermediate.xlsx returns trainer info including max_per_week."""
    from scheduler import parse_availability
    result = parse_availability(INTERMEDIATE_XLSX)
    # Should now return 4 values
    assert len(result) == 4
    dates, trainers, trainer_info, weekly_caps = result
    assert "Alice Chen" in trainer_info
    assert "home_location" in trainer_info["Alice Chen"]
    assert "french_speaking" in trainer_info["Alice Chen"]
    assert "max_per_week" in trainer_info["Alice Chen"]


def test_bob_has_max_2_days_per_week():
    from scheduler import parse_availability
    _, _, trainer_info, _ = parse_availability(INTERMEDIATE_XLSX)
    assert trainer_info["Bob Smith"]["max_per_week"] == 2


def test_weekly_caps_parsed():
    from scheduler import parse_availability
    _, _, _, weekly_caps = parse_availability(INTERMEDIATE_XLSX)
    assert len(weekly_caps) > 0
    for key, val in weekly_caps.items():
        iso_year, iso_week = key
        assert isinstance(iso_year, int)
        assert isinstance(iso_week, int)
        assert isinstance(val, int)


def test_per_trainer_cap_respected():
    """Bob (max 2 days/week) should do at most 1 bootcamp per week."""
    from scheduler import parse_availability, generate_slots, schedule_optimal
    dates, trainers, trainer_info, weekly_caps = parse_availability(INTERMEDIATE_XLSX)
    slots = generate_slots(dates, trainers)
    schedule = schedule_optimal(dates, trainers, slots, config=CONFIG,
                                trainer_info=trainer_info, weekly_caps=weekly_caps)
    # Count Bob's bootcamps per ISO week
    bob_weeks = {}
    for entry in schedule:
        d1, _ = entry["slot"]
        if "Bob Smith" in entry["trainers"]:
            yr, wk, _ = d1.isocalendar()
            bob_weeks[(yr, wk)] = bob_weeks.get((yr, wk), 0) + 1
    for week, count in bob_weeks.items():
        assert count <= 1, f"Bob has {count} bootcamps in week {week} (max 1 due to 2-day cap)"


def test_weekly_cap_respected():
    """No week should exceed its total bootcamp cap."""
    from scheduler import parse_availability, generate_slots, schedule_optimal
    dates, trainers, trainer_info, weekly_caps = parse_availability(INTERMEDIATE_XLSX)
    slots = generate_slots(dates, trainers)
    schedule = schedule_optimal(dates, trainers, slots, config=CONFIG,
                                trainer_info=trainer_info, weekly_caps=weekly_caps)
    week_counts = {}
    for entry in schedule:
        d1, _ = entry["slot"]
        yr, wk, _ = d1.isocalendar()
        week_counts[(yr, wk)] = week_counts.get((yr, wk), 0) + 1
    for week_key, count in week_counts.items():
        cap = weekly_caps.get(week_key)
        if cap:
            assert count <= cap, f"Week {week_key} has {count} bootcamps but cap is {cap}"
