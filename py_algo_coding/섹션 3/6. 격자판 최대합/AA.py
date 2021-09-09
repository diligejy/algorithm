# n = int(input())
# d_list = []
# for _ in range(n):
#     d_list.append(list(map(int, input().split())))


# sum_list = []
# horizontal_sum = 0
# vertical_sum = 0
# left_diagonal_sum = 0
# right_diagonal_sum = 0
# for i in range(len(d_list)):
#     for j in range(len(d_list)):
#         horizontal_sum += d_list[i][j]
#         vertical_sum += d_list[j][i]
#         if i == j:
#             left_diagonal_sum += d_list[i][j]
#         elif i + j == n - 1:
#             right_diagonal_sum += d_list[i][j]
#     sum_list.append(horizontal_sum)
#     sum_list.append(vertical_sum)
#     sum_list.append(left_diagonal_sum)
#     sum_list.append(right_diagonal_sum)
#     horizontal_sum = 0
#     vertical_sum = 0

# print(max(sum_list))

# 두 번째 풀이
n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += n_list[i][j]
        sum2 += n_list[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += n_list[i][i]
    sum2 += n_list[i][n - i - 1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)
