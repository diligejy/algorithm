n = [int(x) for x in input().split()]
if (n == sorted(n)):
    print('ascending')
elif (n == sorted(n)[::-1]):
    print('descending')
else:
    print('mixed')
