import sys
sys.stdin=open('input.txt')

from collections import deque

def dfs():
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    q=deque() #살아있는 세포가 들어가는 큐

    for i in range(N): # 살아있는 세포 큐에 넣기
        for j in range(M):
            if arr[i][j]:
                q.append([i, j, arr[i][j], 0]) # 좌표 x,y , 생명력, 살아있는 시간
    # print(q)

    # 현재 존재하는 세포의 좌표들이 들어가는 세트 생성
    # 중복 될 수 없으니 set으로 만들기
    cell_set=set()

    for k in range(K):
        # temp_q=deque()
        temp_q=[]
        spread_cell_dict={}
        while q:
            x, y, life, t = q.pop()
            # x, y, life, t= q.popleft()
            cell_set.add((x,y))

            # 살아있는 시간이 생명력보다 낮을 경우 - > 아직 비활성
            if t < life:
                temp_q.append([x,y,life,t+1])
                continue

            # 같아지면 분열 시작
            if t == life:
                for dx,dy in dxy:
                    ni=x+dx
                    nj=y+dy
                    if (ni,nj) in cell_set:
                        continue

                    # 동시에 분열해 같은 자리에 들어가는 경우 생명력이 더 높은게 들어가야함
                    # 따라서 딕셔너리에 좌표를 key값 생명력을 리스트로 모아놓고 끝날 때 더 높은 걸 넣어줘야함
                    spread_cell_dict.setdefault((ni,nj),[]).append(life)

            if t+1 < life*2: # 분열후 아직 죽지 않았다면
                temp_q.append([x,y,life,t+1]) #임시 세포 큐에 넣기

        # q=temp_q.copy()
        q=temp_q[:]
        for cell_xy, cell_life in spread_cell_dict.items():
            q.append([cell_xy[0],cell_xy[1],max(cell_life),0])
    return len(q)

T=int(input())
for tc in range(1,T+1):
    N,M,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=dfs()
    print(f'#{tc} {result}')
