#!/usr/bin/env python
"""Advent of Code 2020 - Day 08 - Solution by Julian Knorr (git@jknorr.eu)"""
import re
import sys
from typing import List, Tuple


OPERATION_REGEX = r"^([a-z]{3}) (\+|-)(\d+)$"


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def execute_operation(operation: str) -> Tuple[int, int]:
    match_groups = re.compile(OPERATION_REGEX).fullmatch(operation.strip()).groups()
    if match_groups is None:
        raise ValueError("Invalid Operation Line.")
    op = match_groups[0]
    if op == "nop":
        return 0, 1
    diff = int(match_groups[2])
    if match_groups[1] == "-":
        diff *= -1
    if op == "acc":
        return diff, 1
    if op == "jmp":
        return 0, diff
    raise ValueError("Invalid Operation.")


def execute_code(program: List[str]) -> Tuple[int, bool]:
    executed = [False] * len(program)
    acc = 0
    pointer = 0
    while True:
        if pointer == len(program):
            return acc, True
        if pointer >= len(program):
            return acc, False
        if executed[pointer]:
            return acc, False
        acc_diff, pointer_diff = execute_operation(program[pointer])
        executed[pointer] = True
        acc += acc_diff
        pointer += pointer_diff


def task1(puzzle: List[str]) -> int:
    return (execute_code(puzzle))[0]


def task2(puzzle: List[str]) -> int:
    for i in range(-1, len(puzzle)):
        modified_program = puzzle.copy()
        if i >= 0:
            if modified_program[i].startswith("nop "):
                modified_program[i] = "jmp" + modified_program[i][3:]
            elif modified_program[i].startswith("jmp "):
                modified_program[i] = "nop" + modified_program[i][3:]
            else:
                continue
        acc, success = execute_code(modified_program)
        if success:
            return acc
    raise RuntimeError("Task 2 not solvable.")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        task1_solution = task1(puzzle_lines)
        print("Task 1: acc = {:d}".format(task1_solution))
        task2_solution = task2(puzzle_lines)
        print("Task 2: acc = {:d}".format(task2_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
