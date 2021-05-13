import array as arr

# 정수형 배열 생성하고 초깃값 [1, 2, 3]
int_arr = arr.array('i', [1, 2, 3])

print('elements in array : ', end="")
for i in range(0, len(int_arr)):
    print(int_arr[i], end=' ')
print()

print("The index of 1st occurence of 3 is : " , end = '')
print(int_arr.index(3))

# 1의 위치에 4의 값을 추가
int_arr.insert(1, 4)

print('elements after insertion : ', end=" ")
for i in (int_arr):
    print(i, end=' ')
print()

# 1을 값을 찾아 제거
int_arr.remove(1)

print("elements after delete \'1\' in array : ", end=' ')
for i in (int_arr):
    print(i, end=' ')
print()
