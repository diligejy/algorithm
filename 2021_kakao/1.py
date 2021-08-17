"""
s	                result
"one4seveneight"	1478
"23four5six7"	    234567
"2three45sixseven"	234567
"123"	            123
"""


def string_to_num(s: str) -> int:
    num = int(
        s.replace("one", "1")
        .replace("two", "2")
        .replace("three", "3")
        .replace("four", "4")
        .replace("five", "5")
        .replace("six", "6")
        .replace("seven", "7")
        .replace("eight", "8")
        .replace("nine", "9")
        .replace("zero", "0")
    )
    return num


# string_to_num("one132twozero")


# for 문 등의 반복문을 사용하여 한 글자씩 읽으면서 숫자인 경우 그대로 출력하고,
# 알파벳 문자인 경우 zero~nine 중 해당되는 것이 있으면 숫자로 바꾸고, 아니면 다음 문자를 계속 확인하는 방식
text = "one132twozero"


num_dic = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solutions(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
