n = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores) / len(scores))

acc = float("inf")
val = 0
score_list = []

for i, score in enumerate(scores):
    if abs(score - avg) < acc:
        acc = abs(score - avg)
        val = score
        res = i + 1
    elif abs(score - avg) == acc:
        if score > val:
            val = score
            res = i + 1

print(avg, res)
