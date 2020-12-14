#!/usr/bin/env python
"""Advent of Code 2020 - Day 14 - Solution by Julian Knorr (git@jknorr.eu)"""
import re
import sys
from typing import Dict, List, Tuple


ASSERTION_REGEX = r"^mem\[(\d+)\] = (\d+)$"


def apply_mask(input: int, mask: str) -> int:
    input_bin = bin(input)[2:]
    if len(input_bin) < len(mask):
        input_bin = "0" * (len(mask) - len(input_bin)) + input_bin
    input_bin = list(input_bin)
    for i in range(len(mask)):
        if mask[i] != "X":
            input_bin[i] = mask[i]
    output = int("".join(input_bin), 2)
    return output


def get_addresses_from_mask(address: int, mask: str) -> List[int]:
    address_bin = bin(address)[2:]
    if len(address_bin) < len(mask):
        address_bin = "0" * (len(mask) - len(address_bin)) + address_bin
    address_bin = list(address_bin)
    floating_bits = []
    for i in range(len(mask)):
        if mask[i] != "0":
            address_bin[i] = mask[i]
        if mask[i] == "X":
            floating_bits.append(i)
    result = []
    for b in range(2 ** len(floating_bits)):
        b_bin = bin(b)[2:]
        if len(b_bin) < len(floating_bits):
            b_bin = "0" * (len(floating_bits) - len(b_bin)) + b_bin
        b_bin = list(b_bin)
        new_address = address_bin.copy()
        for i in range(len(floating_bits)):
            new_address[floating_bits[i]] = b_bin[i]
        result.append(int("".join(new_address), 2))
    return result


def execute_program2(program: List[str]) -> dict:
    mask = "X" * 36
    memory = {}
    regex = re.compile(ASSERTION_REGEX)
    for instruction in program:
        instruction = instruction.strip()
        if instruction.startswith("mask = "):
            mask = instruction[7:]
        else:
            match = regex.fullmatch(instruction)
            if not match is None:
                mg = match.groups()
                addresses = get_addresses_from_mask(int(mg[0]), mask)
                for address in addresses:
                    memory[address] = int(mg[1])
            else:
                raise ValueError("Invalid instruction.")
    return memory


def execute_program(program: List[str]) -> dict:
    mask = "X" * 36
    memory = {}
    regex = re.compile(ASSERTION_REGEX)
    for instruction in program:
        instruction = instruction.strip()
        if instruction.startswith("mask = "):
            mask = instruction[7:]
        else:
            match = regex.fullmatch(instruction)
            if not match is None:
                mg = match.groups()
                memory[int(mg[0])] = apply_mask(int(mg[1]), mask)
            else:
                raise ValueError("Invalid instruction.")
    return memory


def task1(puzzle: List[str]) -> int:
    mem = execute_program(puzzle)
    result = 0
    for value in mem:
        result += mem[value]
    return result


def task2(puzzle: List[str]) -> int:
    mem = execute_program2(puzzle)
    result = 0
    for value in mem:
        result += mem[value]
    return result


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


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
