#!/usr/bin/env python
"""Advent of Code 2020 - Day 02 - Solution by Julian Knorr (git@jknorr.eu)"""
import re
import sys
from typing import Callable, List, Optional, Tuple


PASSWORD_REGEX = r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$"


def solve_puzzle(puzzle: List[str], task_validator: Callable) -> Tuple[int, int, int]:
    invalid_lines = 0
    invalid_passwords = 0
    valid_passwords = 0
    regex = re.compile(PASSWORD_REGEX)
    for line in puzzle:
        valid_line, policy, password = evaluate_line(line, regex)
        if not valid_line:
            invalid_lines += 1
            continue
        if task_validator(policy, password):
            valid_passwords += 1
        else:
            invalid_passwords += 1
    return valid_passwords, invalid_passwords, invalid_lines


def validate_task1(policy: list, password: str):
    min_occurrences = int(policy[0])
    max_occurrences = int(policy[1])
    character = policy[2]
    if max_occurrences < min_occurrences:
        raise ValueError("The maximum character occurrences cannot be greater then the minimum occurrences.")
    count = password.count(character)
    if min_occurrences <= count <= max_occurrences:
        return True
    return False


def validate_task2(policy: list, password: str):
    position1 = int(policy[0])
    position2 = int(policy[1])
    character = policy[2]
    if position1 == position2:
        raise ValueError("The policy position must not be equal.")
    count = 0
    if position1 <= len(password):
        if password[position1 - 1] == character:
            count += 1
    if position2 <= len(password):
        if password[position2 - 1] == character:
            count += 1
    if count == 1:
        return True
    return False


def evaluate_line(line: str, regex: re.Pattern) -> Tuple[bool, Optional[list], Optional[str]]:
    m = regex.fullmatch(line.strip())
    policy = []
    if not isinstance(m, re.Match):
        return False, None, None
    for i in range(1, regex.groups + 1):
        policy.append(m.group(i))
    return True, policy, m.group(regex.groups)


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        valid1, invalid1, invalid_entries = solve_puzzle(puzzle_lines, validate_task1)
        print("Invalid Lines: {:d}".format(invalid_entries))
        valid2, invalid2, invalid_entries = solve_puzzle(puzzle_lines, validate_task2)
        print("")
        print("Task 1: Valid Passwords: {:d}".format(valid1))
        print("Task 1: Invalid Passwords: {:d}".format(invalid1))
        print("")
        print("Task 2: Valid Passwords: {:d}".format(valid2))
        print("Task 2: Invalid Passwords: {:d}".format(invalid2))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
