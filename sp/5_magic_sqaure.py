# 참고 : https://jaeworld.github.io/python/python_magic_square/

n = int(input("마방진 행의 길이를 입력해주세요. 홀수만 가능"))


def magic(n: int):
    # n*n 크기의 빈 배열 생성
    arr = [[0]*n for i in range(n)]

    r = 0
    c = n // 2

    # 맨윗행 중간열에 1 배치
    arr[r][c] = 1

    # 2부터 n*n까지 배치합시다.
    for i in range(2, n*n+1):
        #  비어있다면

        """
        첫번째 숫자인 1을 맨윗 행 중간열에 배치한다.
        두번째 수부터는 오른쪽 대각선 위로 이동하며 숫자를 배치한다. 
        행렬의 범위를 넘어가면 반대쪽 끝으로 돌아온다.
        만약 숫자를 놓아야하는 자리에 이미 다른 숫자가 배치되어 있다면 
        현재 위치에서 행을 하나 내린 같은 열의 위치에 숫자를 놓는다. 다음 숫자는 다시 2번을 수행한다.
        """
        if arr[n-1 if r-1 < 0 else r-1][0 if c+1 > n-1 else c+1] == 0:
            r = n-1 if r-1 < 0 else r-1
            c = 0 if c+1 > n-1 else c+1
            arr[r][c] = i

        else:
            r = 0 if r+1 > n-1 else r+1
            arr[r][c] = i

    for l in arr:
        print(l)


magic(n)
