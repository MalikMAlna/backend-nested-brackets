#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = """Watch Demo of Nested Brackets
                with Walkthrough by madarp,
                and valid parenthesis"""

import sys
openers = ["(*", "(", "[", "{", "<"]
closers = ["*)", ")", "]", "}", ">"]


def is_nested(line):
    stack = []
    count = 0
    while line:
        token = line[0]
        if line.startswith("(*"):
            token = "(*"
        elif line.startswith("*)"):
            token = "*)"
        count += 1
        line = line[len(token):]
        if token in openers:
            stack.append(token)
        elif token in closers:
            closer_index = closers.index(token)
            expected_opener = openers[closer_index]
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
