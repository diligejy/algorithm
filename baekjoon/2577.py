product_num = 1
for i in range(3):
    product_num *= int(input())

product_num = str(product_num)


counter = {}
for num in product_num:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cnt_list = []
for num in num_list:
    if str(num) in counter.keys():
        cnt_list.append(counter[str(num)])
    else:
        cnt_list.append(0)

for i in cnt_list:
    print(i)
