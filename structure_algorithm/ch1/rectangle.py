# 가로 세로 길이가 정수, 넓이가 area인 직사각형에서 변의 길이 나열

area = int(input("직사각형의 넓이를 입력하세요: "))

# 방법 1
for i in range(1, area // 2):
    if (area % i) == 0:
        print(i, area // i)

# 방법 2
for i in range(1, area + 1):
    if i * i > area:
        break
    if area % i:
        continue
    print(f"{i} x {area // i}")
