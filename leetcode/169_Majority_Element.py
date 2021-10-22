class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Constraint
        1. int array
        2. array has at least 1 element
        3. Majority Element number is only one.

        Idea1 - Brute Force
        1. 배열을 순회
        2. 각 배열의 요소를 다른 모든 요소와 비교하여 배열에 몇 개가 들어있는지 파악
        3. 개수를 세면서 다수의 수 조건에 맞는 숫자가 있으면 해당 숫자를 반환
        4. 시간복잡도 O(n^2), 공간복잡도 O(1)
        """
        # majority_count = int(len(nums) / 2)
        # for i, item_i in enumerate(nums):
        #     count = 0
        #     for j, item_j in enumerate(nums[i:], start=i):
        #         if item_i == item_j:
        #             count += 1
        #         if count > majority_count:
        #             return item_i
        # return -1

        """
        Idea2 - HashTable
        1. 해시테이블에서 키 항목으로는 배열의 요소로 하고 값 항목으로는 횟수를 지정
        2. 배열을 순회
        3. 배열을 순회하면서 해당 요소를 해시 테이블에서 찾는다.
            - 값이 있다면 해당 요소를 키값으로 하는 값 항목을 꺼내 1을 더해 업데이트
            - 값이 없다면, 해당 요소를 키항목으로 두고 1의 값으로 추가
        4. 값을 업데이트하고 다수의 수 조건에 맞는 숫자를 반환
        """
        # majority_count = int(len(nums) / 2)
        # hashmap = {}
        # for num in nums:
        #     if hashmap.get(num) != None:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1
        #     if hashmap[num] > majority_count:
        #         return num

        """
        Idea3 - sort
        1. 배열을 정렬
        2. 가운데 수를 반환
        """
        return sorted(nums)[int(len(nums) / 2)]
