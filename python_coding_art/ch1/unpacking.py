# 1. bubble_sort using unpacking

# before using unpacking

def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp


names = ['프레즐', '당근', '쑥갓', '베이컨']
bubble_sort(names)
print(names)

# after using unpacking


def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]  # 맞바꾸기


names = ['프레즐', '당근', '쑥갓', '베이컨']
bubble_sort(names)
print(names)

# 2. enumerate with unpacking

# before unpacking
snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i+1}: {name}은 {calories} 칼로리입니다.')

# after unpacking

for _, (name, calories) in enumerate(snacks, 1):
    print(f': {name}은 {calories} 칼로리입니다.')
