n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
res = 0
left = right = n // 2

ans_list = []

# left, right flag 두개로 split하는 건 혁신적인데?

for i in range(n):
    for j in range(left, right + 1):
        res += n_list[i][j]
    if i < n // 2:
        left -= 1
        right += 1
    else:
        left += 1
        right -= 1
