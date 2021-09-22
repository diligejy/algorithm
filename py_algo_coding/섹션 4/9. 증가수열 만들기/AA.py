n = int(input())
n_list = [int(i) for i in input().split()]
res = ""
largest = 0
lt = 0
rt = n - 1
tmp = []

while lt <= rt:
    if n_list[lt] > largest:
        tmp.append((n_list[lt], "L"))
    if n_list[rt] > largest:
        tmp.append((n_list[rt], "R"))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        largest = tmp[0][0]
        if tmp[0][1] == "L":
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
