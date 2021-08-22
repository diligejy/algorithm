import sys

# sys.stdin = open("input.txt", "rt")
# n, k = map(int, input().split())
# cnt = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         cnt += 1
#     if cnt == k:
#         print(i)
#         break
# else:
#     print(-1)

n, k = map(int, input().split())
# 풀이 2
def sol(n, k):
    div_list = [i for i in range(1, n + 1) if n % i == 0]

    if len(div_list) < k:
        return -1
    else:
        return div_list[k - 1]


print(sol(n, k))
