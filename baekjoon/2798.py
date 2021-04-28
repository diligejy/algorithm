import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))


result = 0
for i in range(len(n_list) - 2):
    for j in range(i+1, len(n_list) - 1):
        for k in range(j+1, len(n_list)):
            sum_value = n_list[i] + n_list[j] + n_list[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)
