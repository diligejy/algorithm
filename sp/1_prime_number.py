num = int(input('검사할 숫자를 입력하세요 : '))


def val_prime(num: int):
    """
    숫자보다 작은 수들 중 소수개수 구하기
    """
    result = 0
    for i in range(1, num+1):
        div_num = 0
        for j in range(1, i+1):
            if i % j == 0:
                div_num += 1
        if div_num == 2:
            result += 1
    return result


print('Result : ', val_prime((num)), '개')
