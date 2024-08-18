import sys
sys.stdin=open('input.txt')

from collections import deque
def bfs(x,y):
    global max_home
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    visited=[[0]*N for _ in range(N)]
    cnt=0 # 서비스 받는 집의 갯수
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    K=0 #제공범위 0부터 시작
    if maps[x][y]: # 탐색지점에 집이 있으면
        cnt+=1     # 더해주기
    while q:
        i,j=q.popleft()
        if visited[i][j] != K: # 탐색 중심에서의 거리가 달라지면
            K = visited[i][j]  # 제공 범위를 현재 위치까지로 바꾸고
            cost= K*K + (K-1)*(K-1) # 제공 범위에 따른 cost 계산
            if cost <= M*cnt: # 비용보다 수익이 크면
                if max_home < cnt: # 전에 서비스하는 집 수보다 현재 서비스 집수가 많다면 업데이트
                    max_home=cnt

        for dx, dy in dxy:
            ni= i +dx
            nj= j +dy
            if ni <0 or ni>=N or nj<0 or nj>=N: #범위 벗어나면 패스
                continue
            if visited[ni][nj] >0: #이미 서비스 사용중이면 X
                continue
            visited[ni][nj]=K+1 # K는 현재 중심에서 부터 각위치까지의 거리이자, 적용범위
            q.append([ni,nj])
            if maps[ni][nj]==1: # 집이 있으면 집수 플러스
                cnt+=1
    return



T=int(input())
for tc in range(1,1+1):
    N,M=map(int,input().split())
    maps=[list(map(int,input().split())) for _ in range(N)]

    max_home=0
    for i in range(N):
        for j in range(N):
            bfs(i,j)
    print(f'#{tc} {max_home}')