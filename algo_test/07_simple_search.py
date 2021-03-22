arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

# 8은 몇 번째 있을까?/
# 7번째 - 인덱스로는 6
# 입력받은 숫자가 몇 번째 인덱스에 있는지 찾는 function만들기


def find_index(arr, targetNum):
    if not targetNum in arr:
        raise Exception('숫자 없음')
    for index in range(len(arr)):
        if targetNum == arr[index]:
            return index


print(find_index(arr, int(input('숫자를 입력하세요 \n'))))
