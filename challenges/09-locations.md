# Challenge 9: Location Awareness

## New Data

Switch to `data/advanced.xlsx`. There's a **Locations** sheet.

Open it. Each row is a location with: Name, Country, Demand, French Required, Max Parallel.

## The New Problem

Instead of just filling slots, you're now scheduling to meet demand. Each location needs a certain number of bootcamps. Paris requires at least one French-speaking trainer per bootcamp.

## What to Build

1. `parse_locations(filepath)` — reads the Locations sheet, returns a list of location dicts

2. Update `schedule_optimal(...)` to accept `locations=None`. When provided:
   - Assign each bootcamp to a location
   - Enforce the French-speaking constraint
   - Optimise to meet demand (credit stops at demand — going over doesn't help)

## Questions for Your Spec

- What does the output look like when each bootcamp has a location? (Add `"location"` key to each dict)
- How does CP-SAT model "assign bootcamp to location"?
- What's the new objective function?

## Tests

```bash
python3 -m pytest tests/test_07_locations.py -v
```
