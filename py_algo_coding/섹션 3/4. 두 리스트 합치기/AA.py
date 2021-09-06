"""
sort - nlogn
"""
# n = int(input())
# n_list = [i for i in input().split()]
# m = int(input())
# m_list = [i for i in input().split()]
# m_list.extend(n_list)
# m_list.sort()

# print(" ".join(m_list))

"""
두 번째 풀이 O(n)으로 풀기
"""

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

p1 = p2 = 0
sol_list = []

while p1 < n and p2 < m:
    if n_list[p1] <= m_list[p2]:
        sol_list.append(n_list[p1])
        p1 += 1
    else:
        sol_list.append(m_list[p2])
        p2 += 1

if p1 < n:
    sol_list += n_list[p1:]
elif p2 < m:
    sol_list += m_list[p2:]

for x in sol_list:
    print(x, end=" ")
