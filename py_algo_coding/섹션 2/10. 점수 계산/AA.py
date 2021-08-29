n = int(input())
scores = list(map(int, input().split()))

s = 0
total = 0
for i in scores:
    if i == 1:
        s += 1
        total += s
    else:
        s = 0
print(total)
