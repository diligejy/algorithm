essential = [i for i in input()]
n = int(input())
n_list = [input() for _ in range(n)]


def isDesignGood(order: int, class_list: str):
    res = []
    for cls in class_list:
        if (cls in essential) and (cls not in res):
            res.append(cls)
        else:
            pass
    if "".join(res) == "".join(essential):
        print(f"#{order} YES")
    else:
        print(f"#{order} NO")


for idx, ele in enumerate(n_list):
    isDesignGood(idx + 1, ele)
