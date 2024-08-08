import sys
sys.stdin = open('input.txt')


def space_ship(N, M):
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]  # 위아래여부   시계방향
    dy = [1, 1, 1, 0, -1, -1, -1, 0]  # 좌우여부
    res = 0  # 조건을 만족하는 예비후보지 수
    for i in range(N):
        for j in range(M):
            cnt = 0  # 착륙지점보다 높이가 낮은 구역 수
            v = arr[i][j]   # 탐색 지점 설정
            for k in range(len(dx)):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M: # ni,nj가 배열안에 있을 시
                    if arr[ni][nj] < v:         # 탐색지점보다 낮으면 cnt +1
                        cnt += 1
                if cnt >= 4:                    # 낮은 구간이 4이상이면 후보지 수 +1 후 break
                    res += 1
                    break
    return res


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = space_ship(N, M)
    print(f'#{tc} {result}')
