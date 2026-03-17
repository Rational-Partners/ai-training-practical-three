# Challenge 4: Find Valid Time Slots

## What to Build

A function `generate_slots(dates, trainers, pattern="mon-tue,thu-fri")` that identifies valid bootcamp time windows.

## The Concept

A bootcamp is 2 consecutive working days. We only run bootcamps on specific day patterns:
- **Mon–Tue** (weekday 0 + 1)
- **Thu–Fri** (weekday 3 + 4)

A slot is valid only if at least 2 trainers are available on **both** days.

## Interesting Edge

Week 3 Thu–Fri (2 Apr – 3 Apr 2026) has Good Friday on the 3rd. Only one trainer marks herself available on both days. Your function should correctly classify this as an invalid slot.

## How to Work

1. `/spec` it
2. Review the spec
3. `/build` it
4. Verify

## Tests

```bash
python3 -m pytest tests/test_02_slots.py -v
```
