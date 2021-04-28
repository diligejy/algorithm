import sys

n = int(input())
count = 1
stack = []
result = []

for i in range(1, n + 1):  # 데이터 개수만큼 반복
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:  # 스택 최상위 원소가 데이터와 같을 때까지 출력
        stack.pop()
        result.append('-')
    else:  # 불가능한 경우
        print('NO')
        exit(0)

print('\n'.join(result))  # 가능한 경우
