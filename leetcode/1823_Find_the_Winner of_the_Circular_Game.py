def findTheWinner(n: int, k: int) -> int:
    arr = list(range(1, n+1))
    start = 0
    while len(arr) > 1:
        start = (start+k-1) % len(arr)
        print(start)
        arr.pop(start)
    return arr[0]


findTheWinner(6, 5)
