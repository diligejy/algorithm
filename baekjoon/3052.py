rests = []
for _ in range(10):
    rests.append(int(input()) % 42)

print(len(list(set(rests))))
