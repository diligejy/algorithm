import random


def guessing_game():
    real_ans = random.randint(0, 100)
    while 1:
        user_ans = input("맞춰보시지~~ 0에서 100사이 정수임 : ")
        if not user_ans.isdigit():
            print("제대로 숫자 입력 안할래?")
            continue

        user_ans = int(user_ans)
        if user_ans > real_ans:
            print("Too high")
        elif user_ans < real_ans:
            print("Too low")

        if user_ans == real_ans:
            print(f"Just Right 정답은 {real_ans}였음")
            return "Just Right"


guessing_game()
