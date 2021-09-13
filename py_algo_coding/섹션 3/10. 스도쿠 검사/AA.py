def check(n_list):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[n_list[i][j]] = 1
            ch2[n_list[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[n_list[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


n_list = [list(map(int, input().split())) for _ in range(9)]

if check(n_list):
    print("YES")
else:
    print("NO")
