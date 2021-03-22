s = input()
alphabets = [chr(c) for c in range(ord('a'), ord('z')+1)]

for i in alphabets:
    if s.find(i) >= 0:
        print(s.find(i), end=' ')
    else:
        print(-1, end=' ')
