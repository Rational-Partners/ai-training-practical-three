"""Tests for Challenge 4: experience rules"""
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
    from scheduler import parse_availability, generate_slots, schedule_greedy
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    return schedule_greedy(dates, trainers, slots, config=CONFIG), trainers


def test_every_bootcamp_has_experienced_trainer():
    schedule, _ = _get_schedule()
    for entry in schedule:
        names = set(entry["trainers"])
        exp_in_bootcamp = names & CONFIG["experienced"]
        assert exp_in_bootcamp, \
            f"Bootcamp {entry['slot']} has no experienced trainer: {names}"


def test_trainee_always_paired_with_experienced():
    schedule, _ = _get_schedule()
    for entry in schedule:
        names = set(entry["trainers"])
        trainees_in_bootcamp = names & CONFIG["trainees"]
        if trainees_in_bootcamp:
            exp_in_bootcamp = names & CONFIG["experienced"]
            assert exp_in_bootcamp, \
                f"Trainee in {entry['slot']} not paired with experienced: {names}"


def test_no_experience_config_runs_normally():
    """With no config, should still schedule bootcamps (no experience constraints)."""
    from scheduler import parse_availability, generate_slots, schedule_greedy
    dates, trainers = parse_availability(BASIC_XLSX)
    slots = generate_slots(dates, trainers)
    schedule = schedule_greedy(dates, trainers, slots)
    assert len(schedule) >= 4
