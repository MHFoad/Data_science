#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from the triangle module
    side1 = 3
    side2 = 4
    print("Hypotenuse:", triangle.hypotenuse(side1, side2))  # Output: 5.0
    
    base = 5
    height = 3
    print("Area:", triangle.area(base, height))  # Output: 7.5

if __name__ == "__main__":
    main()
