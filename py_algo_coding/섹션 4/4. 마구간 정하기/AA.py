n, c = map(int, input().split())
n_list = [int(input()) for _ in range(n)]
n_list.sort()


def Count(len):
    cnt = 1
    ep = n_list[0]
    for i in range(1, n):
        if n_list[i] - ep >= len:
            cnt += 1
            ep = n_list[i]
    return cnt


lt = 1
rt = n_list[n - 1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
