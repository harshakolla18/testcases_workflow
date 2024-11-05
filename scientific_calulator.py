import math

class ScientificCalculator:
        def sin(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a number")
        return math.sin(math.radians(x))

    def cos(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a number")
        return math.cos(math.radians(x))

    def tan(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a number")
        return math.tan(math.radians(x))

    def sqrt(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a number")
        if x < 0:
            raise ValueError("Input must be a non-negative number")
        return math.sqrt(x)

    def log(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a number")
        if x <= 0:
            raise ValueError("Input must be a positive number")
        return math.log(x)

    def exp(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a number")
        return math.exp(x)

