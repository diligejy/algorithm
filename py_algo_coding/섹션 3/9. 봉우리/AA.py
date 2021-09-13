# def padding(n, n_list):
#     cnt = 0

#     pad_list = [0 for _ in range(n + 2)]
#     n_list.insert(0, pad_list)
#     n_list.append(pad_list)

#     for idx in range(1, n + 1):
#         n_list[idx].insert(0, 0)
#         n_list[idx].append(0)

#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             print(
#                 n_list[2][1]
#                 == max(
#                     n_list[1][1],
#                     n_list[1][0],
#                     n_list[1][2],
#                     n_list[0][1],
#                     n_list[2][1],
#                 )
#             )
# if n_list[i][j] == max(
#     [
#         n_list[i][j],
#         n_list[i - 1][j],
#         n_list[i + 1][j],
#         n_list[i][j + 1],
#         n_list[i][j - 1],
#     ]
# ):
#     cnt += 1
# return cnt


# n = int(input())
# n_list = [list(map(int, input().split())) for _ in range(n)]
# print(padding(n, n_list))
# print(n_list)

# print(pad_list)

# 두 번째 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
n_list.insert(0, [0] * n)
n_list.append([0] * n)
for sub in n_list:
    sub.insert(0, 0)
    sub.append(0)

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(n_list[i][j] > n_list[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1
print(cnt)
