n, x = [int(x) for x in input().split()]
nums = [int(num) for num in input().split() if int(num) < x]
for i in nums:
    print(i, end=' ')
