import sys


def solve():
    num_list = []
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        num = int(sys.stdin.readline().rstrip())
        if num != 0:
            num_list.append(num)
        else:
            num_list.pop()
    return sum(num_list)


print(solve())
