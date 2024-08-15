import sys
sys.stdin = open('input.txt')

from collections import deque
def find_start():   #출발지 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                return i,j

def BFS(x,y):
    dxy=[[0,1],[1,0],[0,-1],[-1,0]] #우 하 좌 상 방향
    q=deque() #큐 생성
    q.append([x,y]) # 출발 좌표 삽입
    visited[x][y]=1 # 시작 노드 방문 표시

    while q:    # q에 값 없어질 때 까지 while 문 삽입
        i,j=q.popleft()
        # if arr[i][j]==3:
        #     return visited[i][j]-2
        for dx, dy in dxy:
            ni= i+dx
            nj= j+dy
            if 0 > ni or ni>=N or 0 > nj or nj>=N: # 범위 벗어나면 패스
                continue
            if visited[ni][nj]!=0: #이미 방문한 곳이면 패스
                continue
            if arr[ni][nj]==1: #길이 아니면 패스
                continue
            q.append([ni,nj]) #다음 칸 좌표 삽입
            visited[ni][nj]=visited[i][j]+1 # 이동 횟수 +1

            if arr[ni][nj]==3:
                return visited[i][j]-1

    return 0    # 목적지 못찾아가면 0리턴


T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    i,j=find_start()
    result=BFS(i,j)
    print(f'#{tc} {result}')