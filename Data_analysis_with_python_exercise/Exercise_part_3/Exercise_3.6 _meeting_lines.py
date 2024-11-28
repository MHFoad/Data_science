import numpy as np
def meeting_lines(a1, b1, a2, b2):
    """
    Finds the intersection point of two lines y = a1*x + b1 and y = a2*x + b2.

    Parameters:
        a1, b1: Coefficients of the first line.
        a2, b2: Coefficients of the second line.
        X is the variable vectors.

    Returns:
        (x, y): A tuple representing the point of intersection.
    """
    # coefficient matrix
    A=np.array([[-a1,1],[-a2,1]])

    #constant vectors
    B=np.array([b1,b2])
    # Solve for x and y
    x, y = np.linalg.solve(A, B)
    return x, y


def main():
    # Example coefficients
    a1, b1 = 3, 7
    a2, b2 = 5, -8

    x, y = meeting_lines(a1, b1, a2, b2)
    print(f"The lines meet at ({x}, {y})")

main()