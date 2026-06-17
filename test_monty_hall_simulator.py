"""Tests for the Monty Hall simulator."""

import unittest

from monty_hall_simulator import SimulationResult, play_round, run_simulation


class MontyHallSimulatorTests(unittest.TestCase):
    def test_run_simulation_requires_positive_trials(self) -> None:
        with self.assertRaises(ValueError):
            run_simulation(trials=0, strategy="switch", seed=42)

    def test_invalid_strategy_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            # type: ignore[arg-type]
            run_simulation(trials=10, strategy="invalid", seed=42)

    def test_result_win_rate_calculation(self) -> None:
        result = SimulationResult(strategy="switch", trials=4, wins=3)
        self.assertEqual(result.win_rate, 75.0)

    def test_switch_strategy_wins_more_often_than_stay_strategy(self) -> None:
        switch_result = run_simulation(trials=20_000, strategy="switch", seed=7)
        stay_result = run_simulation(trials=20_000, strategy="stay", seed=7)

        self.assertGreater(switch_result.win_rate, 60.0)
        self.assertLess(stay_result.win_rate, 40.0)
        self.assertGreater(switch_result.win_rate, stay_result.win_rate)

    def test_single_round_returns_boolean(self) -> None:
        import random

        result = play_round(strategy="switch", rng=random.Random(1))
        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
