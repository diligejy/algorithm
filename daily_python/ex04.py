def enum_output():
    user_input = input("이름을 입력하세요 : ")
    for idx, word in enumerate(user_input):
        print(user_input[0:idx + 1])

enum_output()

# def hex_output():
#     decnum = 0
#     hexnum = input("Enter a hex number to convert : ")
#     if hexnum.isdigit():
#         for power, digit in enumerate(reversed(hexnum)):
#             decnum += int(digit, 16) * (16 ** power)
#         print(decnum)
#     else:
#         hex_output()


# hex_output()
