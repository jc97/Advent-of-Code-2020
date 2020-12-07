#!/usr/bin/env python
"""Advent of Code 2020 - Day 07 - Solution by Julian Knorr (git@jknorr.eu)"""
import sys
from typing import Dict, List, Optional, Set, Tuple


RULE_REGEX = r"^([a-z]+ [a-z]+) bags contain (?:(no other bags)|(?:(\d+) ([a-z]+ [a-z]+) bags?(?:, (\d+) ([a-z]+ [a-z]+) bags?)*))\.$"


def read_puzzle_file(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    return lines


def build_graph(puzzle: List[str]) -> dict:
    graph = {}
    for rule in puzzle:
        rule_split = rule.strip().split(" contain ")
        rule_bag = (rule_split[0])[:-5]
        if rule_split[1] == "no other bags.":
            continue
        if rule_bag not in graph.keys():
            graph[rule_bag] = []
        rule_sub_bags = rule_split[1][:-1].split(", ")
        for sub_bag in rule_sub_bags:
            sub_bag_rule_split = sub_bag.split(" ", 1)
            weight = int(sub_bag_rule_split[0])
            if weight > 1:
                sub = (sub_bag_rule_split[1])[:-5]
            else:
                sub = (sub_bag_rule_split[1])[:-4]
            graph[rule_bag].append((weight, sub))
    return graph


def get_sub_bags(graph: Dict, start: str, recursive: bool, visited: Optional[Set[str]]) -> Tuple[Optional[List[str]], Optional[Set[str]]]:
    result = []
    if visited is None:
        visited = {start}
    else:
        visited.add(start)
    if start not in graph.keys():
        return None, None
    for edge in graph[start]:
        result.append(edge[1])
        visited.add(edge[1])
        if recursive:
            sub_result, sub_visited = get_sub_bags(graph, edge[1], True, visited)
            if sub_result is not None:
                result += sub_result
            if sub_visited is not None:
                visited.update(sub_visited)
    if recursive:
        return result, visited
    return result, None


def task1(puzzle: List[str]) -> int:
    lookup = "shiny gold"
    graph = build_graph(puzzle)
    result = 0
    for bag in graph.keys():
        subs = (get_sub_bags(graph, bag, True, None))[0]
        if lookup in subs:
            result += 1
    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        puzzle_lines = read_puzzle_file(input_file)
        task1_solution = task1(puzzle_lines)
        print("Task 1: {:d}".format(task1_solution))
    else:
        print("Usage: {:s} puzzle file".format(sys.argv[0]))
