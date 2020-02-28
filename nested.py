#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = """Watch Demo of Nested Brackets
                with Walkthrough by madarp,
                and valid parenthesis"""

import sys

bracket_pair_dict = {"*)": "(*",
                     ")": "(",
                     "]": "[",
                     "}": "{",
                     ">": "<"}

bracket_list = sorted(bracket_pair_dict.keys() +
                      bracket_pair_dict.values(), key=len, reverse=True)


def is_nested(line):
    stack = []
    count = 0
    while line:
        token = line[0]
        for b in bracket_list:
            if line.startswith(b):
                token = b
                break
        count += 1
        line = line[len(token):]
        if token in bracket_pair_dict.values():
            stack.append(token)
        elif token in bracket_pair_dict.keys():
            expected_opener = bracket_pair_dict[token]
            if stack.pop() != expected_opener:
                return "NO " + str(count)
    if stack:
        return "NO " + str(count)

    return "YES"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    print("Testing for the Nesting: {}".format(args[0]))
    with open(args[0]) as ifile:
        with open("output.txt", "w") as ofile:
            for line in ifile:
                result_str = is_nested(line)
                print(result_str)
                ofile.write(result_str + "\n")


if __name__ == '__main__':
    main(sys.argv[1:])
