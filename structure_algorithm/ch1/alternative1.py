
print('+와 -를 번갈아 출력')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2 == 0:
        print('+', end = '')
    else:
        print('-', end = '')

print()