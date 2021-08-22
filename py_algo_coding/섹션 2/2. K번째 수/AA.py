t = int(input())


def sol(t, s, e, k):
    num_list = [int(i) for i in input().split()]
    new_num_list = num_list[s - 1 : e]
    print("#%d %d" % (t + 1, sorted(new_num_list)[k - 1]))


for i in range(t):
    n, s, e, k = map(int, input().split())
    sol(i, s, e, k)
