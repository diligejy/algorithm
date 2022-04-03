import random


def guessing_game():

    # Guessing Words
    real_words = ["apple", "banana", "coconut", "watermelon"]

    ans_idx = random.randint(0, len(real_words) - 1)
    real_ans = real_words[ans_idx]
    while 1:
        print(real_words)
        user_ans = input(f"맞춰보세용, 저 중에 하나임 1에서 {len(real_words)}까지 숫자 중 하나를 입력하세요 : ")
        if not (
            user_ans.isdigit() and (int(user_ans) in range(1, len(real_words) + 1))
        ):
            print("제대로 숫자 입력 안할래?")
            continue
        user_ans = int(user_ans)
        if user_ans < ans_idx:
            print("뒤에 있어")
        elif user_ans > ans_idx:
            print("앞에 있어")
        if user_ans == ans_idx:
            print(f"굳굳!! 정답은{real_ans}였습니다")
            return

    # Gussing Numbers
    # real_ans = random.randint(0, 100)
    # opportunity = 3
    # while opportunity > 0:
    #     user_ans = input("맞춰보시지~~ 기회는 3번, 0에서 100사이 정수임 : ")
    #     if not user_ans.isdigit():
    #         print("제대로 숫자 입력 안할래?")
    #         opportunity -= 1
    #         continue

    #     user_ans = int(user_ans)
    #     if user_ans > real_ans:
    #         opportunity -= 1
    #         print("Too high")
    #     elif user_ans < real_ans:
    #         opportunity -= 1
    #         print("Too low")

    #     if user_ans == real_ans:
    #         print(f"Just Right 정답은 {real_ans}였음")
    #         return "Just Right"

    # print("똑바로 하랬잖아. 3번 넘었다")
    # return "똑바로 하랬잖아. 3번 넘었다"


guessing_game()
