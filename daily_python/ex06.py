def exercise(*words):
    return_list = []

    temp_list = []

    for word in words:
        temp_list.append(word.split(" "))

    for idx, w in enumerate(temp_list):
        res_list = []
        for i, s_w in enumerate(w):
            res_list.append(temp_list[i][idx])
        return_list.append(" ".join(res_list))
    return return_list


print(exercise(*["abc def ghi", "jkl mno pqr", "stu vwx yz"]))

# def pl_sentence(sentence):
#     output = []
#     words = sentence.split()
#     for word in words:
#         if not word.encode().isalpha():
#             print(f"{word}는 영어로 되어있지 않습니다.")
#         if word[0] in "aeiouAEIOU":
#             output.append(f"{word}way")
#         else:
#             output.append(f"{word[1:]}{word[0]}ay")
#     return " ".join(output)


# print(pl_sentence("This is a test translation"))
