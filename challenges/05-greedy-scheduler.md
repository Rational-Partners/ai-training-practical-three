# Challenge 5: Greedy Scheduler

## What to Build

A function `schedule_greedy(dates, trainers, slots, config=None)` that assigns trainer pairs to slots.

## The Algorithm

For each slot in order:
1. Find trainers available on both days of the slot who haven't been booked on those days
2. If 2 or more are available, assign the first 2
3. Otherwise, skip the slot

## Rules

1. Exactly 2 trainers per bootcamp
2. A trainer can only work one bootcamp per day
3. Both trainers must be available on both days

## Output

```python
[
    {"slot": (date(...), date(...)), "trainers": ["Alice Chen", "Bob Smith"]},
    ...
]
```

## How to Work

1. `/spec` it — think carefully about what "first 2" means and how to track bookings
2. `/build` it
3. Verify

## Tests

```bash
python3 -m pytest tests/test_03_greedy.py -v
```
