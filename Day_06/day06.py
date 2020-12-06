#!/usr/bin/env python
"""Advent of Code 2020 - Day 06 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import Callable, List, Set


PuzzleGroup = List[Set[str]]
Puzzle = List[PuzzleGroup]


def read_puzzle_file(filename: str) -> str:
    file = open(filename, 'r')
    return file.read()


def groups_from_puzzle(puzzle: str) -> Puzzle:
    groups_text = puzzle.split("\n\n")
    groups = []
    for g in groups_text:
        group = []
        for person in g.split("\n"):
            if len(person) > 0:
                group.append(set(person.strip()))
        groups.append(group)
    return groups


def get_group_answers_union(group: PuzzleGroup) -> Set[str]:
    return set.union(*group)


def get_group_answers_intersection(group: PuzzleGroup) -> Set[str]:
    return set.intersection(*group)


def count_group_answers(answers: Set[str]) -> int:
    return len(answers)


def sum_group_result_length(groups: Puzzle, operator: Callable) -> int:
    result = 0
    for g in groups:
        result += len(operator(g))
    return result


def task1(puzzle: str):
    groups = groups_from_puzzle(puzzle)
    return sum_group_result_length(groups, get_group_answers_union)


def task2(puzzle: str):
    groups = groups_from_puzzle(puzzle)
    return sum_group_result_length(groups, get_group_answers_intersection)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_data = read_puzzle_file(input_file)
        print("Task 1: Solution: {:d}".format(task1(puzzle_data)))
        print("Task 2: Solution: {:d}".format(task2(puzzle_data)))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
