import random

n, k = map(int, input().split())
num_list = [int(i) for i in input().split()]
sum_list = []

for i in range(len(num_list) - 2):
    for j in range(i + 1, len(num_list) - 1):
        for l in range(j + 1, len(num_list)):
            sum_list.append(num_list[i] + num_list[j] + num_list[l])

print(sorted(sum_list)[k])
