n, m = map(int, input().split())
n_list = list(map(int, input().split()))

lt = 0
rt = 1
tot = n_list[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += n_list[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= n_list[lt]
        lt += 1
    else:
        tot -= n_list[lt]
        lt += 1

print(cnt)
