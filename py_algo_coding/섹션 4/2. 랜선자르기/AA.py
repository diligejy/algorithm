def Count(len):
    cnt = 0
    for x in k_list:
        cnt += x // len
    return cnt


k, n = map(int, input().split())
k_list = list(int(input()) for _ in range(k))
line = []
res = 0

lt = 1
rt = max(k_list)

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
