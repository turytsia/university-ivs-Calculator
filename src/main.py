##
# Team Tripple-Double
#
# @file main.py
#
# @brief Calculator initialization
#
# @section description_doxygen_example Description
# This Python file starts up calculator
#
# @section author_doxygen_example Author(s)
# - Created by Maksym Podhornyi (xpodho08).
# - Modified by Oleksandr Turytsia (xturyt00) on 25/04/2023.
#
# Copyright (c) GNU GENERAL PUBLIC LICENSE version 3

# Functions

import os
import sys
import platform

if platform.system() == "Windows":
    sys.path.append(os.getcwd())
else:
    sys.path.append(os.path.dirname(os.path.abspath("") + "/src"))

from src.view.ivs_view import Calculator


def main():
    """
        Initial method
    """
    calculator = Calculator()
    calculator.create_main_window()
    calculator.run()


if __name__ == "__main__":
    main()