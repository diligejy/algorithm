class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Constraint
        1. int array
        2. All elements are unique.

        Idea 1 - 내가 푼 풀이
        1. n = length of nums
        2. n_list = a list from 0 to n
        3. subtract nums from n_list
        4. return what is left element.
        5. Time Complexity : O(n)
        6. Space Complexity : O(n)
        """
        #         n = len(nums)
        #         n_list = [i for i in range(n+1)]
        #         return list(set(n_list) - set(nums))[0]

        """
        Idea 2 - sort
        1. sort array
        2. 1번째 요소가 0이 아니라면, 0을 반환
        3. 마지막 요소가 n이 아니라면, n을 반환
        4. 배열을 1번 인덱스부터 n-1까지 순회
            - 현재 요소가 이전 요소에 1만큼 큰 수가 아니라면 현재 인덱스를 반환
        5. Time Complexity : O(nlogn)
        6. Space Complexity : O(1)
        """
        #         nums.sort()

        #         if nums[-1] != len(nums):
        #             return len(nums)
        #         if nums[0] != 0:
        #             return 0

        #         for i in range(1, len(nums)):
        #             expected = nums[i - 1] + 1
        #             if expected != nums[i]:
        #                 return expected
        #         return -1

        """
        Idea 3 - Hash set
        1. 배열의 모든 값을 해시 셋에 넣는다.
        2. 0에서 n까지 순회
            - 해시 셋에 없는 값을 반환
        """
        # hash_nums = set(nums)
        # for i in range(len(nums) + 1):
        #     if i not in hash_nums:
        #         return i

        """
        Idea 4 - Bit operation
        1. 변수에 n의 값으로 초기화
        2. 배열을 순회
            - 변수에 현재 인덱스와 해당 값을 다 같이 XOR
        3. 변숫값을 반환
        """
        # missing = len(nums)
        # for idx, val in enumerate(nums):
        #     missing = missing ^ idx ^ val
        # return missing
        """
        Idea 5 - 합의 차
        1. 0에서 n까지 합을 구함
        2. 배열 요소의 총합을 구함
        3. (0에서 n까지 합) - (배열 요소의 총합)을 반환
        """
        # n_sum = sum(list(range(len(nums) + 1)))
        # nums_sum = sum(nums)
        # return n_sum - nums_sum
