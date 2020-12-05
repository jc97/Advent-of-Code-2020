#!/usr/bin/env python
"""Advent of Code 2020 - Day 04 - Solution by Julian Knorr (git@jknorr.eu)"""
import re
import sys
from typing import List, Tuple


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
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
