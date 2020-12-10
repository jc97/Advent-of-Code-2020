#!/usr/bin/env python
"""Advent of Code 2020 - Day 09 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import List, Optional


def find_sum(puzzle: List[int], start: int, end: int, value: int) -> bool:
    for i in range(start, end):
        for j in range(start, end):
            if i == j:
                continue
            if puzzle[i] + puzzle[j] == value:
                return True
    return False


def first_error(puzzle: List[int], preamble_length: int) -> Optional[int]:
    for i in range(preamble_length, len(puzzle)):
        if not find_sum(puzzle, i - preamble_length, i, puzzle[i]):
            return puzzle[i]
    return None


def read_puzzle_file(filename: str) -> List[int]:
    file = open(filename, 'r')
    puzzle = []
    for line in file.readlines():
        puzzle.append(int(line))
    return puzzle


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        task1_solution = first_error(puzzle_lines, 25)
        print("Task 1: {:d}".format(task1_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
