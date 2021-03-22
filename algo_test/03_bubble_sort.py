
"""
핵심 로직 : 첫 번째 요소와 두 번쨰 요소를 비교해서 두 번째 요소가 더 작으면 첫 번째 요소와 자리를 바꿈
"""

numbers = [7, 3, 2, 9]
first = numbers[0]
second = numbers[1]


def bubble(first, second):
    temp = first
    first = second
    second = temp
    return first, second


print(first, second)
print(bubble(7, 3))
