import os
import sys
import platform

if platform.system() == "Windows":
    sys.path.insert(0, os.getcwd())
else:
    sys.path.insert(0, os.path.abspath(".."))

import src.math.ivs_math as m


class ParserError(Exception):
    def __init__(self, msg=None):
        super().__init__(msg or "Syntax error")


class ValueTooLongError(Exception):
    def __init__(self):
        super().__init__("∞")


class IntegerError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


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
        ")": 4
    }

    operator_stack = []
    operand_stack = []

    def _safe(n: int | float):
        result = round(n, 10)
        try:
            return int(result) if result.is_integer() else result
        except AttributeError:
            return int(result)

    def _isnumber(n: str):
        try:
            if n.isdigit():
                return True
            float(n)
            return True
        except Exception:
            return False

    def _apply_binary_op():
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
