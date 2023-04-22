import os
import sys
import platform

if platform.system() == "Windows":
    sys.path.insert(0, os.getcwd())
else:
    sys.path.insert(0, os.path.abspath(".."))

from src.math.ivs_math import sum as _sum, sub, mult, div, fac, exp, square_root


class ParserError(Exception):
    def __init__(self):
        super().__init__("Syntax error occured")


class ValueTooLongError(Exception):
    def __init__(self):
        super().__init__("Value is too long")


def parse(expr: str) -> str:
    if not expr:
        return ""

    precedence = {
        "(": 0,
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "√": 3,
        "^": 3,
        ")": 4}

    operator_stack = []
    operand_stack = []

    def is_number(n: str):
        try:
            if n.isdigit():
                return True
            float(n)
            return True
        except Exception:
            return False

    def apply_operator():
        b = operand_stack.pop()
        a = operand_stack.pop()
        op = operator_stack.pop()

        if op == "+":
            operand_stack.append(_sum(a, b))
        elif op == "-":
            operand_stack.append(sub(a, b))
        elif op == "*":
            operand_stack.append(mult(a, b))
        elif op == "/":
            operand_stack.append(div(a, b))
        elif op == "^":
            operand_stack.append(exp(a, b))

    def apply_factorial():
        a = operand_stack.pop()
        operand_stack.append(fac(a))

    def apply_square():
        a = operand_stack.pop()
        operator_stack.pop()
        operand_stack.append(square_root(a))

    try:
        expr = expr.split(" ")
        for token in expr:
            print(operand_stack)
            if is_number(token):
                operand_stack.append(float(token))
            elif token in "+-*/^√":
                # Parse operator
                while operator_stack and operand_stack and precedence[token] <= precedence[operator_stack[-1]]:
                    if operator_stack[-1] == "√":
                        apply_square()
                    else:
                        apply_operator()
                operator_stack.append(token)
            elif token == "(" or token == "√" or token == "-":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack[-1] != "(":
                    if operator_stack[-1] == "√":
                        apply_square()
                    else:
                        apply_operator()
                operator_stack.pop()
            elif token == "!":
                apply_factorial()
            else:
                raise ParserError()

        while operator_stack:
            if operator_stack[-1] == "√":
                apply_square()
            else:
                apply_operator()

        result = operand_stack[0]

        if result < 999_999_999_999:
            return str(operand_stack[0]).rstrip('0').rstrip('.')
        else:
            return "{:.2E}".format(operand_stack[0])

    except RecursionError:
        raise ValueTooLongError()
    except Exception as e:
        print(e)
        raise ParserError()
