from typing import List
nums = [1, 3, 5, 6]
target = 0


# Brute force
"""
def searchInsert(nums: List[int], target: int) -> int:
    idx = 0
    for i in range(len(nums)):
        if target == nums[i]:
            return i
        elif target > nums[i]:
            idx = i+1
    return idx
"""

# Binary Search


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((low + high) / 2)

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(searchInsert(nums, target))
