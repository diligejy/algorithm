class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        # Constraint
        # 1. int array
        # 2. return value is present in at least two out of the three array
        # 3. return value is distinct
        # 4. return value type is array
        # 5. order is out of mind.

        # Idea
        # 1. make array nums which is concatenation of (nums1 + nums2 + nums3)
        # 2. to find key, find the distinct value in nums
        # 3. iterate key and find how many present in nums and store in value
        # 4. if value < 2: -> drop the key
        # 5. transform keys in dictionary to list

        # Time Complexity
        # O(n)

        # Space Complexity
        # O(1) # -> How to estimate Space complexity?

        ans = []
        nums = nums1 + nums2 + nums3

        for n in set(nums):
            isTwoContain = (n in nums1) + (n in nums2) + (n in nums3)
            if (nums.count(n) > 1) and (isTwoContain > 1):
                ans.append(n)
        return ans
