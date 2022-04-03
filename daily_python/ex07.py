def ubbi_dubbi(eng_word: str):
    temp_list = []
    for w in eng_word:
        if w in "aeiouAEIOU":
            temp_list.append(f"ub{w}")
        else:
            temp_list.append(w)
    return f"입력하신 {eng_word}의 ubbi_dubbi 버전은 {''.join(temp_list)}입니다."


def user_input():
    user_word = input("원하는 영어를 입력하세요 : ")
    if user_word.encode().isalpha():
        print(ubbi_dubbi(user_word))
    else:
        user_input()


user_input()
