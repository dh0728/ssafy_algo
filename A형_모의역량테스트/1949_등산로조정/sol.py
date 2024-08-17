import sys
sys.stdin=open('input.txt')

def bfs(x,y):
    print(x,y)
    pass

def find_top():
    max_top=0
    for i in range(N):
        for j in range(N):
            if maps[i][j]>max_top:
                max_top=maps[i][j]
    return max_top

def start(top):
    cnt=0
    for i in range(N):
        for j in range(N):
            if cnt==5:
                return
            if maps[i][j]==top:
                bfs(i,j)
                cnt+=1
    return

T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split())
    maps=[list(map(int,input().split())) for _ in range(N)]
    max_top=find_top()
    start(max_top)