# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

# 1. 예전에 배운 해시로 푼 풀이
def solution(participant, completion):
    part_dict = {}
    comp_dict = {}
    for p in participant:
        part_dict[p] = part_dict.get(p, 0) + 1
    for c in completion:
        comp_dict[c] = comp_dict.get(c, 0) + 1

    for k in part_dict.keys():
        if k in comp_dict.keys():
            if part_dict[k] != comp_dict[k]:
                return k
        else:
            return k


# 2. 극강의 간결함을 추구하신 분의 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
