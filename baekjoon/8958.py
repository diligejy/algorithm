def solve():
    s = input()
    cnt = 0
    rst = 0
    for c in s:
        if c == 'O':
            cnt += 1
            rst += cnt
        else:
            cnt = 0
    print(rst)


t = int(input())
for _ in range(t):
    solve()
