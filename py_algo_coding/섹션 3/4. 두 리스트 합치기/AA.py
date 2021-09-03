# n = int(input())
# n_list = [int(i) for i in input().split()]
# m = int(input())
# m_list = [int(i) for i in input().split()]
# m_list.extend(n_list)
# m_list.sort()

# print(" ".join(map(str, m_list)))

n = int(input())
n_list = [i for i in input().split()]
m = int(input())
m_list = [i for i in input().split()]
m_list.extend(n_list)
m_list.sort()

print(" ".join(m_list))
