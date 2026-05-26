import math

def factorial_function(x):

    if x < 0:
        return "Error! Negative number not allowed."

    if x != int(x):
        return "Error! Only integer values allowed."

    return math.factorial(int(x))