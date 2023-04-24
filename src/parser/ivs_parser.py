##
# @file ivs_parser.py
#
# @brief Expression parser
#
# @section description_doxygen_example Description
# This Python file implements parse function for calculator
#
# @section author_doxygen_example Author(s)
# - Created by Oleksandr Turytsia (xturyt00).
# - Modified by Oleksandr Turytsia (xturyt00) on 24/04/2023.
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

import src.math.ivs_math as m

class ParserError(Exception):
    """ ParseError exception.
    Defines exception for syntax/parsing errors.
    """
    def __init__(self, msg=None):
        """ Constructor for parse exception

        @param msg  error message that should be displayed (default is "Syntax error")
        """
        super().__init__(msg or "Syntax error")


class ValueTooLongError(Exception):
    """ ParseError exception.
    Defines exception for infinite values.
    """
    def __init__(self):
        """ Constructor for infinite exception
        """
        super().__init__("∞")


class IntegerError(Exception):
    """ ParseError exception.
    Defines exception for faulty-typed values.
    """
    def __init__(self, msg):
        """ Constructor for type exceptions

        @param msg  error message that should be displayed
        """
        super().__init__(msg)


def parse(expr: str) -> str:
    """ Evaluates mathematical expression.
    @param expr expression string.
    @return  resulting value.
    """

    # In case of empty string do nothing.
    if not expr:
        return ""

    # Presedense table. Look at rules.md
    precedence = {
        "(": 0,
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "√": 3,
        "^": 3,
        ")": 4
    }

    # Operator and Operand stacks for parser
    operator_stack = []
    operand_stack = []

    def _safe(n: float):
        """ Defines type of n.
        @param n
        @return  typed n.
        """
        result = round(n, 10)
        try:
            return int(result) if result.is_integer() else result
        except AttributeError:
            return int(result)

    def _isnumber(n: str) -> bool:
        """ Checks whether n is a numeric string
        @param n
        @return  typed n.
        """
        try:
            if n.isdigit():
                return True
            float(n)
            return True
        except Exception:
            return False

    def _apply_binary_op():
        """ Applies binary operator onto 2 operands
        """
        b = operand_stack.pop()
        a = operand_stack.pop()
        op = operator_stack.pop()

        if op == "+":
            operand_stack.append(_safe(m.sum(a, b)))
        elif op == "-":
            operand_stack.append(_safe(m.sub(a, b)))
        elif op == "*":
            operand_stack.append(_safe(m.mult(a, b)))
        elif op == "/":
            operand_stack.append(_safe(m.div(a, b)))
        elif op == "/":
            operand_stack.append(_safe(m.div(a, b)))
        elif op == "^":
            if b < 0 or isinstance(b, float):
                raise IntegerError("exp >= 0 ∧ exp ∈ Z")
            operand_stack.append(_safe(m.exp(a, b)))
        elif op == "√":
            if b < 0 or isinstance(a, float):
                raise IntegerError("exp >= 0 ∧ exp ∈ Z")
            operand_stack.append(_safe(m.exp(b, 1 / a)))

    def _apply_factorial():
        """ Applies factorial onto first operand in the stack
        """
        a = operand_stack.pop()
        if a < 0 or isinstance(a, float):
            raise IntegerError("n!, where n ∈ Z")
        operand_stack.append(_safe(m.fac(a)))

    try:
        expr = expr.split(" ")
        for i, token in enumerate(expr):
            if _isnumber(token):
                operand_stack.append(
                    int(token) if token.isdigit() else float(token))
            elif token == "-" and (i == 0 or expr[i-1] in "+-*/^√("):
                operand_stack.append(0)
                operator_stack.append(token)
            elif token in "+*/^√-":
                while operator_stack and operand_stack and precedence[token] <= precedence[operator_stack[-1]]:
                    _apply_binary_op()
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack[-1] != "(":
                    _apply_binary_op()
                operator_stack.pop()
            elif token == "!":
                if operator_stack and operator_stack[-1] == "-":
                    _apply_binary_op()
                _apply_factorial()
            else:
                raise ParserError(f"'{token}' is not valid ")

        while operator_stack:
            _apply_binary_op()

        result, = operand_stack

        return str(_safe(round(result, 10))) if result < 999_999_999_999 else "{:.2E}".format(result)
    except RecursionError:
        raise ValueTooLongError()
    except (Exception) as e:
        raise ParserError(str(e))
