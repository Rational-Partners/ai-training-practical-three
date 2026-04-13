---
description: Read specs/current.md and implement the specified function in scheduler.py using a 5-phase approach
---

You are a builder. Your job is to take a specification from `specs/current.md` and produce working, tested code in `scheduler.py`.

Work through these 5 phases in order. Do not skip phases.

## Phase 1: Pre-flight

1. Read `specs/current.md` — this is your source of truth for what to build
2. Read `scheduler.py` — understand what functions already exist. You must NOT break or remove any existing function
3. Read the test files in `tests/` that will verify the new work
4. Read the relevant data files from `data/` if the spec references them
5. If the spec is missing or empty, STOP and tell the user to run `/spec` first

## Phase 2: Plan

Before writing any code, outline your plan:

1. List the functions you will create or modify, with their signatures and type hints
2. Describe how each function works at a high level
3. Note how new functions interact with existing ones
4. Identify any helper functions needed
5. State which tests you expect to pass after implementation

Present this plan to the user. Keep it concise — function signatures + one line each.

## Phase 3: Implement

Write the code in `scheduler.py`:

1. Add new functions below existing ones — never insert code that breaks existing functions
2. Use type hints on all function signatures
3. Keep functions small and pure where possible — each function should do one thing
4. Follow the patterns already established in `scheduler.py`
5. Import any new libraries at the top of the file
6. Do not add unnecessary comments — clear code is better than commented code

## Phase 4: Verify

Run the tests and iterate until they pass:

1. Run `.venv/bin/python3 -m pytest tests/ -v`
2. If tests fail: read the failure message, diagnose the issue, fix the code, re-run
3. Repeat until ALL tests pass (not just the new ones — never break existing tests)
4. Do NOT report success until all tests pass

## Phase 5: Report

Summarize what was done:

1. What functions were built or modified
2. Test results (which tests pass, total count)
3. Any tradeoffs, assumptions, or decisions made during implementation
4. Anything the user should know for the next challenge

Keep the report concise.

$ARGUMENTS
