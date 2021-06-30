def generate(numsRows : int) -> List[List[int]]:
    pascal = []

    if numsRows <= 0:
        return pascal
    
    pascal.append([1])

    for i in range(1, numsRows):
        prev_len = len(pascal[i - 1])
        curr_list = []

        for j in range(prev_len + 1):
            num = 1
            if j != 0 and j != prev_len:
                num = pascal[i - 1][j - 1] + pascal[i - 1][j]
            
            curr_list.append(num)
        
        pascal.append(curr_list)
    return pascal