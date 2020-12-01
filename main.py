import sys


def calculate_expense_report_solution_task1(year: int, expenses: list) -> int:
    delta = []
    for i in range(len(expenses)):
        if expenses[i] in delta:
            j = delta.index(expenses[i])
            return expenses[i] * expenses[j]
        delta.append(year - expenses[i])
    raise RuntimeError("Task not solvable.")


def read_input_file(file_name: str):
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
    else:
        print("Usage: {:s} expenses file".format(sys.argv[0]))
