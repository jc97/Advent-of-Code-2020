#!/usr/bin/env python
"""Advent of Code 2020 - Day 04 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import Callable, Dict, List


TASK1_REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    return file.readlines()


def passports_from_puzzle(puzzle: List[str]) -> List[str]:
    passports = []
    current_data = ""
    for line in puzzle:
        if len(line.strip()) == 0 and len(current_data) > 0:
            passports.append(current_data)
            current_data = ""
        else:
            current_data += line
    if len(current_data) > 0:
        passports.append(current_data)
    return passports


def parse_passport(passport_data: str) -> Dict:
    field_data = passport_data.strip().split()
    fields = dict()
    for f in field_data:
        data = f.split(":")
        fields[data[0]] = data[1]
    return fields


def get_passports(puzzle: List[str]) -> List[Dict]:
    raw_passports = passports_from_puzzle(puzzle)
    passports = []
    for p in raw_passports:
        passports.append(parse_passport(p))
    return passports


def validate_passport_task1(passport: Dict) -> bool:
    for required in TASK1_REQUIRED_FIELDS:
        if required not in passport.keys():
            return False
    return True


def count_valid_passports(puzzle: List[str], validator: Callable) -> int:
    passports = get_passports(puzzle)
    valid_count = 0
    for p in passports:
        if validator(p):
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_data = read_puzzle_file(input_file)
        print("Task 1: Valid Passports: {:d}".format(count_valid_passports(puzzle_data, validate_passport_task1)))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
