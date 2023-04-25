##
# @file profiler.py
#
# @brief Profiler
#
# @section description_doxygen_example Description
# This Python file implements profiling that analyzes math functions at ivs_math.py
#
# @section author_doxygen_example Author(s)
# - Created by Pavlo Butenko (xbuten00).
# - Modified by Oleksandr Turytsia (xturyt00) on 24/04/2023.
#
# Copyright (c) GNU GENERAL PUBLIC LICENSE version 3

# Functions

import cProfile
from ..math import ivs_math as math


def count(list: list) -> int:
    """ Counts list elements
        @param list
        @return  number of elements in list.
        """
    list_count = 0
    for _ in list:
        list_count = math.sum(list_count, 1)
    return list_count


def avg(list: list) -> list:
    """ Calculates average value from list
        @param list
        @return  average value
        """
    sum = 0
    for item in list:
        sum = math.sum(sum, item)
    return (math.div(sum, count(list)))


def formule(list: list) -> list:
    """ Applies formula in order to analyze math functions
        @param list
        @return  calculated value
        """
    list_count = count(list)
    average = avg(list)
    s = 0
    for item in list:
        s = math.sum(s, math.exp(item, 2))
    s = math.sub(s, math.mult(list_count, math.exp(average, 2)))
    s = math.div(s, math.sub(list_count, 1))
    s = math.square_root(s)
    return s


def main():
    """ Init function
        """
    input_numbers = list(map(int, input().split()))
    print("Average value is " + str(avg(input_numbers)))
    print("S = " + str(formule(input_numbers)))


if __name__ == '__main__':
    cProfile.run('main()', sort='time')
