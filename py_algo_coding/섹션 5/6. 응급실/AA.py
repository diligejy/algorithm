from collections import deque

n, m = map(int, input().split())

cnt = 0
n_list = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
n_list = deque(n_list)
while True:
    cur = n_list.popleft()
    if any(cur[1] < x[1] for x in n_list):
        n_list.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)
