import sys
sys.stdin = open('input.txt')
T=int(input())

di = [0,1,0,-1]
dj = [1,0,-1,0]
for ts in range(1, T+1):
    N=int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total=0
    for i in range(N):
        for j in range(N):
            s = 0
            # i,i 원소의 4방향 원소에 대해
            for k in range(4):
                ni = i +di[k]
                nj = j +dj[k]
                if 0<=ni<N and 0<=nj<N:
                    s +=abs(arr[ni][nj]-arr[i][j]) #실존하는 인접원소 ni,nj
            total += s
    print(f'#{ts} {total}')