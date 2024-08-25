import sys
sys.stdin=open('input.txt')

from collections import deque
def bfs(x,y):
    visited = [[0] * N for _ in range(N)]  # 방문 표시 리스트 생성
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    while q:
        i,j=q.popleft()
        for dx,dy in dxy:
            nx=i+dx
            ny=j+dy
            if nx < 0 or nx >=N or ny <0 or ny>=N: #범위를 벗어나면 패스
                continue
            if visited[nx][ny]==1: # 방문한 길이면
                continue
            if arr[nx][ny]==1: # 갈 수 없는 길이면
                continue
            if arr[nx][ny]==3:
                return 1
            visited[nx][ny]=1
            q.append([nx,ny])
    return 0
for tc in range(1,11):
    T=int(input())
    N = 100  # 맵 크기
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)

    result=bfs(1, 1)
    print(f'#{tc} {result}')