# 2^n -x => 2^n - 2* x
# 2^n -x = a
# 2^n = x + a
# n = ceil(log2(a))

# 3 -> 2 # n => 2
# 4 -> 2 # n => 2
# 5 -> 2 # n => 3

import math


def solve():
    a = int(input())
    n = math.ceil(math.log2(a))
    x = 2**n - a
    print(2**n - 2*x)


solve()
