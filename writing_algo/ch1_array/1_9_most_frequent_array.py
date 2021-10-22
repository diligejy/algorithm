from types import List

# def majorityElement(nums: List[int]) -> int:
#     """
#     Brute-force
#     """
#     majority_count = int(len(nums) / 2)

#     for i, item_i in enumerate(nums):
#         count = 0
#         for j, item_j in enumerate(nums[i:], start=i):
#             if item_i == item_j:
#                 count += 1
#             if count > majority_count:
#                 return item_i
#     return -1


def majorityElement(nums: List[int]) -> int:
    majority_count = int(len(nums))

    hashmap = {}

    for num in nums:
        if hashmap.get(num) != None:
            hashmap[num] = hashmap[num] + 1
        else:
            hashmap[num] = 1

        if hashmap[num] > majority_count:
            return num
    return -1