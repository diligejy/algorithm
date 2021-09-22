n = int(input())
input_list = [int(i) for i in input().split()]
input_list.insert(0, 0)
sub_list = [0 for _ in range(n)]

for i in range(1, n + 1):
    for j in range(n):
        if input_list[i] == 0 and sub_list[j] == 0:
            sub_list[j] = i
            break
        if sub_list[j] == 0:
            input_list[i] -= 1

for x in sub_list:
    print(x, end=" ")
