def mysum(*numbers):
    res = 0
    for i in numbers:
        res += i
    print(res)
    return res


mysum(1, 2, 3)
