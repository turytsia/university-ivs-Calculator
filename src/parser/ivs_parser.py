import os, sys, platform

if platform.system() == "Windows":
    sys.path.insert(0, os.getcwd())
else:
    sys.path.insert(0, os.path.abspath(".."))

from src.math.ivs_math import sum as _sum, sub, mult, div, fac, exp, square_root

class ParserError(Exception):
    def __init__(self):
        super().__init__("Syntax error occured")

def parse(expr: str) -> str:
    if not expr:
        return ""

    precedence = {
        "(": 0,
        "+": 1, 
        "-": 1, 
        "*": 2, 
        "/": 2, 
        "^":3, 
        ")":4}

    operator_stack = []
    operand_stack = []

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

    try:
        expr = expr.split(" ")
        for token in expr:
            if token.isdigit():
                operand_stack.append(int(token))
            elif token in "+-*/^":
                # Parse operator
                while operator_stack and precedence[token] <= precedence[operator_stack[-1]]:
                    apply_operator()
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack[-1] != "(":
                    apply_operator()
                operator_stack.pop()
            elif token == "!":
                apply_factorial()
            else:
                raise ParserError()

        while operator_stack:
            apply_operator()

        return operand_stack[0]

    except:
        raise ParserError()
