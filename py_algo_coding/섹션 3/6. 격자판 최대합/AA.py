n = int(input())
d_list = []
for _ in range(n):
    d_list.append(list(map(int, input().split())))


sum_list = []
horizontal_sum = 0
vertical_sum = 0
left_diagonal_sum = 0
right_diagonal_sum = 0
for i in range(len(d_list)):
    for j in range(len(d_list)):
        horizontal_sum += d_list[i][j]
        vertical_sum += d_list[j][i]
        if i == j:
            left_diagonal_sum += d_list[i][j]
        elif i + j == 4:
            right_diagonal_sum += d_list[i][j]
    sum_list.append(horizontal_sum)
    sum_list.append(vertical_sum)
    sum_list.append(left_diagonal_sum)
    sum_list.append(right_diagonal_sum)
    horizontal_sum = 0
    vertical_sum = 0

print(max(sum_list))
