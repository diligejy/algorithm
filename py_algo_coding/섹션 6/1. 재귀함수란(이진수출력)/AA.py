def decimal_to_binary(n: int):
    if n == 0:
        return
    else:
        decimal_to_binary(n // 2)
        print(n % 2, end="")


n = int(input())
decimal_to_binary(n)
