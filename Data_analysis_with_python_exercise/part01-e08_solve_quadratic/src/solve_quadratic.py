#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2
def main():
    print(solve_quadratic(1, -3, 2)) # Expected: (2.0, 1.0)
    print(solve_quadratic(1, 2, 1))   # Expected: (-1.0, -1.0)

if __name__ == "__main__":
    main()
