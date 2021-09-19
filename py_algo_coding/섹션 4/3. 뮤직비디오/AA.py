n, m = map(int, input().split())
n_list = [int(i) for i in input().split()]

lt = 1
rt = sum(n_list)
maxx = max(n_list)


def Count(capacity):
    cnt = 1
    sum = 0
    for n in n_list:
        if sum + n > capacity:
            cnt += 1
            sum = n
        else:
            sum += n
    return cnt


cnt = 0
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
