import random


def guessing_game():
    real_ans = random.randint(0, 100)
    opportunity = 3
    while opportunity > 0:
        user_ans = input("맞춰보시지~~ 기회는 3번, 0에서 100사이 정수임 : ")
        if not user_ans.isdigit():
            print("제대로 숫자 입력 안할래?")
            opportunity -= 1
            continue

        user_ans = int(user_ans)
        if user_ans > real_ans:
            opportunity -= 1
            print("Too high")
        elif user_ans < real_ans:
            opportunity -= 1
            print("Too low")

        if user_ans == real_ans:
            print(f"Just Right 정답은 {real_ans}였음")
            return "Just Right"

    print("똑바로 하랬잖아. 3번 넘었다")
    return "똑바로 하랬잖아. 3번 넘었다"


guessing_game()
