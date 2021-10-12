import sys


def DFS(L, sum, tsum):
    global result
    if sum + (total - tsum) < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L + 1, sum + n_list[L], tsum + n_list[L])
        DFS(L + 1, sum, tsum + n_list[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    n_list = [int(input()) for _ in range(n)]
    result = -2147000
    total = sum(n_list)
    DFS(0, 0, 0)
    print(result)
