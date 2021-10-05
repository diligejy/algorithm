import heapq as hq

n_list = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(n_list) == 0:
            print(-1)
        else:
            print(-hq.heappop(n_list))
    else:
        hq.heappush(n_list, -n)
