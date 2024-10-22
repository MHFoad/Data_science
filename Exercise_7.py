import math


def main():
    def triangle():
        base = int(input("Give base of the triangle: "))
        height = int(input("Give height of the triangle: "))
        return .5 * base * height

    def rectangle():
        width = int(input("Give width of the rectangle: "))
        height = int(input("Give height of the rectangle: "))
        return width * height

    def circle():
        radius = int(input("Give radius of the circle:"))
        return math.pi * (radius ** 2)

    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape == "triangle":
            print(f"The area is {triangle():.6f}")
        elif shape == "rectangle":
            print(f"The area is {rectangle():.6f}")
        elif shape == "circle":
            print(f"The area is {circle():.6f}")
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
