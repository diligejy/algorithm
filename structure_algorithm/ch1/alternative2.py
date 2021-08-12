print("+와 -를 번갈아 출력")
n = int(input("몇 개를 출력할깝쇼?: "))

for _ in range(n // 2):
    print("+-", end="")  # +-를 n // 2개의 출력

if n % 2:
    print("+", end="")  # n이 홀수일 때만 + 출력

print()
