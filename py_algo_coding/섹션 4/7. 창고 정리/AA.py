l = int(input())
l_list = [int(i) for i in input().split()]
m = int(input())

l_list.sort()
for _ in range(m):
    l_list[len(l_list) - 1] -= 1
    l_list[0] += 1
    l_list.sort()

print(l_list[len(l_list) - 1] - l_list[0])
