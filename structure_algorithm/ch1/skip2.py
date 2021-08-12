# 1부터 12까지 8을 건너뛰고 출력하기 2

# for i in list(range(1, 8)) + list(range(9, 13)):
#     print(i, end=" ")
# print()

n = int(input("어떤 수를 건너뛰시겠습니까?: "))
for i in list(range(1, n)) + list(range(n + 1, 13)):
    print(i, end=" ")
print()
