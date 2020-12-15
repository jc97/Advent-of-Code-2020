#!/usr/bin/env python
"""Advent of Code 2020 - Day 15 - Solution by Julian Knorr (git@jknorr.eu)"""
from typing import List


def elves_game(starting_numbers: List[int], end: int) -> int:
    game = starting_numbers.copy()
    n = len(starting_numbers) + 1
    while n <= end:
        last_number = game[n - 2]
        try:
            previous_occurrence_n = len(game) - 1 - game[-2::-1].index(last_number)
        except ValueError:
            previous_occurrence_n = None
            pass
        if previous_occurrence_n is None:
            game.append(0)
        else:
            game.append(n - previous_occurrence_n - 1)
        n += 1
    return game[-1]


if __name__ == '__main__':
    task1_solution = elves_game([5, 1, 9, 18, 13, 8, 0], 2020)
    print("Task 1: {:d}".format(task1_solution))
