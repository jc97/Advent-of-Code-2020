#!/usr/bin/env python
"""Advent of Code 2020 - Day 17 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import Dict, List


Row = Dict[int, bool]
Slice = Dict[int, Row]
State = Dict[int, Slice]


def next_state(state: State) -> State:
    new_state = dict()
    min_level = min(state.keys())
    max_level = max(state.keys())
    for z in range(min_level - 1, max_level + 2):
        for y in range(min(state[0]) - 1, max(state[0]) + 2):
            for x in range(min(state[0][0]) - 1, max(state[0][0]) + 2):
                active_neighbours = get_active_neighbours(state, x, y, z)
                new_cube_state = False
                try:
                    current_cube_state = state[z][y][x]
                except KeyError:
                    current_cube_state = False
                if current_cube_state and 2 <= active_neighbours <= 3:
                    new_cube_state = True
                elif not current_cube_state and active_neighbours == 3:
                    new_cube_state = True
                set_cube_state(new_state, x, y, z, new_cube_state)
    return new_state


def set_cube_state(state: State, x: int, y: int, z: int, activeness: bool):
    if z not in state:
        state[z] = dict()
    if y not in state[z]:
        state[z][y] = dict()
    state[z][y][x] = activeness


def get_active_neighbours(state: State, x: int, y: int, z: int) -> int:
    result = 0
    for z2 in range(z - 1, z + 2):
        if z2 not in state:
            continue
        for y2 in range(y - 1, y + 2):
            if y2 not in state[z2]:
                continue
            for x2 in range(x - 1, x + 2):
                if x2 not in state[z2][y2]:
                    continue
                if x != x2 or y != y2 or z != z2:
                    if state[z2][y2][x2]:
                        result += 1
    return result


def parse_puzzle_state(cube_state: str) -> bool:
    if cube_state == "#":
        return True
    return False


def puzzle_to_state(puzzle: List[str]) -> State:
    result = {0: dict()}
    for y in range(len(puzzle)):
        row = dict()
        puzzle_row = puzzle[y].strip()
        for x in range(len(puzzle_row)):
            row[x] = parse_puzzle_state(puzzle_row[x])
        result[0][y] = row
    return result


def count_active_cubes(state: State) -> int:
    result = 0
    for z in state:
        for y in state[z]:
            for x in state[z][y]:
                if state[z][y][x]:
                    result += 1
    return result


def task1(state: State, iterations: int) -> int:
    state = state.copy()
    for i in range(iterations):
        state = next_state(state)
    return count_active_cubes(state)


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        initial_state = puzzle_to_state(puzzle_lines)
        task1_solution = task1(initial_state, 6)
        print("Task 1: {:d}".format(task1_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
