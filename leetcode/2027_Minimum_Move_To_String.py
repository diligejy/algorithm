class Solution: 
    def minimumMoves(self, s: str) -> int: 
        N = len(s) 
        count = 0 
        i = 0 
        while i < N: 
            if s[i] == 'X': 
                i += 3 
                count += 1 
                continue 
            i += 1 
        return count
