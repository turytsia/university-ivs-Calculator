import sys
import os
from enum import Enum
import ast


# class TokenTypes(Enum):
#     OPERATOR_PLUS = 0
#     OPERATOR_MINUS = 1
#     OPERATOR_MULTIPLY = 2
#     OPERATOR_DIVIDE = 3
#     OPERATOR_POW = 4
#     OPERATOR_OPEN_BRACE = 5
#     OPERATOR_CLOSE_BRACE = 6
#     OPERATOR_FACTORIAL = 7
#     DIGIT = 8
#     DOLLAR = 9
#     ERR = 99


# class Token:
#     def __init__(self, value = None) -> None:
            
#         self.value = value
#         if value is None:
#             self.type = TokenTypes.DOLLAR
#         elif value == "+":
#             self.type = TokenTypes.OPERATOR_PLUS
#         elif value == "-":
#             self.type = TokenTypes.OPERATOR_MINUS
#         elif value == "*":
#             self.type = TokenTypes.OPERATOR_MULTIPLY
#         elif value == "/":
#             self.type = TokenTypes.OPERATOR_DIVIDE
#         elif value == "^":
#             self.type = TokenTypes.OPERATOR_POW
#         elif value == "!":
#             self.type = TokenTypes.OPERATOR_FACTORIAL
#         elif value == "(":
#             self.type = TokenTypes.OPERATOR_OPEN_BRACE
#         elif value == ")":
#             self.type = TokenTypes.OPERATOR_CLOSE_BRACE
#         else:
#             try:
#                 self.value = int(value)
#                 self.type = TokenTypes.DIGIT
#             except ValueError:
#                 self.type = TokenTypes.ERR

#     def __repr__(self) -> str:
#         return f"Token( {self.value}, {self.type.name} )"


# class Lexer:
#     def __init__(self, expression: str) -> None:
#         self.expression = expression

#     def get_token(self):
#         for token in self.expression.split(" "):
#             yield Token(token)
#         yield Token()
    

# class OpNode:
#     def __init__(self, left: Token, token: Token, right: Token = None) -> None:
#         self.token = token
#         self.left = left
#         self.right = right
    
#     def __repr__(self) -> str:
#         return f"({self.operator}: {self.left}, {self.left})"
    

# class ExprNode:
#     def __init__(self, token: Token) -> None:
#         self.token = token

#     def __repr__(self) -> str:
#         return f"({self.token})"

# class PrecStack:
#     def __init__(self) -> None:
#         self.root = None

#     def push(self, token:Token):
#         print(f"inserting token {token} to the stack")
#         if self.root is None:
#             if token.type == TokenTypes.DIGIT:
#                 self.root = ExprNode(token)
#             else:
#                 raise ValueError("Error, expected digit")
#         else:
#             node = self.root

#             while node is not None:
#                 if isinstance(node, ExprNode):
 
#             if token.type != TokenTypes.DIGIT:
#                 self.root = OpNode(self.root., token)
#             else:
#                 raise ValueError("Error, expected operation")

#     def reduce(self):

#         print(f"reducing by rule")
      
#         pass

#     def top(self):
#         return self.stack[-1]


# class Parser:

#     # OPERATOR_PLUS = 0
#     # OPERATOR_MINUS = 1
#     # OPERATOR_MULTIPLY = 2
#     # OPERATOR_DIVIDE = 3
#     # OPERATOR_POW = 4
#     # OPERATOR_OPEN_BRACE = 5
#     # OPERATOR_CLOSE_BRACE = 6
#     # OPERATOR_FACTORIAL = 7
#     # DIGIT = 8

#     PREC = [
#         [">", ">", "<", "<", "<", "<", "<", "<", "<",">"],
#         [">", ">", "<", "<", "<", "<", "<", "<", "<",">"],
#         [">", ">", ">", ">", "<", "<", "<", "<", "<",">"],
#         [">", ">", ">", ">", "<", "<", "<", "<", "<",">"],
#         ["", "", "", "", "", "<", "", "", "<",">"],
#         ["", "", "", "", "", "<", "<", "", "<", ""],
#         [">", ">", ">", ">", ">", "", ">", ">", "",">"],
#         [">", ">", ">", ">", ">", "", ">", ">", "", ">"],
#         [">", ">", ">", ">", ">", "", ">", ">", "", ">"],
#         ["<", "<", "<", "<", "<", "<", "", "<", "<", "="]
#     ]

#     def __init__(self) -> None:
#         pass

#     def parse(self, input):
#         lexer = Lexer(input)
#         stack = PrecStack()
#         tokenReader = lexer.get_token()

#         while True:
#             try:
#                 token = next(tokenReader)
#                 if token.type == TokenTypes.ERR:
#                     return False
                
#                 action = self.PREC[stack.top().value][token.type.value]

#                 print(f"applying rule \'{action}\'")

#                 if action == "<":
#                     stack.push(token)
#                 elif action == ">":
#                     stack.reduce()
#                 elif action == "=":
#                     return True
#                 else:
#                     return False


#             except StopIteration:
#                 break

#         return True


def main():
    # parser = Parser()
    
    for line in sys.stdin:
        os.system('cls')
        tree = ast.parse(line, mode="eval")
        print(ast.dump(tree))


if __name__ == '__main__':
    main()
