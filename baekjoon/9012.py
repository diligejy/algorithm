# def solve(s: str):
#     if s.count('(') != s.count(')'):
#         return "NO"
#     else:
#         pass


# for i in range(int(input())):
#     print(solve(input()))

def solve():
    data = input()
    stack = []
    for item in data:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0:
                print("NO")
                return
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')


n = int(input())
for _ in range(n):
    solve()
