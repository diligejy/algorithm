def move(n, n_list, m, m_list):

    for i in m_list:
        row, direction, num = i

        while num > n:
            num -= n
        tmp_list = []

        if direction == 1:
            for j in range(num):
                tmp = n_list[row - 1].pop()
                tmp_list.append(tmp)
            tmp_list = tmp_list[::-1]
            for idx in range(len(tmp_list)):
                n_list[row - 1].insert(idx, tmp_list[idx])
        else:
            for j in range(num):
                tmp = n_list[row - 1].pop(0)
                tmp_list.append(tmp)
            n_list[row - 1].extend(tmp_list)

    return n_list


def cal(n, n_list):
    left = 0
    right = n - 1
    res = 0
    for idx in range(n):
        for j in range(left, right + 1):
            res += n_list[idx][j]
        if idx < n // 2:
            left += 1
            right -= 1
        else:
            left -= 1
            right += 1
    return res


n = int(input())
n_list = list(list(map(int, input().split())) for _ in range(n))
m = int(input())
m_list = list(list(map(int, input().split())) for _ in range(m))

print(cal(n, move(n, n_list, m, m_list)))
