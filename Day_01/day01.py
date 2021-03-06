#!/usr/bin/env python
"""Advent of Code 2020 - Day 01 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys


def calculate_expense_report_solution_task1(year: int, expenses: list) -> int:
    delta = []
    for i in range(len(expenses)):
        if expenses[i] in delta:
            j = delta.index(expenses[i])
            return expenses[i] * expenses[j]
        delta.append(year - expenses[i])
    raise RuntimeError("Task not solvable.")


def calculate_expense_report_solution_task2(year: int, expenses: list) -> int:
    delta1 = []
    delta2 = []
    for i in range(0, len(expenses)):
        delta2.append([])

    for i in range(len(expenses)):
        found, x, y = in_matrix(delta2, expenses[i])
        if found:
            return expenses[x] * expenses[y] * expenses[i]
        delta1.append(year - expenses[i])
        for n in range(0, i):
            delta2[i].append(delta1[n] - expenses[i])
    raise RuntimeError("Task not solvable.")


def in_matrix(matrix: list, value) -> tuple:
    for i in range(len(matrix)):
        if value in matrix[i]:
            return True, i, matrix[i].index(value)
    return False, None, None


def read_input_file(file_name: str) -> list:
    file = open(file_name, 'r')
    lines = file.readlines()
    numbers = []
    for line in lines:
        if line.strip().isdigit():
            numbers.append(int(line.strip()))
    return numbers


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_expenses = read_input_file(sys.argv[1])
        result = calculate_expense_report_solution_task1(2020, input_expenses)
        print("Result for Task 1: {:d}".format(result))
        result = calculate_expense_report_solution_task2(2020, input_expenses)
        print("Result for Task 2: {:d}".format(result))
    else:
        print("Usage: {:s} expenses file".format(sys.argv[0]))
