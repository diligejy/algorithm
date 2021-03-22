arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]


def binarySearch(arr, targetNum):
    """
    1. 숫자를 입력받음 -> targetNum
    2. len(list)의 절반에 해당하는 midIndex의 원소를 구함
    3. arr[midIndex]와 targetNum을 비교
    4. 1번 targetNum이 크다 -> midIndex ~ len(list) -1 까지 반복
    5. 2번 targetNum과 arr[midIndex]가 같다 -> ok
    6. 3번 targetNum이 작다 => 0 ~ midIndex까지 반복
    """
    start = 0
    end = len(arr) - 1
    while (start <= end):
        midIndex = len(arr) // 2
        if targetNum == arr[midIndex]:
            return midIndex
        elif targetNum > arr[midIndex]:
            start = midIndex + 1
        elif targetNum < arr[midIndex]:
            end = midIndex - 1

    print("start:", start, "end:", end)


binarySearch(arr, 8)
