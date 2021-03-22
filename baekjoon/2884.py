h, m = input().split()
h, m = int(h), int(m)

m = m - 45
if m < 0:
    m = m + 60
    h = h - 1
    if h < 0:
        h = h + 24


print(h, m)

# 풀이 2
H, M = [int(x) for x in input().split()]
T = ((H * 60 + M - 45) + (24 * 60)) % (24 * 60)
