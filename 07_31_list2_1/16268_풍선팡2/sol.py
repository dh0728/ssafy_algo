import sys
sys.stdin = open('input.txt')

def count_flower(arr ,row, col,n,m):
    dx=[-1,0,1,0] #좌우 방향백터
    dy=[0,1,0,-1] #위아래 방향백터
    sum_flw = arr[row][col]
    for i in range(4):
        ni= row+dy[i]   # 상하좌우 index(row)
        nj= col+dx[i]   # 상하좌우 index(col)
        if 0<=ni<n and 0<=nj<m:     #index가 arr안에 있는지 검사
            sum_flw +=arr[ni][nj]
    return sum_flw


T = int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split()) # N: row M:col
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_flw=0
    for i in range(N):
        for j in range(M):
            result = count_flower(arr,i,j,N,M)  #꽃가루 count 함수 호출
            if result > max_flw:
                max_flw = result
    print(f'#{tc} {max_flw}')
