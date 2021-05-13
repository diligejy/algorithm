"""
두 수의 합 찾기

주어진 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 목표값을 만들 때 
그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하는 프로그램 작성,

입력값으로 주어지는 배열에는 정확히 하나의 정답이 존재하며, 같은 요소의 값을 중복해서 사용할 수 없음

입력값 : nums = [2, 7, 10, 19], target = 9
출력값 : [0, 1]
"""


"""
1. Brute Force
nums = [2, 7, 10, 19]
target = 9

for i in range(0, len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        if (nums[i] + nums[j] == target):
            print([i, j])
"""

# 2. HashTable

"""
1. 해시테이블을 구성
    - 키값으로는 배열의 요소, 값으로는 요소의 인덱스로 구성
2. 각 요소를 순회하면서 
    - 목표값 - 현재 요소 = 다른 요소
    - 해시 테이블에서 다른 요소의 값을 찾는다
    - 만약 다른 요소가 해시 테이블에 있다면, 현재 요소의 인덱스와 해시 테이블의 값(인덱스)을 반환한다.
    - 다른 요소가 없다면, 현재 요소를 해시 테이블의 키값으로 넣고 인덱스를 해시 테이블의 값 항목으로 추가    
"""
nums = [2, 7, 10, 19]
target = 9

hashtable_dict = {}
for i in range(len(nums)):
    other_elem = target - nums[i]
    if hashtable_dict.get(other_elem) is not None and hashtable_dict[other_elem] != i:
        print(sorted([i, hashtable_dict[other_elem]]))
    hashtable_dict[nums[i]] = i
