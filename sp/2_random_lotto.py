import random


def random_lotto(input_list: list):
    """
    1부터 50까지의 수 중 랜덤으로 지정한 수 6개 맞추기
    """

    # 1. 컴퓨터가 중복되지 않는 6개의 숫자를 뽑도록 하기
    random_set = set()
    while len(random_set) < 6:
        random_set.add(random.randint(1, 50))
    random_set = sorted(random_set)

    ans_num = len((set(random_set) & set(input_list)))
    output_sentence = '정답 번호 공개 \n' + ' '.join(str(x) for x in random_set) + \
        ' 당신의 등수는 ' + str(7-ans_num) + '등입니다!\n' + \
        '맞힌 개수 : ' + str(ans_num) + '개'
    return output_sentence


# 2. 사용자에게 숫자 받기
input_list = []
while len(input_list) < 6:
    input_num = int(input('숫자를 입력하세요 : '))
    if (input_num < 1) or (input_num > 50):
        input_num = int(input('다시 숫자를 입력하세요 : '))
    elif input_num in input_list:
        input_num = int(input('이미 있는 숫자입니다. 다시 숫자를 입력하세요 : '))
    else:
        input_list.append(input_num)

print(random_lotto(input_list))


# 참고 : https://stackoverflow.com/questions/45128314/is-there-a-way-to-convert-a-list-variable-into-a-non-list-variable
