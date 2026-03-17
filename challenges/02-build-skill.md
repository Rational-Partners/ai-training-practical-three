# Challenge 2: Build a Build Skill

## What You're Doing

Now you need a skill that takes a spec and produces working, tested code. This is your `/build` skill.

## What Makes a Good Build Skill

A naive build skill says "implement this". A good one:

1. **Reads the spec** — references `specs/current.md` throughout
2. **Plans before coding** — outlines the functions/classes it will write and why, before touching any file
3. **Respects what exists** — looks at `scheduler.py` to understand what's already there, never breaks existing functions
4. **Follows engineering standards** — uses type hints, handles errors at boundaries, keeps functions small and pure where possible
5. **Verifies with tests** — runs `python3 -m pytest tests/ -v` after implementing, fixes failures before reporting done
6. **Reports clearly** — tells you what was built, what the tests show, and anything to watch out for

## Structure to Aim For

A production build skill typically works in phases:

1. **Pre-flight** — Read the spec. Read the current `scheduler.py`. Identify what already exists. Note which tests will verify the new work.
2. **Plan** — Write out the functions to create, their signatures, and how they interact. Do this *before touching any file*.
3. **Implement** — Write the code, keeping functions small and testable.
4. **Verify** — Run `python3 -m pytest tests/ -v`. If tests fail, read the failure, fix the code, and re-run. Don't report done until tests pass.
5. **Report** — State what was built, what the tests show, and any tradeoffs or assumptions made.

Look at `.claude/commands/next.md` in this repo — it's already a working command. Notice how it reads files, applies logic, and produces structured output. A build skill is similar but longer.

You can also look at how Claude Code's own documentation describes good system prompts for coding agents. The principle: *be explicit about what to check, when to stop, and what "done" means*.

## Where to Put It

Create `.claude/commands/build.md`. Same pattern as your spec command.

Think carefully about:
- What should it check before writing any code?
- How should it communicate its plan before executing?
- What should happen if tests fail?
- How should it handle a vague or incomplete spec?

## Tests

No automated tests. Your acceptance criterion: run `/build` after speccing the availability parser (Challenge 3). If it produces working code that passes `tests/test_01_availability.py` without you having to intervene — your skill is good.
