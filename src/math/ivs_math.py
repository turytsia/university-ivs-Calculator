##
# @file ivs_math.py
#
# @brief Math functions for calculator.
#
# @section description_doxygen_example Description
# This Python file implements several functions for a calculator, including addition, 
# subtraction, multiplication, division, factorial, exponentiation, and square root.
#
# @section author_doxygen_example Author(s)
# - Created by Nikita Koliada (xkolia00).
# - Modified by Oleksandr Turytsia (xturyt00) on 24/04/2023.
#
# Copyright (c) GNU GENERAL PUBLIC LICENSE version 3

# Functions

class ZeroDivisonError(Exception):
    def __init__(self):
        super().__init__("Cannot divide by zero")

def sum(a: float, b: float) -> float:
    """ Sums 2 operands up.
    @param a   first operand.
    @param b   second operand.
    @return  sum of param a and b
    """
    return a + b

def sub(a: float, b: float) -> float:
    """ Subtracts 2 operands up.
    @param a   first operand.
    @param b   second operand.
    @return  difference between a and b
    """
    return a - b


def mult(a: float, b: float) -> float:
    """ Multiplies 2 operands up.
    @param a   first operand.
    @param b   second operand.
    @return  multiplication of a and b
    """
    return a * b


def div(a: float, b: float) -> float:
    """ Divides 2 operands up.
    @param a   first operand.
    @param b   second operand.
    @return  division of a and b
    """
    if b != 0:
        return a / b
    else:
        raise ZeroDivisonError()


def fac(a: int) -> int:
    """ Applies factorial onto given value.
    @param a  operand.
    @return  factorial of a
    """
    if a == 0 or a == 1:
        return 1
    return a * fac(a-1)


def exp(a: float, b: int) -> float:
    """ Takes power of b on argument a.
    @param a   first operand.
    @param b   second operand (power).
    @return  a in power of b
    """
    return a ** b

# returns the result of square root of a


def square_root(a: float) -> float:
    """ Applies square root onto given value.
    @param a  operand.
    @return  square of a
    """
    if a < 0:
        raise ValueError("Cannot compute square root of negative number")
    elif a == 0:
        return 0
    else:
        x = a
        y = 1
        while x > y:
            x = (x + y) / 2
            y = a / x
        return x