arr = [7, 3, 2, 9]


def sum(arr, acc):
    if len(arr) < 1:
        return acc
    return sum(arr, acc + arr.pop())


print("result=>", sum(arr, 0))
