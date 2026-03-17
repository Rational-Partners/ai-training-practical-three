"""Tests for Challenge 7: location awareness"""
import pytest
from datetime import date
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ADVANCED_XLSX = os.path.join(DATA_DIR, "advanced.xlsx")

CONFIG = {
    "experienced": {"Alice Chen", "Bob Smith", "Diana Müller"},
    "trainees": {"Carol Jones"},
}


def test_parse_locations_returns_list():
    from scheduler import parse_locations
    locations = parse_locations(ADVANCED_XLSX)
    assert isinstance(locations, list)
    assert len(locations) > 0


def test_locations_have_required_fields():
    from scheduler import parse_locations
    locations = parse_locations(ADVANCED_XLSX)
    for loc in locations:
        assert "name" in loc
        assert "country" in loc
        assert "demand" in loc
        assert "french_required" in loc


def test_paris_requires_french():
    from scheduler import parse_locations
    locations = parse_locations(ADVANCED_XLSX)
    paris = next(l for l in locations if l["name"] == "Paris")
    assert paris["french_required"] is True


def test_london_does_not_require_french():
    from scheduler import parse_locations
    locations = parse_locations(ADVANCED_XLSX)
    london = next(l for l in locations if l["name"] == "London")
    assert london["french_required"] is False


def test_french_location_bootcamps_have_french_speaker():
    from scheduler import parse_availability, generate_slots, schedule_optimal, parse_locations
    dates, trainers, trainer_info, weekly_caps = parse_availability(ADVANCED_XLSX)
    slots = generate_slots(dates, trainers)
    locations = parse_locations(ADVANCED_XLSX)
    schedule = schedule_optimal(dates, trainers, slots, config=CONFIG,
                                trainer_info=trainer_info, weekly_caps=weekly_caps,
                                locations=locations)
    for entry in schedule:
        loc = entry.get("location")
        if loc:
            loc_data = next((l for l in locations if l["name"] == loc), None)
            if loc_data and loc_data["french_required"]:
                french_speakers = {name for name in entry["trainers"]
                                   if trainer_info.get(name, {}).get("french_speaking", False)}
                assert french_speakers, \
                    f"Bootcamp at {loc} has no French speaker: {entry['trainers']}"
