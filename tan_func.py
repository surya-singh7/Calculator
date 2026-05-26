import math

def tan_function(x):

    if x % 180 == 90:
        return "Undefined Value."

    return math.tan(math.radians(x))