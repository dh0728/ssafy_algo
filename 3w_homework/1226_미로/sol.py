import sys
sys.stdin =open('input.txt')

def dfs(i,j ,v):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]] # 오 하 좌 상
    v[i][j] = 1 #현재 좌표 방문 표시
    if arr[i][j] == 3:  # 목적지 도착하면 리턴1
        return 1
    for dx, dy in dxy:  # 이동할 좌표 찾기
        ni = i + dx
        nj = j + dy
        if 0 <= ni < N and 0 <= nj <N and arr[ni][nj]!=1 and v[ni][nj]==0:  # 미로안, 벽X, 미방문 지점 일시
            if dfs(ni,nj,v): # dfs가 1을 리턴하면서 계속 길을 찾아감
                return 1
    return 0

for tc in range(1,11):
    T=int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    N= len(arr)
    visited=[[0]*16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j]==2:    #출발 지점 찾기
                result=dfs(i,j ,visited)    #찾으면 미로 찾기 시작
    print(f'#{tc} {result}')
