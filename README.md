# Bootcamp Scheduler — AI Development Practical

A hands-on practical where you build a real constraint optimisation system, step by step, using AI.

## Setting Up Your Computer

Before starting, you need Python and the project dependencies installed. **This is especially important on Windows**, where Python setup can be tricky.

Open Claude Code in this directory and give it this prompt:

> Check if my computer is set up for this practical. I need Python 3.10 or later. Check what Python versions I have installed. If I don't have one, install one for me. Then create a virtual environment using that Python version, activate it, and install the dependencies from requirements.txt. Run `python -m pytest tests/ -x` to verify everything is working — the tests should fail with import errors (that's expected, we haven't built anything yet). Tell me when I'm ready to go.

Claude will handle the rest — including downloading Python if needed, dealing with Windows PATH issues, and creating the virtual environment.

If you don't have Claude Code installed yet, run:
```bash
npm install -g @anthropic-ai/claude-code
```
This requires Node.js 18+. See [claude.ai/code](https://claude.ai/code) for details.

---

## The Scenario

You are building a scheduling tool for a training company. They run 2-day bootcamps and need to assign trainers from a pool, respecting availability, experience requirements, weekly limits, locations, and bank holidays.

The trainer availability comes in as Excel spreadsheets (in the `data/` folder). Your job is to turn that into an optimal schedule.

## The Method

This practical teaches a **spec-first** workflow — you describe *what* to build, and Claude builds it:

1. **Spec it** — Write a precise technical specification (you'll build a `/spec` command for this)
2. **Build it** — Prompt Claude to implement from your spec
3. **Test it** — Run the tests to verify it works
4. **Repeat** — Each challenge adds new requirements

## The Challenges

There are 10 challenges, getting progressively harder:

| # | Challenge | What You Build |
|---|-----------|---------------|
| 1 | Spec Skill | A `/spec` command that interviews you and writes a technical spec |
| 2 | Build Skill | A `/build` command that implements code from a spec |
| 3 | Availability Parser | Read trainer availability from Excel |
| 4 | Find Valid Slots | Generate valid 2-day bootcamp time slots |
| 5 | Greedy Scheduler | Assign trainers to slots greedily |
| 6 | Experience Rules | Ensure each bootcamp has an experienced trainer |
| 7 | Constraint Solver | Optimal scheduling using Google OR-Tools CP-SAT |
| 8 | Caps and Limits | Enforce per-trainer and weekly caps |
| 9 | Location Awareness | Assign bootcamps to locations with language requirements |
| 10 | Full System | Bank holidays, weightings, travel penalties — the lot |

Challenges 1–2 are about building your own tools. Challenges 3–10 are about using those tools to build the scheduler itself.

## Getting Started

Open Claude Code in this directory:

```bash
claude
```

Then type:

```
/next
```

This will show you your current progress and tell you exactly what to do next. **Use `/next` whenever you're unsure where you are.**

## Structure

```
challenges/     Ten progressively harder challenges
data/           Sample Excel input files (basic, intermediate, advanced)
specs/          Your specifications live here (example provided)
tests/          Tests that verify each challenge
scheduler.py    Your implementation (starts empty)
```

## Tips

- You don't need to be a Python expert — that's what Claude is for
- Talk to Claude in plain English. If something is too technical, ask it to explain more simply
- Every challenge has tests. If the tests pass, you've done it right
- Use `/next` to check your progress at any time
- If you get stuck on a challenge, read the challenge file in `challenges/` — it has all the details
