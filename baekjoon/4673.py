
def d(n):
    for i in str(n):
        n += int(i)
    return n


"""
셀프 넘버 - d(n)으로 구할 수 없는 숫자

전략
1부터 10000까지의 숫자에서 셀프 넘버를 제거한다.
"""

del_list = []
for num in range(1, 10001):
    k = d(num)
    del_list.append(k)

for num in range(1, 10001):
    if num in del_list:
        pass
    else:
        print(num)
