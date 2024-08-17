import sys
sys.stdin=open('input.txt')

def find_top():
    max_top=0
    for i in range(N):
        for j in range(N):
            if maps[i][j]>max_top:
                max_top=maps[i][j]

T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split())
    maps=[list(map(int,input().split())) for _ in range(N)]
    find_top()