#Fraction

class Fraction:

    def __init__(self, fraction):
        self.fraction = fraction
        if isinstance(self.fraction, str):
            raise Exception("Need to pass a number")

    def __add__(self, other):
        if isinstance(other, str):
            raise Exception("Need to pass a number")
        return round(self.fraction + other.__dict__["fraction"], 3)

    def __sub__(self, other):
        if isinstance(other, str):
            raise Exception("Need to pass a number")
        return round(self.fraction - other.__dict__["fraction"], 3)

    def __mul__(self, other):
        if isinstance(other, str):
            raise Exception("Need to pass a number")
        return round(self.fraction * other.__dict__["fraction"], 3)

    def __truediv__(self, other):
        if isinstance(other, str):
            raise Exception("Need to pass a number")
        try:
            return round(self.fraction / other.__dict__["fraction"], 3)
        except ZeroDivisionError:
            return "Infinitely large number"

x = Fraction(1/2)
y = Fraction(1/4)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
