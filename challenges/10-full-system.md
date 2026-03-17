# Challenge 10: Full Production System

## Three Final Features

Tackle each one separately: spec it, build it, test it, then move to the next.

---

### Feature A: Bank Holidays

The `holidays` library knows every country's public holidays:

```python
import holidays
uk = holidays.country_holidays("GB", years=2026)
date(2026, 4, 3) in uk  # True — Good Friday
```

A trainer's home country (from `trainer_info`) determines which holidays block them. You'll need a mapping from country names like `"UK"`, `"France"`, `"Netherlands"` to ISO codes (`"GB"`, `"FR"`, `"NL"`).

Implement `apply_bank_holidays(trainers, trainer_info)` — modifies `trainers` in place, setting availability to `False` on bank holidays for each trainer's home country.

### Feature B: Trainer Weightings

`data/advanced.xlsx` has a **Weightings** sheet. Implement `parse_weightings(filepath)` that returns `dict[str, int]`.

Add a soft preference to the CP-SAT objective: when two solutions have the same number of bootcamps, prefer the one that uses higher-weighted trainers more.

### Feature C: Travel Penalties

Long-haul travel (India, USA, Singapore, Australia, etc.) is expensive. Add a travel cost to the objective that penalises assigning a trainer to a location in a long-haul country.

The penalty should be soft: it nudges the solver to prefer local assignments but doesn't block them.

---

## Final Check

```bash
python3 -m pytest tests/ -v
```

All 46 tests should pass.

## Reflection

Look back at your `/spec` and `/build` skills. What would you change about them after using them 8 times? Edit them. They're yours.
