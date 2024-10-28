def remove_punctuation(word):
    """
    Helper function to remove punctuation from the ends of a word.
    """
    punctuation_chars = """!"#$%&'()*,-./:;?@[]_"""
    return word.strip(punctuation_chars )
def word_frequencies(filename):
   # word_freq = {}
    with open (filename, "r") as file:
        words=[remove_punctuation(word) for line in file for word in line.split()]

        word_freq={word:words.count(word) for word in set(words)}
        return word_freq


result=word_frequencies("./alice.txt")
for word, count in result.items():
    print("{}\t{}".format(word,count))
