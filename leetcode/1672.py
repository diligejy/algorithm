from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    max = 0
    for account in accounts:
        if sum(account) >= max:
            max = sum(account)
        else:
            max = max
    return max


accounts = [[1, 2, 3], [3, 2, 1]]
maximumWealth(accounts)
