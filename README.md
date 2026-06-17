# Monty Hall Simulator

A small, testable Python simulation of the classic Monty Hall probability problem. The project is designed as a clean portfolio example for algorithmic thinking, statistical simulation, command-line tooling, and automated validation.

## What it demonstrates

- Monte Carlo simulation using Python standard library tools
- Clear separation between simulation logic and command-line execution
- Reproducible runs through deterministic random seeds
- Lightweight automated tests using `unittest`
- Simple CI validation through GitHub Actions

## Why this project matters

The Monty Hall problem is a useful way to demonstrate how intuition can be tested with data. In the simulation, the player either keeps the original door choice or switches after the host reveals a losing door. Over many trials, switching should win about two-thirds of the time, while staying should win about one-third of the time.

For a software engineering portfolio, this project shows the ability to turn a business or teaching question into executable logic, measurable output, and repeatable validation.

## Run locally

```bash
python monty_hall_simulator.py --trials 10000 --strategy switch --seed 42
python monty_hall_simulator.py --trials 10000 --strategy stay --seed 42
```

Example output:

```text
Strategy: switch
Trials: 10000
Wins: 6635
Win rate: 66.35%
```

## Run tests

```bash
python -m unittest discover -v
```

## Project structure

```text
.
|-- monty_hall_simulator.py          # Simulation logic and CLI entry point
|-- test_monty_hall_simulator.py     # Unit tests
`-- .github/workflows/python-tests.yml
```

## Portfolio positioning

This repository is intentionally small. It is meant to be easy for a recruiter, hiring manager, or technical reviewer to scan quickly while still showing clean code structure, repeatable results, and basic automated validation.

## Author

James Allendoerfer  
Senior Integration Developer | Oracle PL/SQL | Backend Systems | Data Engineering | Adjunct Faculty
