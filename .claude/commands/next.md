---
description: Show the next challenge to work on based on current progress. Use when the student wants to know where they are or what to do next.
---

Check the student's current progress and show them exactly what to do next.

## How to determine progress

**Step 1 — Check for meta-skills (challenges 1 and 2)**

Read `.claude/commands/` to check which commands exist:
- `spec.md` present → Challenge 1 complete
- `build.md` present → Challenge 2 complete

**Step 2 — Check scheduler.py for implemented functions**

Read `scheduler.py` and look for these function definitions (in order):

| Function | Challenge complete |
|----------|-------------------|
| `def parse_availability` | Challenge 3 |
| `def generate_slots` | Challenge 4 |
| `def schedule_greedy` | Challenge 5 |
| `schedule_greedy` body references `config` or `experienced` | Challenge 6 |
| `def schedule_optimal` | Challenge 7 |
| `def parse_availability` returns 4 values (check for `trainer_info` usage) | Challenge 8 |
| `def parse_locations` | Challenge 9 |
| `def apply_bank_holidays` | Challenge 10 |

Work through the list top to bottom. The first one that's missing is the next challenge.

## What to output

1. A clear status summary — which challenges are done (✓) and which aren't yet
2. The next challenge: its number, title, and one sentence on what to build
3. The exact command to read the challenge file:
   `Ask Claude: "Read challenges/NN-name.md and explain what I need to build"`
4. If challenges 1 or 2 are next: remind them that the output is a new file in `.claude/commands/`, not content added to CLAUDE.md
5. If all 10 are done: congratulate them and suggest running `python3 -m pytest tests/ -v` for the final check

Keep the output tight — status list + next action. Don't describe all the remaining challenges.
