##
# @file profiler.py
#
# @brief Data generator for profiler.py
#
# @section description_doxygen_example Description
# This Python file implements value generator
#
# @section author_doxygen_example Author(s)
# - Created by Pavlo Butenko (xbuten00).
# - Modified by Oleksandr Turytsia (xturyt00) on 24/04/2023.
#
# Copyright (c) GNU GENERAL PUBLIC LICENSE version 3

import random
import sys

assert(int(sys.argv[1]) > 1)
for i in range(0, int(sys.argv[1])):
    print(random.randint(1, 100000), end=" ")
