import sys

# 파이썬에선 재귀 호출횟수를 제한하고 있다.
# setrecursionlimit를 이용해 늘려주면 오류 해결
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**8)
def dfs(x,y):
    global result
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]

    if arr[x][y]==3: #도착점에 도달했을시
        result=1
        return

    for dx,dy in dxy:
        nx=x+dx
        ny=y+dy
        if nx<0 or nx>=N or ny<0 or ny>=N: #범위를 벗어나면
            continue
        if arr[nx][ny] ==1: #갈수 없는 길이면
            continue
        if visited[nx][ny] ==1: #이미방문한적 있으면
            continue

        visited[nx][ny]=1
        dfs(nx,ny)
        visited[nx][ny]=0
    return -1

for tc in range(1,11):
    T=int(input())
    N=100 #맵 크기
    arr=[list(map(int,input())) for _ in range(N)]
    # print(arr)
    visited = [[0] * 100 for _ in range(N)]  # 방문 표시 리스트 생성
    result=0
    dfs(1,1)
    print(f'#{tc} {result}')
