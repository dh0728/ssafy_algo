import sys
sys.stdin= open('input.txt')

# 정답1
def snail_sort(N):
    dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dy = [1, 0, -1, 0]
    arr = [[0] * N for _ in range(N)]
    i = 0  # 초기 row
    j = 0  # 초기 col
    dir = 0  # 방향에 따른 dxy값 dxy[dir]

    for n in range(1, N * N + 1):
        arr[i][j] = n
        ni = i + dx[dir]  # i 방향 백터 +
        nj = j + dy[dir]  # j 방향 백터 +

        # 범위를 벗어나거나 이미 숫자가 채워진 경우 방향 전환
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dir = (dir + 1) % 4
            i = i + dx[dir]
            j = j + dy[dir]

    return arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = snail_sort(N)
    print(f'#{tc}')
    for li in result:
        print(' '.join(map(str, li)))



