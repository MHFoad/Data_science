import numpy as np
def most_frequent_first(arr, c):
    # Get the values in column `c`
    column = arr[:, c]

    # Get the unique values and their counts
    unique_values, counts = np.unique(column, return_counts=True)

    # Create a dictionary mapping each value to its frequency
    value_to_count = dict(zip(unique_values, counts))

    # Sort the rows based on the frequency of the values in column `c`
    sorted_indices = np.argsort([-value_to_count[val] for val in column])

    # Return the sorted array
    return arr[sorted_indices]


# Test the function
a = np.array([
    [5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
    [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
    [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
    [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
    [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
    [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
    [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
    [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
    [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
    [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]
])

# Test the function with column index -1 (last column)
result = most_frequent_first(a, -1)
print(result)
