from collections import deque

n, m = map(int, input().split())
n_list = [int(i) for i in input().split()]
n_list.sort()
n_list = deque(n_list)
cnt = 0

while n_list:
    if len(n_list) == 1:
        cnt += 1
        break

    if n_list[0] + n_list[-1] > m:
        n_list.pop()
        cnt += 1
    else:
        n_list.popleft()
        n_list.pop()
        cnt += 1
print(cnt)
