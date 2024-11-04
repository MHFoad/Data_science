from math import gcd
class Rational:
    def __init__(self,numerator,denominator):
        if denominator==0:
            raise ValueError("Denominator cannot be zero.")
        common_divisor = gcd(numerator, denominator)
        self.numerator=numerator//common_divisor
        self.denominator=denominator//common_divisor
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    # Addition
    def __add__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        return NotImplemented
    #subtraction
    def __sub__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        return NotImplemented
    #multiplication
    def __mul__(self, other):
        if isinstance(other,Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Rational(new_numerator, new_denominator)
        return NotImplemented

    # Division
    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.denominator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator)
        return NotImplemented

    # Less than
    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        return NotImplemented

    # Greater than
    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        return NotImplemented

    # Equality
    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return NotImplemented
    #Not Equal
    def __ne__(self, other):
        if isinstance(other,Rational):
            return self.numerator != other.numerator and self.denominator != other.denominator
        return NotImplemented


r1=Rational(1,4)
r2=Rational(2,3)
print(r1)
print(r2)
print(r1*r2)
print(r1/r2)
print(r1+r2)
print(r1-r2)
print(Rational(1,2) == Rational(2,4))
print(Rational(1,2) != Rational(5,7))
print(Rational(2,2) > Rational(2,4))
print(Rational(1,2) < Rational(2,4))
