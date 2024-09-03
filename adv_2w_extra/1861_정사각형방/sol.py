import sys
sys.stdin=open('input.txt')

from collections import deque
def bfs(i,j):
    global max_depth
    global max_depth_room_num
    dxy=[[0,1],[1,0],[0,-1],[-1,0]] # 우 하 좌 상
    visited=[[0]*N for _ in range(N)]
    visited[i][j]=1
    q=deque()
    q.append([i,j,1])
    v_list.append(arr[i][j])  # 리스트에 삽입해 이동횟수 카운팅에서 생략

    while q:
        x,y,depth=q.popleft()
        for dx, dy in dxy:
            ni = x+dx
            nj = y+dy
            if ni < 0 or ni >=N or nj < 0 or nj >=N: #범위 벗어나면
                continue
            if visited[ni][nj] !=0: # 이미 방문했으면
                continue
            if arr[ni][nj] - arr[x][y] !=1: #다음 방문이 정확히 1크지 않으면
                continue
            visited[ni][nj]=depth+1
            q.append([ni,nj,depth+1])
            v_list.append(arr[ni][nj])  # 리스트에 삽입해 이동횟수 카운팅에서 생략

    if max_depth < depth:   # 최대 이동 횟수가 더 크다면
        max_depth=depth
        max_depth_room_num=arr[i][j]
    elif max_depth == depth: # 최대 이동 횟수가 같으면
        if max_depth_room_num > arr[i][j]: # 방번호 크기 비교후
            max_depth_room_num=arr[i][j]   # 방번호가 작은것 삽입
    return

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_depth=0
    max_depth_room_num=0
    v_list=[]   # 이동횟수를 셀 필요가 없는 시작 방번호 리스트
    for i in range(N):
        for j in range(N):
            if arr[i][j] in v_list:
                continue
            bfs(i,j)

    print(f'#{tc} {max_depth_room_num} {max_depth}')