# Challenge 6: Experience Rules

## What to Add

Update your scheduler to enforce trainer experience levels, passed in via `config`:

```python
config = {
    "experienced": {"Alice Chen", "Bob Smith", "Diana Müller"},
    "trainees": {"Carol Jones"},
    # Eve Brown — no category, can pair with anyone
}
```

## The Rules

1. Every bootcamp must have at least one experienced trainer
2. A trainee can only be assigned alongside an experienced trainer

## What This Reveals

With these rules, the Mon 6 Apr – Tue 7 Apr slot (week 4) can't be scheduled — only Carol (trainee) and Eve (uncategorised) are available that week. Neither satisfies rule 1. The greedy scheduler should skip it.

## How to Work

Update `schedule_greedy` (or write `schedule_with_experience` — let your spec decide).

1. `/spec` it
2. `/build` it
3. Verify

## Tests

```bash
python3 -m pytest tests/test_04_experience.py -v
```
