import sys

def file_count(filename):
    with open (filename, "r") as file:
        line_count = 0
        word_count = 0
        char_count = 0
        for line in file:
            line_count += 1  # Increment line count for each line
            words = line.split()  # Split the line into words by whitespace
            word_count += len(words)  # Add the number of words in the current line
            char_count += len(line)  # Add the number of characters in the current line (including whitespace)

    return (line_count, word_count, char_count)

def main():
    for filename in sys.argv[1:]:
        line_count, word_count, char_count = file_count(filename)
        print(f"{line_count}\t{word_count}\t{char_count}\t{filename}")

if __name__ == "__main__":
    main()
