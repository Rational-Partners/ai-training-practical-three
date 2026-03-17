# Challenge 3: Availability Parser

## What to Build

A function `parse_availability(filepath)` that reads `data/basic.xlsx` and returns who is available on each date.

## The Data

Open `data/basic.xlsx` and look at it. The Availability sheet has:
- Row 1: header with date strings (`"2026-03-16"`, `"2026-03-17"`, ...)
- Column A: trainer name
- Other cells: `"Yes"` when available, empty when not

There are 5 trainers and 20 working days (4 weeks of Mon–Fri).

## How to Work

1. Run `/spec` to write a spec for this function
2. Review `specs/current.md` — edit it until you're happy with it
3. Run `/build` to implement from the spec
4. Run `python3 -m pytest tests/test_01_availability.py -v` to verify

## What the Tests Expect

The function should return a tuple where:
- First element (`dates`): a sorted list of `date` objects
- Second element (`trainers`): `dict[str, dict[date, bool]]` — for each trainer, for each date, whether they're available

A 2-tuple `(dates, trainers)` is correct for now. Challenge 8 will extend this to a 4-tuple — the tests are written to handle both.

## Tests

```bash
python3 -m pytest tests/test_01_availability.py -v
```
