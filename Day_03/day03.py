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


def task01(input_puzzle: List[str]) -> int:
    x, y = 0, 0
    rows = len(input_puzzle)
    trees = 0
    while y < rows - 1:
        y += 1
        x = (x + 3) % len(input_puzzle[y])
        if input_puzzle[y][x] == TREE:
            trees += 1
    return trees


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        puzzle = clean_and_check_puzzle(puzzle_lines)
        task1_solution = task01(puzzle)
        print("Task 1: Trees: {:d}".format(task1_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
