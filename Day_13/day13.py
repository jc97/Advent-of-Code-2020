#!/usr/bin/env python
"""Advent of Code 2020 - Day 13 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import Tuple


def get_waiting_time(bus: int, departure: int):
    return (((departure // bus) + 1) * bus) - departure


def task1(schedule: str, departure: int) -> int:
    best_bus = {"id": None, "waiting": None}
    for bus in schedule.strip().split(","):
        if bus == "x":
            continue
        bus = int(bus)
        waiting_time = get_waiting_time(bus, departure)
        if best_bus["id"] is None:
            best_bus["id"] = bus
            best_bus["waiting"] = waiting_time
        elif waiting_time < best_bus["waiting"]:
            best_bus["id"] = bus
            best_bus["waiting"] = waiting_time
    return best_bus["id"] * best_bus["waiting"]


def read_puzzle_file(filename: str) -> Tuple[str, int]:
    file = open(filename, 'r')
    puzzle = file.readlines()
    departure = int(puzzle[0].strip())
    schedule = puzzle[1].strip()
    return schedule, departure


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_schedule, puzzle_departure = read_puzzle_file(input_file)
        task1_solution = task1(puzzle_schedule, puzzle_departure)
        print("Task 1: {:d}".format(task1_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
