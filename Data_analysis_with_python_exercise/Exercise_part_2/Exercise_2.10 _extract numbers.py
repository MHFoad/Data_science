def extract_numbers(input_string):
    numbers = []  # Initialize an empty list to store the numbers
    words = input_string.split()  # Split the string into words based on whitespace

    for word in words:
        try:
            # Try to convert to an integer
            num = int(word)
            numbers.append(num)  # If successful, add to the list
        except ValueError:
            try:
                # If it fails, try converting to a float
                num = float(word)
                numbers.append(num)  # If successful, add to the list
            except ValueError:
                # If both conversions fail, skip this word
                continue

    return numbers  # Return the list of numbers

# Example usage
print(extract_numbers("abd 123 1.2 test 13.2 -1"))
