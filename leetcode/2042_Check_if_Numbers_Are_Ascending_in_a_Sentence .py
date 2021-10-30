class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        min_value = float("-inf")
        for e in s.split():
            if e.isdigit():
                if int(e) <= min_value:
                    return False
                    min_value = int(e)
        return True
