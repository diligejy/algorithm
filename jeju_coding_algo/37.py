# https://www.notion.so/37-count-dc0e13c631da440cba8fa057bb9549b0
# 새 학기를 맞아 호준이네 반은 반장 선거를 하기로 했습니다.  
# 그런데 표를 하나씩 개표하는 과정이 너무 번거롭게 느껴진 당신은 
# 학생들이 뽑은 후보들을 입력받으면 
# 뽑힌 학생의 이름과 받은 표 수를 출력하는 프로그램을 작성

# 입력
# 원범 원범 혜원 혜원 혜원 혜원 유진 유진

# 출력
# 혜원(이)가 총 4표로 반장이 되었습니다.


# 1. 각 사람들의 이름을 set으로 만들어준다.
# 2. 각 set의 요소마다 몇 개가 list에 있는지 dict로 만들어준다
# 3. dictionary를 value기준으로 descending sort한 뒤 가장 높은 dictionary를 출력

user_input_list = input().split(' ')
user_input_set = set(user_input_list)
print(user_input_set)

result = {}

for name in user_input_set:
    result[name] = user_input_list.count(name)

result = sorted(result.items(), key=(lambda x : x[1]), reverse=True)

print(f'{result[0][0]}(이)가 총 {result[0][1]}표로 반장이 되었습니다.')
