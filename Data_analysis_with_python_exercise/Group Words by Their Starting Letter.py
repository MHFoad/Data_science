def group_of_words(given_list):
    word_dict={letter:{word:len(word) for word in given_list if word.startswith(letter)}
               for letter in sorted({word[0] for word in given_list})
               }
    return word_dict
words = ["apple", "apricot", "banana", "cherry", "date", "elderberry", "fig", "grape", "guava"]
D=group_of_words(words)
print (D)

