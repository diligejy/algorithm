n = int(input())
nums = []
letters = []

for e in range(n):
    test_case = input().split()
    nums.append(test_case[0])
    letters.append(test_case[1])

for num, letter in zip(nums, letters):
    rep = ''
    for s in letter:
        rep += int(num) * s
    print(rep)


# def solve():
#     n, s = input().split()
#     n = int(n)
#     for c in s:
#         print(c * n, end = '')
#     print()


# t = int(input())
# for _ in range(t):
#     solve()
