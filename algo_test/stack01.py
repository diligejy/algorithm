from datetime import datetime


def solution(s):
    cnt = 0
    while '()' in s:
        sp = s.split('()')
        s = ''.join(sp)
        cnt += 1
    print('cnt:', cnt)
    return len(s) == 0  # _는 가독성 때문에 사용


s = '(' * 5000000 + ')' * 5000000
print(f'len:{len(s)} start:', datetime.now())
print('final:', solution(s))
print('finish:', datetime.now())

[].pop()
