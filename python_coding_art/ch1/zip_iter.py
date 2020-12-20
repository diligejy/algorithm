names = ['Cecilia', '남궁민수', 'eneow']
counts = [len(n) for n in names]


# before using enumerate or zip
longest_name = None
max_count = 0
for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count
# print(longest_name)

# after using enumerate
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

# after using zip
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
print(longest_name)
