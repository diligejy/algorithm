import random

n, k = map(int, input().split())
num_list = [int(i) for i in input().split()]
sum_list = set()

for i in range(n):
    for j in range(i + 1, n):
        for l in range(j + 1, n):
            sum_list.add(num_list[i] + num_list[j] + num_list[l])

print(sorted(list(sum_list), reverse=True)[k - 1])
