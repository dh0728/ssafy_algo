import sys
sys.stdin=open('input.txt')

from collections import deque

def bfs(x,y): #출발 i, 출발 j
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    visited=[[0]*M for _ in range(N)]
    q=deque()
    q.append([x,y,1])
    visited[x][y]=1
    cnt=1
    while q:
        i,j,depth=q.popleft()
        if depth >= L:
            return cnt

        for dx, dy in dxy:
            ni=i+dx
            nj=j+dy
            if ni<0 or ni >=N or nj<0 or nj >=M: # 범위 벗어나면 패스
                continue
            if not arr[ni][nj] or visited[ni][nj] !=0 : # 파이프가 아니거나 방문했으면 패스
                continue

            # ni, nj가 현재 파이프로 갈수 있는 길이고 다음파이프와도 이어져 있는지 확인
            if [dx, dy] in pipe[arr[i][j]] and [-dx, -dy] in pipe[arr[ni][nj]]:
                q.append([ni,nj,depth+1])
                visited[ni][nj]=depth +1
                cnt+=1
    return cnt

T=int(input())
for tc in range(1,T+1):
    # N 세로크기, M 가로크기, 맨홀 뚜껑이 위치한 세로 R 가로 C, 탈출후 소요된 시간
    N,M,R,C,L=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    # 구조물 타입
    # 1 상하좌우 연결
    # 2 상, 하 터널 연결
    # 3 좌, 우 터널 연결
    # 4 상, 우 터널 연결
    # 5 하, 우 터널 연결
    # 6 하, 좌 터널 연결
    # 7 상, 좌 터널 연결
    pipe=[
        0,
        [[0,1],[1,0],[0,-1],[-1,0]],
        [[1,0],[-1,0]],
        [[0,1],[0,-1]],
        [[0,1],[-1,0]],
        [[0,1],[1,0]],
        [[0,-1],[1,0]],
        [[0,-1],[-1,0]]
    ]
    result=bfs(R,C)
    print(f'#{tc} {result}')
