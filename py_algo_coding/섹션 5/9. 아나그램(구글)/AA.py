def isAnagram(first_word: str, second_word: str) -> str:
    first_res = dict()
    second_res = dict()
    for word in first_word:
        first_res[word] = first_res.get(word, 0) + 1
    for word in second_word:
        second_res[word] = second_res.get(word, 0) + 1

    for i in first_res.keys():
        if i in second_res.keys():
            if first_res[i] != second_res[i]:
                print("NO")
                break
        else:
            print("NO")
            break
    else:
        print("YES")


first = input()
second = input()

isAnagram(first, second)
