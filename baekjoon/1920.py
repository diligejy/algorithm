import sys
n = int(sys.stdin.readline().rstrip())
n_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))


def binary(l, n_list, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if l == n_list[mid]:
        return 1
    elif l < n_list[mid]:
        return binary(l, n_list, start, mid-1)
    else:
        return binary(l, n_list, mid+1, end)


for ele in m_list:
    start = 0
    end = len(n_list) - 1
    print(binary(ele, n_list, start, end))
