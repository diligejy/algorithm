from decimal import *


def run_timing_decimal():
    """
    사용자에게 부동소수점 형식 문자열 2개를 입력받고, Decimal 클래스 인스턴스로 변환한 뒤 둘을 더해서 출력
    """
    total = 0
    for i in range(2):
        total += Decimal(input("Enter floating point : "))

    return total


print(run_timing_decimal())

# def run_timing():
#     """
#     사용자에게 숫자 입력을 여러 개 받고, 그 평균을 출력
#     """

#     number_of_runs = 0
#     total_time = 0

#     while True:
#         one_run = input("Enter 10 km run time: ")

#         if not one_run:
#             break

#         number_of_runs += 1
#         total_time += float(one_run)

#     avg_time = total_time / number_of_runs

#     print(f"Average of {avg_time}, over {number_of_runs} runs")


# run_timing()
