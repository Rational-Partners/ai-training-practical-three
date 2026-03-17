"""Tests for Challenge 8: full system — bank holidays, weightings, travel penalties"""
import pytest
from datetime import date
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ADVANCED_XLSX = os.path.join(DATA_DIR, "advanced.xlsx")


def test_good_friday_blocks_london_trainer():
    """Alice Chen (London) should not be assignable on Good Friday (3 Apr 2026)."""
    from scheduler import apply_bank_holidays, parse_availability
    dates, trainers, trainer_info, _ = parse_availability(ADVANCED_XLSX)
    # Force Alice available on Good Friday before bank holiday blocking
    trainers["Alice Chen"][date(2026, 4, 3)] = True
    apply_bank_holidays(trainers, trainer_info)
    assert trainers["Alice Chen"][date(2026, 4, 3)] is False, \
        "Alice (London/UK) should be blocked on Good Friday"


def test_good_friday_does_not_block_paris_trainer():
    """Diana Müller (Paris) should not be affected by UK Good Friday."""
    from scheduler import apply_bank_holidays, parse_availability
    dates, trainers, trainer_info, _ = parse_availability(ADVANCED_XLSX)
    trainers["Diana Müller"][date(2026, 4, 3)] = True
    apply_bank_holidays(trainers, trainer_info)
    # Good Friday is not a public holiday in France (outside Alsace-Lorraine)
    assert trainers["Diana Müller"][date(2026, 4, 3)] is True, \
        "Diana (Paris/France) should not be blocked on UK Good Friday"


def test_parse_weightings():
    from scheduler import parse_weightings
    weightings = parse_weightings(ADVANCED_XLSX)
    assert isinstance(weightings, dict)
    assert len(weightings) > 0
    for name, weight in weightings.items():
        assert isinstance(weight, (int, float))


def test_alice_has_highest_weight():
    from scheduler import parse_weightings
    weightings = parse_weightings(ADVANCED_XLSX)
    assert "Alice Chen" in weightings
    max_weight = max(weightings.values())
    assert weightings["Alice Chen"] == max_weight


def test_full_schedule_runs_without_error():
    """Full pipeline with all features should run and return a schedule."""
    from scheduler import (parse_availability, generate_slots, schedule_optimal,
                           parse_locations, parse_weightings, apply_bank_holidays)
    dates, trainers, trainer_info, weekly_caps = parse_availability(ADVANCED_XLSX)
    apply_bank_holidays(trainers, trainer_info)
    slots = generate_slots(dates, trainers)
    locations = parse_locations(ADVANCED_XLSX)
    weightings = parse_weightings(ADVANCED_XLSX)
    config = {
        "experienced": {"Alice Chen", "Bob Smith", "Diana Müller"},
        "trainees": {"Carol Jones"},
    }
    schedule = schedule_optimal(
        dates, trainers, slots,
        config=config,
        trainer_info=trainer_info,
        weekly_caps=weekly_caps,
        locations=locations,
        weightings=weightings,
    )
    assert isinstance(schedule, list)
    assert len(schedule) > 0
