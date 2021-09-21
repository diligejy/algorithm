n = int(input())
player_info = []
for _ in range(n):
    height, weight = map(int, input().split())
    player_info.append((height, weight))


player_info.sort(key=lambda x: x[0], reverse=True)

largest = 0
cnt = 0
for i in player_info:
    if i[1] > largest:
        largest = i[1]
        cnt += 1
print(cnt)
