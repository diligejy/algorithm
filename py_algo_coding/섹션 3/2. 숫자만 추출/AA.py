with_string = input()

# 정규표현식으로 하는 방법도 있겠으나 간단하게 loop
# https://www.kite.com/python/answers/how-to-extract-integers-from-a-string-in-python

nums = []
for word in with_string:
    if word.isdigit():
        nums.append(int(word))

for idx, _ in enumerate(nums):
    if nums[0] == 0:
        nums = nums[1:]

# int list join
# https://hyesun03.github.io/2017/04/08/python_int_join/
natural_num = int("".join(map(str, nums)))
print(natural_num)

cnt = 0
for i in range(1, natural_num + 1):
    if natural_num % i == 0:
        cnt += 1

print(cnt)
