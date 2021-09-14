n_list = [list(map(int, input().split())) for _ in range(7)]

print(n_list)

cnt = 0
for i in range(3):
    for j in range(7):
        tmp = n_list[j][i : i + 5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if n_list[i + k][j] != n_list[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)
