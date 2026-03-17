# Bootcamp Scheduler — AI Development Practical

A hands-on practical where you build a real constraint solver, step by step, using AI.

## The Goal

By the end, you'll have a working system that takes a spreadsheet of trainer availability and produces an optimal bootcamp schedule — handling experience requirements, weekly caps, location languages, bank holidays, and more.

## The Method

This practical teaches a *spec-first* workflow:

1. **Spec it** — Use `/spec` to write a precise technical specification
2. **Build it** — Prompt Claude to implement from your spec
3. **Test it** — Run the tests to verify it works
4. **Repeat** — Each challenge adds new requirements to your spec

The LLM does the heavy lifting. Your job is to describe *what* the system should do well enough that Claude can build it.

## Prerequisites

- **Python 3.10–3.12** — required for `ortools`. Python 3.13+ is not yet supported by OR-Tools.
- **Claude Code** — install with `npm install -g @anthropic/claude-code` (requires Node 18+)

## Setup

```bash
# Recommend using a virtualenv
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to Work

Open Claude Code in this directory:

```bash
claude
```

Then follow the challenges in order. Start with:

```
/next
```

## Structure

```
challenges/     Ten progressively harder challenges
data/           Sample Excel input files
specs/          Your specifications live here
tests/          Tests that verify each challenge
scheduler.py    Your implementation (starts empty)
```

## Starting Point

Run `/next` to see your first challenge.
