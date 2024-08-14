import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(start,end):
    visited = [[0] * SIZE for _ in range(SIZE)] # 방문체크 리스트 생성
    # q=deque([start])  #시작지면 큐에 삽입 start=[1,1]
    q=deque([(1,1)])
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    visited[start[0]][start[1]]=1
    while q:
        x,y =q.popleft()
        if arr[x][y]==3:
            return 1

        for dx, dy in dxy:
            ni = x + dx
            nj = y + dy
            if 0 > ni and ni >= SIZE and 0 > nj and nj >= SIZE: # 범위 벗어날 경우 continue
                continue
            if visited[ni][nj] == 1: #이미 방문했다면 패스
                continue
            if arr[ni][nj]== 1: # 갈 수 없는 길이면 패스
                continue
            visited[ni][nj]=1
            q.append((ni,nj))

    return 0

for tc in range(1,11):
    T=input()
    SIZE=100
    arr = [list(map(int, input())) for _ in range(SIZE)]
    result=BFS([1,1],[11,11])
    print(f'#{tc} {result}')