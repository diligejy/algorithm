class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Constraint
        1. int array
        2. k is positive int
        
        Idea1 - Brute Force
        1. k번만큼 순회
        2. 배열의 요소를 1칸씩 우측으로 이동 및 회전
        3. Time Complexity : O(n * k)
        4. Space Complexity : O(1)
        """
        # for _ in range(k):
        #     prev = nums[len(nums) - 1]
        #     for i in range(len(nums)):
        #         temp = nums[i]
        #         nums[i] = prev
        #         prev = temp

        """
        Idea2 - Temporary Array
        1. 입력과 같은 크기의 임시 배열(temp)을 생성
        2. nums 배열을 순회
            - temp 배열에 nums의 요소를 k만큼 이동 및 회전시킨 위치에 값을 삽입
        3. 임시 배열을 순회
            - temp 배열의 요소를 nums 배열에 같은 인덱스의 값을 복사
        4. Time Complexity : O(n)
        5. Space Complexity : O(n)
        """
        #         temp = [0] * len(nums)

        #         for i, val in enumerate(nums):
        #             temp[(i + k) % len(nums)] = nums[i]

        #         nums[:] = temp
        """
        Idea3 
        1. 모든 요소가 한 번씩 교환이 될 때까지 배열을 순회
        2. 요소를 k만큼 이동 및 저장
            - 이동한 위치의 이전 요소는 저장
            - 저장한 요소는 다음 k만큼 이동하여 넣기
            - 이동시킬 때마다 카운트
            - 다음 요소를 선택하고 다시 2번의 내용을 반복
        """
        #         count = 0

        #         for start in range(len(nums)):
        #             if count >= len(nums):
        #                 break

        #         curr_index = start
        #         prev_elem = nums[start]

        #         while True:
        #             next_index = (curr_index + k) % len(nums)
        #             temp = nums[next_index]
        #             nums[next_index] = prev_elem
        #             prev_elem = temp

        #             curr_index = next_index
        #             count += 1

        #             if curr_index == start:
        #                 break
        """
        Idea4 - 3번 뒤집기
        1. 전체 숫자를 뒤집는다
        2. 처음 K만큼까지 숫자를 뒤집는다
        3. 이전에 뒤집은 숫자 다음(n- k)부터 마지막(n)까지 뒤집는다
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[0:k] = nums[0:k][::-1]
        nums[k : len(nums)] = nums[k : len(nums)][::-1]
