string = '13+3*{24*(35-46.76)-89}'
# 1 + (2 * 3) - (2 * 4)
# 1 + (6) - (8)
# 7 - 8
# -1

# 숫자와 괄호를 분리해주는 식


def stringTokenizer(string, deli):
    """
    13, +, 24, * (, 35, -, 46.76, )
    """
    result = []
    acc = ""
    for chr in string:
        if chr in deli:
            if acc != "":  # 빈 칸일 때는 넣지 않는다.
                result.append(acc)
                acc = ""
            result.append(chr)
        else:
            acc = acc + chr
    return result


result = stringTokenizer(string, "+-*/()[]^")
print('=>', result)  # []
