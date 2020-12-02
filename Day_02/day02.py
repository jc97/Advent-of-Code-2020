#!/usr/bin/env python
"""Advent of Code 2020 - Day 02 - Solution by Julian Knorr (git@jknorr.eu)"""
import re
import sys
import typing


PASSWORD_REGEX = r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$"


def solve_puzzle(puzzle: typing.List[str]) -> typing.Tuple[int, int, int]:
    invalid_lines = 0
    invalid_passwords = 0
    valid_passwords = 0
    regex = re.compile(PASSWORD_REGEX)
    for line in puzzle:
        m = regex.fullmatch(line.strip())
        if not isinstance(m, re.Match):
            invalid_lines += 1
            continue
        min_occurrences = int(m.group(1))
        max_occurrences = int(m.group(2))
        character = str(m.group(3))
        password = m.group(4)
        if max_occurrences < min_occurrences:
            raise ValueError("The maximum character occurrences cannot be greater then the minimum occurrences.")
        count = password.count(character)
        if min_occurrences <= count <= max_occurrences:
            valid_passwords += 1
        else:
            invalid_passwords += 1
    return valid_passwords, invalid_passwords, invalid_lines


def read_puzzle_file(filename: str) -> typing.List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        valid, invalid, invalid_entries = solve_puzzle(puzzle_lines)
        print("Valid Passwords: {:d}".format(valid))
        print("Invalid Passwords: {:d}".format(invalid))
        print("Invalid Lines: {:d}".format(invalid_entries))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
