# nums = [input().split() for x in range(int(input()))]
# import sys
# input = sys.stdin.readline
# nums = [input().split() for _ in range(int(input()))]
# nums = sorted(nums, key=lambda x: [int(x[0]), int(x[1])])
# for n in nums:
#     print(n[0], n[1])

N = 100000

def solve():
    n = int(input())
    arr = []
    for _ in range(n):
        x, y = [int(x) + N for x in input().split()]
        tmp = x * 2 * N + y
        arr.append(tmp)
    arr.sort()
    print(arr)
    for item in arr:
        x = item // (2 * N)
        y = item % (2 * N)
        print(x - N, y - N)


solve()
