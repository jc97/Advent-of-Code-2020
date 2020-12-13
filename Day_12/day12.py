#!/usr/bin/env python
"""Advent of Code 2020 - Day 12 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import List, Tuple


def navigate(x: int, y: int, d: int, operation: str) -> Tuple[int, int, int]:
    operation_type = operation[:1]
    operation_value = int(operation[1:])
    if operation_type == "N" or (operation_type == "F" and d == 0):
        return x, y + operation_value, d
    if operation_type == "S" or (operation_type == "F" and d == 180):
        return x, y - operation_value, d
    if operation_type == "E" or (operation_type == "F" and d == 90):
        return x + operation_value, y, d
    if operation_type == "W" or (operation_type == "F" and d == 270):
        return x - operation_value, y, d
    if operation_type == "L":
        return x, y, (d - operation_value) % 360
    if operation_type == "R":
        return x, y, (d + operation_value) % 360
    raise ValueError("Invalid Operation.")


def navigate_list(x: int, y: int, d: int, operations: List[str]) -> Tuple[int, int, int]:
    for op in operations:
        x, y, d = navigate(x, y, d, op.strip())
    return x, y, d


def task1(puzzle: List[str]) -> int:
    x, y, d = navigate_list(0, 0, 90, puzzle)
    return abs(x) + abs(y)


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    puzzle = file.readlines()
    return puzzle


def task2(puzzle: List[str]) -> int:
    status = {"x": 0, "y": 0, "wp_x": 10, "wp_y": 1}
    for operation_raw in puzzle:
        operation = operation_raw.strip()
        if operation[:1] in ["N", "S", "W", "E"]:
            status["wp_x"], status["wp_y"], _ = navigate(status["wp_x"], status["wp_y"], 0, operation)
        elif operation == "R90" or operation == "L270":
            wp_x = status["wp_y"]
            wp_y = -1 * status["wp_x"]
            status["wp_x"], status["wp_y"] = wp_x, wp_y
        elif operation == "L90" or operation == "R270":
            wp_y = status["wp_x"]
            wp_x = -1 * status["wp_y"]
            status["wp_x"], status["wp_y"] = wp_x, wp_y
        elif operation == "R180" or operation == "L180":
            status["wp_x"] = status["wp_x"] * -1
            status["wp_y"] = status["wp_y"] * -1
        elif operation[:1] == "F":
            factor = int(operation[1:])
            status["x"] += factor * status["wp_x"]
            status["y"] += factor * status["wp_y"]
        else:
            raise ValueError("Invalid Operation.")
    return abs(status["x"]) + abs(status["y"])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        task1_solution = task1(puzzle_lines)
        print("Task 1: {:d}".format(task1_solution))
        task2_solution = task2(puzzle_lines)
        print("Task 2: {:d}".format(task2_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
