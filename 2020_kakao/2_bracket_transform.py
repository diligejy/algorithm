def reverse_string(p):
    res = ""
    for item in p:
        if item == '(':
            res += ')'
        else:
            res += '('
    return res


def right(p):
    stack = []
    for ele in p:
        if ele == '(':
            stack.append(ele)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    return False


def split_string(p):
    open_b = 0
    close_b = 0
    res = ""
    for i in range(len(p)):
        if p[i] == '(':
            open_b += 1
        else:
            close_b += 1
        res += p[i]
        if open_b == close_b and (open_b + close_b < len(p)):
            return res, p[i+1:]
    return res, ''


def solve(p):
    if p == '':
        return ""
    u, v = split_string(p)
    if right(u):
        return u + solve(v)
    else:
        u = u[1:-1]
        u = reverse_string(u)
        return '(' + solve(v) + ')' + u


def solution(p):
    return solve(p)
