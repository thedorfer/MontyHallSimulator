"""Monty Hall simulation.

This module provides a small, testable implementation of the classic
Monty Hall probability problem. It can be imported by tests or executed
as a command-line program.
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from typing import Literal

Strategy = Literal["stay", "switch"]


@dataclass(frozen=True)
class SimulationResult:
    """Summary of a simulation run."""

    strategy: Strategy
    trials: int
    wins: int

    @property
    def win_rate(self) -> float:
        """Return the win rate as a percentage."""
        if self.trials == 0:
            return 0.0
        return (self.wins / self.trials) * 100


def play_round(strategy: Strategy, rng: random.Random) -> bool:
    """Play a single Monty Hall round.

    Args:
        strategy: Either "stay" to keep the first choice or "switch" to
            change to the remaining unopened door.
        rng: Random number generator used for deterministic tests/runs.

    Returns:
        True if the player wins the car; otherwise False.
    """
    if strategy not in {"stay", "switch"}:
        raise ValueError("strategy must be either 'stay' or 'switch'")

    doors = [0, 1, 2]
    car = rng.choice(doors)
    first_choice = rng.choice(doors)

    # The host opens a goat door that was not selected by the player.
    available_goat_doors = [door for door in doors if door != first_choice and door != car]
    host_opens = rng.choice(available_goat_doors)

    if strategy == "stay":
        final_choice = first_choice
    else:
        final_choice = next(door for door in doors if door not in {first_choice, host_opens})

    return final_choice == car


def run_simulation(trials: int, strategy: Strategy, seed: int | None = None) -> SimulationResult:
    """Run a Monty Hall simulation for the requested number of trials."""
    if trials < 1:
        raise ValueError("trials must be greater than zero")

    rng = random.Random(seed)
    wins = sum(play_round(strategy, rng) for _ in range(trials))
    return SimulationResult(strategy=strategy, trials=trials, wins=wins)


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(description="Run a Monty Hall probability simulation.")
    parser.add_argument("--trials", type=int, default=10_000, help="Number of trials to run.")
    parser.add_argument(
        "--strategy",
        choices=["stay", "switch"],
        default="switch",
        help="Player strategy to simulate.",
    )
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed for reproducible output.")
    return parser


def main() -> None:
    """Run the command-line program."""
    args = build_parser().parse_args()
    result = run_simulation(trials=args.trials, strategy=args.strategy, seed=args.seed)

    print(f"Strategy: {result.strategy}")
    print(f"Trials: {result.trials}")
    print(f"Wins: {result.wins}")
    print(f"Win rate: {result.win_rate:.2f}%")


if __name__ == "__main__":
    main()
