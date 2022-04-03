def myzip(*iters):
    return_list = []
    for i in range(len(iters[0])):
        res = []
        for j in range(len(iters)):
            res.append(iters[j][i])
        return_list.append(tuple(res))
    return return_list


print(myzip([10, 20, 30], "abc"))
# def plus_minus(num_list):
#     return -(sum(num_list[::2])) + 2 * num_list[0] + sum(num_list[1::2])


# print(plus_minus([10, 20]))

# def even_odd_sums(num_list):
#     return [sum(num_list[::2]), sum(num_list[1::2])]


# print(even_odd_sums([10, 20, 30, 40, 50, 60]))


# def firstlast(seq):
#     return seq[:1] + seq[-1:]


# print(firstlast((1, 2, 3, 4)))
