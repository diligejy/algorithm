import sys
word = set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word = list(word)
word.sort(key=lambda x: len(x))
word.sort()
for i in word:
    print(i)
