# def other_pig_latin(eng_word: str):
#     """
#     - 모음이 2개 이상 있을 경우 끝에 way
#     - 모음이 1개만 있을 경우 첫 글자를 마지막으로 옮기고 ay를 붙이기
#     - 모음 없을 경우도 마찬가지
#     """
#     res = 0
#     for i in set(eng_word):
#         if i in "aeiouAEIOU":
#             res += 1
#     if res > 1:
#         return f"{eng_word}way"
#     else:
#         return f"{eng_word[1:]}{eng_word[0]}ay"


# def get_user_input():
#     user_input = input("영어 단어를 입력하세요 : ")
#     if user_input.encode().isalpha():
#         print(other_pig_latin(user_input))
#     else:
#         get_user_input()


# get_user_input()


def pig_latin(eng_word: str):
    """
    - 모음(a, e, i, o, u)로 시작시 끝에 way추가
    - 자음으로 시작시 첫 글자를 마지막으로 옮기고 끝에 ay를 추가
    """

    if eng_word[0] in "aeiouAEIOU":
        return eng_word + "way"
    else:
        return eng_word[1:] + eng_word[0] + "ay"


def get_user_input():
    user_input = input("영어 단어를 입력하세요 : ")
    if user_input.encode().isalpha():
        print(pig_latin(user_input))
    else:
        get_user_input()


get_user_input()
