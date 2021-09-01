n = int(input())

num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))


price_list = []
for num in num_list:
    if num[0] == num[1] == num[2]:
        price_list.append(10000 + num[0] * 1000)
    elif (num[0] == num[1]) or (num[2] == num[0]):
        price_list.append(1000 + num[0] * 100)
    elif num[1] == num[2]:
        price_list.append(1000 + num[1] * 100)
    else:
        price_list.append(max(num) * 100)

print(max(price_list))
