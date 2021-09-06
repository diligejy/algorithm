# nums = [i for i in range(1, 21)]

# for _ in range(10):
#     a, b = map(int, input().split())
#     nums[a - 1 : b] = [i for i in reversed(nums[a - 1 : b])]

# print(" ".join(map(str, nums)))


a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]
a.pop(0)

for x in a:
    print(x, end=" ")
