def find_longest_word(words):
    words = words.split(" ")
    return sorted(words, key=lambda x: len(x))[-1]


print(find_longest_word("this is nonononononononono"))

# def strsort(word: str):
#     return "".join(sorted(word))


# print(strsort("cba"))
