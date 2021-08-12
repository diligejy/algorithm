"""
0   * 
1  *** 
2 *****
"""
def star_odd(n):
    for i in range(1, n):
        for j in range(n - 1 - i):
            print(' ', end='')
        for j in range(1, i*2, 1):
            print('*', end='')
        print('')

star_odd(3)