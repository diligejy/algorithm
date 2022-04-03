from itertools import chain
from collections import defaultdict


def sum_dict(*args):
    # args = list(args)
    d3 = defaultdict(list)
    for i in args:
        for k, v in chain(i.items()):
            d3[k].append(v)
    return d3
    # print(d3)

    # for k, v in d3.items():
    #     print(k, v)
    # return args


print(sum_dict({"ex1": "ex2"}, {"ex1": "ex5"}, {"ex3": "ex4"}))


# def sum_numeric(*args):
#     res = 0
#     for item in args:
#         if type(item) == int or item.isdigit():
#             res += int(item)
#     return res


# print(sum_numeric(10, 20, "a", "30", "bcd"))


# def mysum_bigger_than(args, *items):
#     res = args - args
#     for i in items:
#         if i > args:
#             res += i
#     return res


# print(mysum_bigger_than(10, 5, 20, 30, 6))

# def mysum(*args):
#     if not args:
#         return args
#     output = args[0]
#     for item in args[1:]:
#         output += item
#     return output


# # print(mysum())
# # print(mysum("abc", "def"))
# print(mysum([1, 2, 3], [4, 5, 6]))
