import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + 1):
    N, M = list(map(int, input().split()))
    dij = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    arr = [list(map(int, input().split())) for _ in range(N)]

    A = 0

    for i in range(0, N):
        for j in range(0, M):
            spot = arr[i][j]
            counts = 0
            for di, dj in dij:
                ni = i + di
                nj = j + dj

                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                if spot > arr[ni][nj]:
                    print(f'i ={i} j={j} ni={ni} nj={nj} 값{arr[ni][nj]}')
                    counts += 1
            if counts >= 4:
                A += 1

    print(f'#{test_case} {A}')