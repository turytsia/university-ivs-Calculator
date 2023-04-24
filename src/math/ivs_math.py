class ZeroDivisonError(Exception):
    def __init__(self):
        super().__init__("Cannot divide by zero")

# returns the sum of a and b
def sum(a, b):
    return a + b

# returns the difference between a and b
def sub(a, b):
    return a - b

# returns the product of a and b
def mult(a, b):
    return a * b

# returns the quotient of a and b
def div(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisonError()

# returns the factorial of a (the product of all positive integers up to a)
def fac(a):
    if a == 0 or a == 1:
        return 1
    return a * fac(a-1)

# returns the result of raising a to the power of b
def exp(a, b):
    return a ** b

# returns the result of square root of a
def square_root(a):
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