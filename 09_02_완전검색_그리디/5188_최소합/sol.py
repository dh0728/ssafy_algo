import sys
sys.stdin = open('input.txt')

# dfs 사용시 시간초과
def dfs(x,y,sum_num):   # 전에 방문한 지점을 또 방문할 일이 없으므로 visited는 필요없다
    global min_sum
    dxy=[[0,1],[1,0]]
    if x==N-1 and y==N-1:
        if min_sum > sum_num:
            min_sum = sum_num
        return

    for dx,dy in dxy:
        nx=x+dx
        ny=y+dy
        if nx >= N or ny >= N: # 범위 넘어가면 continue
            continue
        if visited[nx][ny] != 0:  # 이미 방문 했다면
            continue
        dfs(nx,ny,sum_num+arr[nx][ny]) #범위 안이면 arr[nx][ny]값 더해준후 재귀 호출
    return

# bfs 사용
from collections import deque

def bfs(x,y):
    dxy = [[0, 1], [1, 0]]
    visited=[[0]*N for _ in range(N)]
    q=deque()
    visited[x][y]=arr[x][y]
    q.append([x,y,arr[x][y]]) #  시작지점 방문 처리

    while q:
        i, j, pre_v = q.popleft()
        for dx, dy in dxy:
            ni = i+dx
            nj = j+dy
            if ni >= N or nj >= N:  # 범위 넘어가면 continue
                continue
            if visited[ni][nj] != 0: # 이미 방문 했다면
                continue
            if ni==0 or nj==0: #제일 바깥쪽에 경우
                visited[ni][nj]=arr[ni][nj]+pre_v
                q.append([ni,nj,visited[ni][nj]])
            else:
                if visited[ni-1][nj] >= visited[ni][nj-1]: # 기준위치에서 왼쪽의 합계가 위쪽보다 작다면
                    visited[ni][nj]=arr[ni][nj]+visited[ni][nj-1] # 왼쪽의 합계를 더하기
                    q.append([ni, nj, visited[ni][nj]])    # 큐에 삽입
                else:                                      # 위쪽의 합계가 더 작다면
                    visited[ni][nj] = arr[ni][nj] + visited[ni-1][nj] # 위쪽의 합계 더하기
                    q.append([ni, nj, visited[ni][nj]])    # 큐에 삽입
    return visited[N-1][N-1]

T=int(input())
for tc in range(1,T+1):
    N=int(input()) # N * N
    # visited = [[0] * N for _ in range(N)]
    # min_sum=N*N*10
    # dfs(0,0,arr[0][0])
    arr=[list(map(int,input().split())) for _ in range(N)]
    min_sum=bfs(0,0)
    print(f'#{tc} {min_sum}')
