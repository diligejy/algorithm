n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if n_list[mid] == m:
        print(mid + 1)
        break
    elif n_list[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
