import sys
sys.stdin=open('input.txt')

def dfs(x,y,de_list,dir,end): # x,y는 현재좌표, de_list 먹은 디저트번호 리스트,
    global max_desert             # dir 방향, end 시작지점
    if dir==3 and x==end[0] and y==end[1] and len(de_list) > 3:  # 시작점 도착
        if max_desert < len(de_list):
            max_desert = len(de_list)
        return

    if x<0 or x>=N or y<0 or y>=N: #범위 벗어나는 경우
        return

    if arr[x][y] not in de_list: # 이전까지 먹어본 적 없는 디저트 일경우
        dfs(x+dxy[dir][0],y+dxy[dir][1],de_list+[arr[x][y]],dir,end) #직진하기
        if dir <3:
            dfs(x+dxy[dir][0],y+dxy[dir][1],de_list+[arr[x][y]],dir+1,end) #방향 꺾기
    return
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    # 오른쪽위,오른쪽아래,왼쪽위,왼쪽아래 순서중요!!
    # 방향은 어짜피 중복이라 한방향만 생각하기
    dxy=[[1,1],[1,-1],[-1,-1],[-1,1]]
    max_desert=0
    for i in range(N):
        for j in range(N):
            if (i==0 or i==N-1) and (j==0 or j==N-1): #모서리는 시작점이 될 수 없음
                continue
            dfs(i,j,[],0,[i,j])

    if max_desert:
        print(f'{tc} {max_desert}')
    else:
        print(f'{tc} -1')
