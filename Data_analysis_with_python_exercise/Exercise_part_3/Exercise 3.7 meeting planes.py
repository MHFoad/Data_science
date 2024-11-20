import numpy as np
def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    """
    Finds the planes meet of three lines z = a1*y + b*1x +c1 , z = a2*y + b2*x +c2 and z = a3*y + b3*x +c3

    Parameters:
        a1, b1, c1: Coefficients of the first line.
        a2, b2, c2: Coefficients of the second line.
        a3, b3, c3: Coefficients of the third line.


    Returns:
        (x, y, z): A tuple representing the planes meet point of intersection.
    """
    # coefficient matrix
    A=np.array([[-a1,-b1, 1],[-a2,-b2, 1], [-a3,-b3, 1]])

    #constant vectors
    B=np.array([c1,c2, c3])
    # Solve for x and y
    x, y, z = np.linalg.solve(A, B)
    return x, y ,z


def main():
    # Example coefficients
    a1, b1, c1 = 1 , 2, -1
    a2, b2, c2 = 3, 1, 2
    a3, b3, c3= 2, -3, 1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"The planes meet at ({x}, {y}, {z})")

main()