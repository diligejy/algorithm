numbers = [7, 3, 2, 9]

if numbers[0] > numbers[1]:
    # 자리를 바꿔줌
    temp = numbers[0]
    numbers[0] = numbers[1]
    numbers[1] = temp


def bubble_sort(array):
    """
    i : 0, 1, 2
    j : 1, 2, 3
    """
    if len(array) < 2:
        return array
    else:
        for i in range(0, len(array) - 1):
            for j in range(i+1, len(array)):
                if array[i] > array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
    return array


print(bubble_sort([7, 3, 2, 9]))
