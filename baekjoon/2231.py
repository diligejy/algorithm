import sys
n = int(sys.stdin.readline().rstrip())


def solve(n):
    for i in range(1, n):
        cnt = i
        test = i
        while True:
            cnt += (test % 10)
            test = test // 10
            if test == 0:
                break
        if cnt == n:
            print(i)
            return
    print(0)


solve(n)
