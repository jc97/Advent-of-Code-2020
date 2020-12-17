#!/usr/bin/env python
"""Advent of Code 2020 - Day 15 - Solution by Julian Knorr (git@jknorr.eu)"""
import re
import sys
from typing import List, Optional, Tuple


RULE_REGEX = r"^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$"
Rule = Tuple[str, Tuple[int, int], Tuple[int, int]]
Ticket = List[int]
Puzzle = Tuple[List[Rule], Ticket, List[Ticket]]


def parse_puzzle(puzzle_text: List[str]) -> Puzzle:
    rules = []
    ticket = []
    tickets = []
    regex = re.compile(RULE_REGEX)
    mode = 0
    for line in puzzle_text:
        line = line.strip()
        if len(line) == 0:
            mode += 1
            continue
        if mode == 0:
            match = regex.fullmatch(line)
            if match is None:
                raise ValueError("Invalid input.")
            groups = match.groups()
            field = groups[0]
            range1 = (int(groups[1]), int(groups[2]))
            range2 = (int(groups[3]), int(groups[4]))
            rules.append((field, range1, range2))
        elif mode == 1:
            if line == "your ticket:":
                continue
            for value in line.split(","):
                ticket.append(int(value))
        elif mode == 2:
            if line == "nearby tickets:":
                continue
            t = []
            for value in line.split(","):
                t.append(int(value))
            tickets.append(t)
        else:
            raise ValueError("Invalid error")
    return rules, ticket, tickets


def check_field_plausibility(value: int, rules: List[Rule]) -> bool:
    for rule in rules:
        if check_rule(value, rule):
            return True
    return False


def check_rule(value: int, rule: Rule) -> bool:
    if rule[1][0] <= value <= rule[1][1]:
        return True
    if rule[2][0] <= value <= rule[2][1]:
        return True
    return False


def ticket_plausibility_error_rate(ticket: Ticket, rules: List[Rule]) -> int:
    error_rate = 0
    for value in ticket:
        if not check_field_plausibility(value, rules):
            error_rate += value
    return error_rate


def check_ticket_plausibility(ticket: Ticket, rules: List[Rule]) -> bool:
    for value in ticket:
        if not check_field_plausibility(value, rules):
            return False
    return True


def task1(puzzle: Puzzle) -> int:
    error_rate = 0
    for ticket in puzzle[2]:
        error_rate += ticket_plausibility_error_rate(ticket, puzzle[0])
    return error_rate


def remaining_possibility(ticket: Ticket, rules: List[Rule], assertions: dict) -> Optional[Tuple[str, int]]:
    for field_index in range(len(ticket)):
        if field_index in assertions.values():
            continue
        possible_rule = None
        for rule in rules:
            if rule[0] in assertions:
                continue
            if check_rule(ticket[field_index], rule):
                if possible_rule is None:
                    possible_rule = rule[0]
                else:
                    possible_rule = None
                    break
        if possible_rule is not None:
            return possible_rule, field_index
    return None


def decode_tickets(puzzle: Puzzle) -> dict:
    valid_tickets = []
    for ticket in puzzle[2]:
        if check_ticket_plausibility(ticket, puzzle[0]):
            valid_tickets.append(ticket)
    num_fields = len(puzzle[0])
    assertion = {}
    updated = True
    while len(assertion) < num_fields and updated:
        updated = False
        for ticket in valid_tickets:
            next_solution = remaining_possibility(ticket, puzzle[0], assertion)
            if next_solution is not None:
                assertion[next_solution[0]] = next_solution[1]
                updated = True
                if len(assertion) == num_fields:
                    break
    if len(assertion) < num_fields:
        raise ValueError("No solution")
    return assertion


def decode_tickets2(puzzle: Puzzle) -> dict:
    possibilities = {}
    valid_tickets = []
    for ticket in puzzle[2]:
        if check_ticket_plausibility(ticket, puzzle[0]):
            valid_tickets.append(ticket)
    num_fields = len(puzzle[0])
    for rule in puzzle[0]:
        possibilities[rule[0]] = list(range(num_fields))
    for ticket in valid_tickets:
        for field_index in range(len(ticket)):
            for rule in puzzle[0]:
                if not check_rule(ticket[field_index], rule):
                    possibilities[rule[0]].remove(field_index)
    update = True
    while update:
        update = False
        for p in possibilities:
            if len(possibilities[p]) == 1:
                for p2 in possibilities:
                    if p2 != p:
                        try:
                            possibilities[p2].remove(possibilities[p][0])
                            update = True
                        except ValueError:
                            pass
    return possibilities


def task2(puzzle: Puzzle) -> int:
    assertion = decode_tickets2(puzzle)
    result = 1
    for field in assertion:
        if field.startswith("departure"):
            result *= puzzle[1][assertion[field][0]]
    return result


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        input_puzzle = parse_puzzle(puzzle_lines)
        task1_solution = task1(input_puzzle)
        print("Task 1: {:d}".format(task1_solution))
        task2_solution = task2(input_puzzle)
        print("Task 2: {:d}".format(task2_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
