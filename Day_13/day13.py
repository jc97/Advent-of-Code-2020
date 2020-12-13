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


def task2(schedule: str) -> int:
    first_bus = None
    for bus in schedule.strip().split(","):
        if bus != "x":
            first_bus = int(bus)
            break
    t = first_bus
    busses = schedule.strip().split(",")
    iteration_factor = first_bus
    iteration_factor_index = 0
    while True:
        valid_result = True
        i = -1
        for bus in busses:
            i += 1
            if bus == "x" or int(bus) == first_bus:
                continue
            bus_int = int(bus)
            check = (t + busses.index(bus)) % bus_int
            if check != 0 and check != bus_int:
                valid_result = False
                break
            elif iteration_factor_index < i:
                iteration_factor *= bus_int
                iteration_factor_index = i
        if valid_result:
            return t
        t += iteration_factor


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
        task2_solution = task2(puzzle_schedule)
        print("Task 2: {:d}".format(task2_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
