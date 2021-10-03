n = int(input())
pre = [input() for _ in range(n)]
for _ in range(n - 1):
    pre.remove(str(input()))
print(pre[0])

# hash로 풀기
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0
for key, val in p.items:
    if val == 1:
        print(key)
        break