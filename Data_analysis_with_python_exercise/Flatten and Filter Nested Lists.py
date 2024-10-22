""" Task: Write a function flatten_and_filter that flattens a nested list (a list of lists) into a single list, but only keeps elements that satisfy certain conditions.

Flatten the list of lists.
Keep only elements that are divisible by 3 and greater than 10.
Return the resulting list.
"""
def flatten_and_filter(nested_list):
    n=len(nested_list)
    return [element for item in nested_list for element in item if
            element % 3 == 0 and element > 10]
    #return [nested_list[i][j] for i in range (n) for j in range (n) if nested_list[i][j]%3==0 and nested_list[i][j]>10 ]

nested_list = [
    [4, 9, 12],
    [15, 7, 18],
    [21, 6, 24]
]
result = flatten_and_filter(nested_list)
print(result)