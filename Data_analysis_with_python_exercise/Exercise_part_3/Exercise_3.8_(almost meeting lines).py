import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    # Coefficient matrix A and constant vector B
    A = np.array([[-a1, 1], [-a2, 1]])
    B = np.array([b1, b2])

    try:
        # Try solving the exact system
        result = np.linalg.solve(A, B)
        return tuple(result), True  # Exact meeting point exists
    except np.linalg.LinAlgError:
        # Use least squares to find the closest point
        result, _, _, _ = np.linalg.lstsq(A, B, rcond=None)
        return tuple(result), False  # Approximate meeting point

# Example usage
(x, y), exact = almost_meeting_lines(1, 2, -1, 0)
print(f"x: {x}, y: {y}, exact: {exact}")
