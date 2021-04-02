import sys


def solve(num: int):
    """
    n이 주어졌을 때 n을 1, 2, 3의 합으로 나타내는 방법의 수
    """
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    return solve(num-1) + solve(num-2) + solve(num-3)


input = sys.stdin.readline
nums = [int(input()) for _ in range(int(input().rstrip()))]
for i in nums:
    print(solve(i))
