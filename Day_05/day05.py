#!/usr/bin/env python
"""Advent of Code 2020 - Day 05 - Solution by Julian Knorr (git@jknorr.eu)"""
import re
import sys
from typing import List, Optional, Tuple


SEAT_REGEX = r"^[BF]{7}[LR]{3}$"


def parse_binary_index(code: str, upper: str, lower: str, minimum: int, maximum: int) -> int:
    maximum_of_lower_range = ((maximum - minimum) // 2) + minimum
    if code[0] == lower:
        maximum = maximum_of_lower_range
    elif code[0] == upper:
        minimum = maximum_of_lower_range + 1
    else:
        raise ValueError("Invalid code.")
    code = code[1:]
    if len(code) == 0:
        if minimum == maximum:
            return minimum
        else:
            raise ValueError("Invalid code: Value range remaining.")
    else:
        if not minimum < maximum:
            raise ValueError("Invalid code: Value range too small.")
        else:
            return parse_binary_index(code, upper, lower, minimum, maximum)


def parse_seat(seat: str) -> Tuple[int, int]:
    if len(seat) != 10:
        raise ValueError("A valid seat code consists of exactly 10 characters.")
    if re.compile(SEAT_REGEX).fullmatch(seat) is None:
        raise ValueError("The seat code contains invalid characters: {:s}".format(seat))
    row_code = seat[:7]
    column_code = seat[-3:]
    row = parse_binary_index(row_code, "B", "F", 0, 127)
    column = parse_binary_index(column_code, "R", "L", 0, 7)
    return row, column


def seat_id(row: int, column: int) -> int:
    return (row * 8) + column


def highest_seat_id(puzzle: List[str]) -> int:
    maximum = 0
    for seat in puzzle:
        current_id = seat_id(*(parse_seat(seat.strip())))
        maximum = max(maximum, current_id)
    return maximum


def seat_plan(puzzle: List[str]) -> List[List[bool]]:
    empty_row = [False] * 8
    seats = [empty_row] * 128
    for seat in puzzle:
        r, c = parse_seat(seat.strip())
        seats[r][c] = True
    return seats


def find_missing_seat(puzzle: List[str]) -> Tuple[Optional[int], Optional[int]]:
    plan = seat_plan(puzzle)
    for r in range(len(plan)):
        for c in range(len(plan[r])):
            if plan[r][c] is False and r+2 < len(plan):
                if plan[r+2][c] is False:
                    return (r + 1), c
    return None, None


def task2(puzzle: List[str]) -> int:
    ids = []
    for seat in puzzle:
        ids.append(seat_id(*(parse_seat(seat.strip()))))
    ids.sort()
    for s in ids:
        if not (s + 1) in ids and (s + 2) in ids:
            return s + 1
    raise RuntimeError("Task 2 not solvable.")


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        task1_solution = highest_seat_id(puzzle_lines)
        print("Task 1: Highest Seat Id: {:d}".format(task1_solution))
        task2_solution = task2(puzzle_lines)
        print("Task 2: Santa's Seat Id: {:d}".format(task2_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
