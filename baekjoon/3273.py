def twoSum(num_list: list, target: int):
    hashtable_dict = {}
    couple_num = 0
    for i in range(len(num_list)):
        value = target - num_list[i]
        if hashtable_dict.get(value) is not None and hashtable_dict[value] != i:
            couple_num += 1
        hashtable_dict[num_list[i]] = i
    return couple_num


n = int(input())
nums = [int(x) for x in input().split()]
target = int(input())
print(twoSum(nums, target))
