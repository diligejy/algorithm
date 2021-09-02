nums = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    nums[a - 1 : b] = [i for i in reversed(nums[a - 1 : b])]

print(" ".join(map(str, nums)))
