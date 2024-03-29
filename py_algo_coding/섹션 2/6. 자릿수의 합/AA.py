"""
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.
"""


def digit_sum(x):
    res = 0
    for i in x:
        res += int(i)
    return res


n = int(input())
num_list = list(input().split())
max = -1000
ans = 0

for val in num_list:
    if max < digit_sum(val):
        max = digit_sum(val)
        ans = val

print(ans)
