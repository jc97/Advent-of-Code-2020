#!/usr/bin/env python
"""Advent of Code 2020 - Day 10 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import List


def read_puzzle_file(filename: str) -> List[int]:
    file = open(filename, 'r')
    puzzle = []
    for line in file.readlines():
        puzzle.append(int(line))
    puzzle.sort()
    return puzzle


def puzzle_amend(puzzle: List[int]) -> None:
    puzzle.append(max(*puzzle) + 3)


def task1(puzzle: List[int]) -> int:
    current_adapter = 0
    joltage_differences_count = {1: 0, 2: 0, 3: 0}
    joltage_differences_count[puzzle[0]] += 1
    while current_adapter < len(puzzle) - 1:
        joltage_difference = puzzle[current_adapter + 1] - puzzle[current_adapter]
        if joltage_difference > 3:
            raise RuntimeError("Not solvable.")
        joltage_differences_count[joltage_difference] += 1
        current_adapter += 1
    return joltage_differences_count[1] * joltage_differences_count[3]


def task2(puzzle: List[int]) -> int:
    puzzle = [0] + puzzle
    possibilities = [0] * len(puzzle)
    possibilities[0] = 1
    for adapter in range(0, len(puzzle) - 1):
        for next_adapter in range(adapter + 1, adapter + 4):
            if next_adapter >= len(puzzle):
                break
            if puzzle[next_adapter] - puzzle[adapter] > 3:
                break
            possibilities[next_adapter] += possibilities[adapter]
    return possibilities[len(puzzle) - 1]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        puzzle_amend(puzzle_lines)
        task1_solution = task1(puzzle_lines)
        print("Task 1: {:d}".format(task1_solution))
        task2_solution = task2(puzzle_lines)
        print("Task 2: {:d}".format(task2_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
