from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        if 0 in nums:
            return 0
        else:
            for ele in nums:
                if ele < 0:
                    neg += 1

            if neg % 2 == 0:
                return 1
            else:
                return -1
