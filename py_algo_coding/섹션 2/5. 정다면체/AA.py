# 1번 - 내가 푼 풀이
from collections import Counter

n, m = map(int, input().split())

n_list = [i for i in range(1, n + 1)]
m_list = [i for i in range(1, m + 1)]

ans_list = []
for i in n_list:
    for j in m_list:
        ans_list.append(i + j)

for i in Counter(ans_list).most_common():
    if i[1] == Counter(ans_list).most_common(1)[0][1]:
        print(i[0], end=" ")

# 2번 - 영상 풀이
n, m = map(int, input().split())
cnt = [0] * (n + m + 3)
max = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] = cnt[i + j] + 1

for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=" ")
