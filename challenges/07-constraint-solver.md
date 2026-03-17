# Challenge 7: Replace Greedy with CP-SAT

## The Problem with Greedy

Greedy assigns the first valid pair for each slot. This can block better assignments later. Consider:

- Alice is the only experienced trainer available for Thu–Fri week 1
- Greedy assigns Alice to Mon–Tue week 1 (valid, first available)
- Now Thu–Fri week 1 has no experienced trainer — slot is skipped
- An optimal solver would have assigned Bob to Mon–Tue, preserving Alice for Thu–Fri

The optimal solver finds the globally best assignment.

## CP-SAT Basics

Google OR-Tools CP-SAT:

```python
from ortools.sat.python import cp_model

model = cp_model.CpModel()
solver = cp_model.CpSolver()

# Boolean variable: is trainer t assigned to slot s?
x = model.new_bool_var("x_t_s")

# Constraint: sum of assignments <= cap
model.add(sum(vars) <= cap)

# Objective: maximise total bootcamps
model.maximize(sum(slot_active_vars))

status = solver.solve(model)
solver.value(x)  # 0 or 1
```

## What to Build

`schedule_optimal(dates, trainers, slots, config=None)` — same interface as `schedule_greedy`, uses CP-SAT internally.

Key modelling decisions for your spec:
- How do you model "slot is scheduled or not"?
- How do you enforce "exactly 2 trainers per scheduled slot"?
- How do you encode the experience rules?

Set `solver.parameters.max_time_in_seconds = 30`.

## Tests

```bash
python3 -m pytest tests/test_05_solver.py -v
```
