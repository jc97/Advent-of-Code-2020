#!/usr/bin/env python
"""Advent of Code 2020 - Day 11 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import List, Tuple


OCCUPIED_STR = "#"
FLOOR_STR = "."
EMPTY_STR = "L"
OCCUPIED = 2
EMPTY = 1
FLOOR = 0
State = List[List[int]]


def count_occupied_adjacent_seats(state: State, row: int, column: int) -> int:
    result = 0
    rows = len(state)
    columns = len(state[0])
    if row > 0:
        result += int(state[row - 1][column] == OCCUPIED)
        if column > 0:
            result += int(state[row - 1][column - 1] == OCCUPIED)
        if column < columns - 1:
            result += int(state[row - 1][column + 1] == OCCUPIED)
    if row < rows - 1:
        result += int(state[row + 1][column] == OCCUPIED)
        if column > 0:
            result += int(state[row + 1][column - 1] == OCCUPIED)
        if column < columns - 1:
            result += int(state[row + 1][column + 1] == OCCUPIED)
    if column > 0:
        result += int(state[row][column - 1] == OCCUPIED)
    if column < columns - 1:
        result += int(state[row][column + 1] == OCCUPIED)
    return result


def next_state(state: State) -> Tuple[State, bool]:
    rows = len(state)
    columns = len(state[0])
    new_state = []
    for r in range(rows):
        new_state.append([FLOOR] * columns)
    modified = False
    for r in range(rows):
        for c in range(columns):
            if state[r][c] != FLOOR:
                occupied_adjacent_seats = count_occupied_adjacent_seats(state, r, c)
                if state[r][c] == EMPTY:
                    if occupied_adjacent_seats == 0:
                        new_state[r][c] = OCCUPIED
                        modified = True
                    else:
                        new_state[r][c] = EMPTY
                elif state[r][c] == OCCUPIED:
                    if occupied_adjacent_seats >= 4:
                        new_state[r][c] = EMPTY
                        modified = True
                    else:
                        new_state[r][c] = OCCUPIED
    return new_state, modified


def count_occupied_seats(state: State) -> int:
    result = 0
    for row in state:
        for seat in row:
            if seat == OCCUPIED:
                result += 1
    return result


def task1(puzzle: State) -> int:
    new_state = puzzle
    modified = True
    while modified:
        new_state, modified = next_state(new_state)
    return count_occupied_seats(new_state)


def read_puzzle_file(filename: str) -> State:
    file = open(filename, 'r')
    state = []
    columns = 0
    for line in file.readlines():
        row = []
        for s in line.strip():
            if s == FLOOR_STR:
                row.append(FLOOR)
            elif s == EMPTY_STR:
                row.append(EMPTY)
            elif s == OCCUPIED_STR:
                row.append(OCCUPIED)
            else:
                raise ValueError("Invalid seat label.")
        if columns == 0 or columns == len(row):
            state.append(row)
        else:
            raise ValueError("Every rows needs to have the same length.")
        if columns == 0:
            columns = len(row)
    return state


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle = read_puzzle_file(input_file)
        task1_solution = task1(puzzle)
        print("Task 1: {:d}".format(task1_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
