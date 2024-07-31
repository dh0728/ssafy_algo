import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N =int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dx=[1,1,-1,-1]  #좌축방향백터
    dy=[1,-1,1,-1]  #상하방향백터
    sum_num=arr[2][2]   #중심좌표
    for i in range(len(dx)):
        ni = 2
        nj = 2
        for _ in range(2):
            ni += dx[i] #좌우방향벡터 만큼 +
            nj += dy[i] #상하방향벡터 만큼 +
            sum_num +=arr[ni][nj]
    print(f'#{tc} {sum_num}')