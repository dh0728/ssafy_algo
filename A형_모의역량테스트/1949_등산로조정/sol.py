import sys
sys.stdin=open('input.txt')
def find_top(): # 최대 높이가 몇인지 찾기
    max_top=0
    for i in range(N):
        for j in range(N):
            if maps[i][j]>max_top:
                max_top=maps[i][j]
    return max_top

# 인자로 줘야할 거 현재좌표, 길 수, 깎을 수 있는 횟수, 현재 꼭대기 높이
def dfs(i,j,cnt,k_cnt, top):
    # print(i,j,top)
    global max_route
    if max_route < cnt:
        max_route =cnt
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for dx, dy in dxy:
        ni = i + dx
        nj = j + dy
        if 0 > ni or ni >= N or 0 > nj or nj >= N:  # 범위를 벗어나면
            continue
        if visited[ni][nj] != 0:  # 이미 방문한 길이면
            continue
        if not k_cnt and maps[ni][nj] >= top:  # 깎을 기회가 없으면
            continue
        if k_cnt and maps[ni][nj] >= top:  # 높이가 높거나 같지만 깎을 기회가 있으면
            if maps[i][j] <= maps[ni][nj] - K:  # 깎아도 크거나 같으면
                continue
            visited[ni][nj] = 1
            dfs(ni,nj,cnt+1,0,top-1)
            visited[ni][nj] = 0
        if maps[ni][nj] <top: # 전 위치보다 높이가 낮으면
            visited[ni][nj]=1
            dfs(ni,nj,cnt+1,k_cnt,maps[ni][nj])
            visited[ni][nj]=0
    return
def start(top):
    cnt=0
    for i in range(N):
        for j in range(N):
            if cnt==5:  # 최대 높이는 최대 5 곳이므로 넘어가면 리턴
                return
            if maps[i][j]==top:
                visited[i][j] = 1  # 시작좌표 방문처리
                dfs(i,j,1,1,maps[i][j])    # 최대 높이면 탐색 시작
                visited[i][j] = 0  # 방문처리 복원
                cnt+=1
    return

T=int(input())

for tc in range(1,T+1):
    N,K=map(int,input().split())
    maps=[list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_top=find_top()
    max_route = 0
    start(max_top)
    print(f'#{tc} {max_route}')