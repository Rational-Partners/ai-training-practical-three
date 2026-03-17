# Challenge 8: Caps and Limits

## New Data

Switch to `data/intermediate.xlsx`. Open it and examine the extra columns.

New columns in the Availability sheet: **Home Location**, **French**, **Max/Week**.

There's also a **cap row** — the first row with a blank name — containing numbers on Monday columns. These are per-week bootcamp limits.

## Two New Constraints

**Per-trainer weekly cap**: `Max/Week = 2` means at most 2 days per week, so at most 1 bootcamp per week for that trainer.

**Per-week total cap**: The cap row number for a given Monday = maximum bootcamps allowed that calendar week across all slots.

## What to Build

1. Update `parse_availability(filepath)` to return a 4-tuple: `(dates, trainers, trainer_info, weekly_caps)` when extra columns are present. `trainer_info` maps trainer name → `{home_location, french_speaking, max_per_week}`.

2. Update `schedule_optimal(...)` to accept `trainer_info=None, weekly_caps=None` and enforce both caps when provided.

## Note on Backwards Compatibility

`basic.xlsx` has no extra columns. `parse_availability` should handle both formats — returning `({}, {})` for trainer_info and weekly_caps when the columns aren't there.

## Tests

```bash
python3 -m pytest tests/test_06_caps.py -v
```
