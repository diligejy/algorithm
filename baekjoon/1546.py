n = int(input())
scores = [int(x) for x in input().split()]

scores = [(x / max(scores)) * 100 for x in scores]

print(sum(scores) / n)
