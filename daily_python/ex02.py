# 매개변수 : 여러 자료형 구성된 리스트, 그 값을 더해서 리턴하는 함수
# 숫자 또는 숫자로 변환해서 더할 수 있는 것들만 더하기
def mysum(*lists):
    res = 0
    for i in lists:
        if type(i) == int or i.isdigit():
            res += int(i)
    return res


print(mysum(*["apple", "1", "3", 5, "no", "카라"]))

# 단어 리스트 매개변수 & (가장 짧은 단어 길이, 가장 긴 단어 길이, 단어 길이 평균) 튜플 리턴
# def mysum(*words):
#     res = 0
#     words = [len(i) for i in words]
#     words.sort()
#     for i in words:
#         res += i
#     avg = res / len(words)
#     return (words[0], words[-1], avg)


# print(mysum(*["apple", "good", "no"]))


# 매개변수 숫자 리스트 & 평균
# def mysum(*numbers):
#     res = 0
#     for i in numbers:
#         res += i
#     avg = res / len(numbers)
#     return avg


# 두 번째 매개변수 지정 안하고 숫자 알아서 더하도록
# print(mysum(*[1, 2, 3]))
# def mysum(*numbers):
#     res = 0
#     for i in numbers:
#         res += i
#     return res


# print(mysum(*[1, 2, 3], 4))


# def mysum(*numbers):
#     res = 0
#     for i in numbers:
#         res += i
#     print(res)
#     return res


# mysum(1, 2, 3)
