import sys


def list_interval_sum():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    num_list = list(map(int, sys.stdin.readline().rstrip().split()))
    s = [0]
    for i in range(n):
        s.append(num_list[i] + s[i])

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().rstrip().split())
        print(s[j] - s[i-1])

list_interval_sum()
