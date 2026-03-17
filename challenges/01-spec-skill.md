# Challenge 1: Build a Spec Skill

## What You're Doing

Before writing any code, you need a tool for thinking clearly about what to build. Your first task is to write a `/spec` skill — a Claude Code command that helps you write high-quality technical specifications.

This is a meta-challenge: you're building a tool you'll use for everything else.

## What Makes a Good Spec

A spec that just says "parse the Excel file and return availability" isn't useful. A good spec has:

- **Inputs** — exact data types, shapes, file formats, optional vs required
- **Outputs** — what is returned, in what format, with what guarantees
- **Rules** — numbered, testable constraints that must always hold
- **Acceptance criteria** — specific statements that can be checked: "given X, the result must be Y"
- **Test cases** — at least 3 concrete examples with real data from `data/basic.xlsx`
- **Edge cases** — what happens with blank cells, unknown trainers, empty files
- **Engineering notes** — performance, error handling, library choices worth noting

## The Skill Should Interview You

A good spec skill doesn't just ask "what do you want?" It asks targeted questions that surface things you haven't thought about yet. It should produce a spec good enough that you could hand it to another developer and they'd build exactly the right thing.

## Where to Put It

Create `.claude/commands/spec.md`. This file becomes the `/spec` command automatically — no registration needed.

```
.claude/
  commands/
    spec.md    ← your new command
    next.md    ← already exists
```

The CLAUDE.md explains the file format. YAML frontmatter is optional but a `description` field helps Claude know when to suggest it.

Think carefully about:
- What questions should it ask, and in what order?
- How does it handle vague or incomplete answers?
- What sections should the output spec always have?

## How to Know It's Working

Run `/spec` and describe the availability parser (Challenge 3 tells you what it does). Review `specs/current.md` — if it has enough detail that Claude could implement it correctly without asking further questions, your skill is good.

## See an Example

`specs/example.md` shows what a solid spec looks like.

## Tests

No automated tests. Your acceptance criterion: the spec produced is good enough to drive a correct implementation in Challenge 3.
