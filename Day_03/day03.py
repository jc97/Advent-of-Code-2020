#!/usr/bin/env python
"""Advent of Code 2020 - Day 03 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import List, Optional


TREE = "#"
FREE = "."


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def clean_and_check_puzzle(puzzle_input: List[str]) -> Optional[List[str]]:
    puzzle_output = []
    for line in puzzle_input:
        line = line.strip()
        for field in line:
            if field not in [TREE, FREE]:
                raise ValueError("Invalid field value: {:s}".format(field))
        puzzle_output.append(line)
    return puzzle_output


def test_slope(input_puzzle: List[str], slope_width_x: int, slope_width_y: int) -> int:
    x, y = 0, 0
    rows = len(input_puzzle)
    trees = 0
    while y < rows - 1:
        y += slope_width_y
        x = (x + slope_width_x) % len(input_puzzle[y])
        if input_puzzle[y][x] == TREE:
            trees += 1
    return trees


def task01(input_puzzle: List[str]) -> int:
    return test_slope(input_puzzle, 3, 1)


def task02(input_puzzle: List[str]) -> int:
    result = 1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for slope in slopes:
        result *= test_slope(input_puzzle, slope[0], slope[1])
    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        puzzle = clean_and_check_puzzle(puzzle_lines)
        task1_solution = task01(puzzle)
        print("Task 1: Trees: {:d}".format(task1_solution))
        task2_solution = task02(puzzle)
        print("Task 2: Trees: {:d}".format(task2_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
