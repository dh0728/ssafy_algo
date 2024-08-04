import sys
sys.stdin = open('input.txt')

def count_flw(arr,N,M): #꽃가루 countin 함수
    dxy=[[0,1],[1,0],[0,-1],[-1,0]] #우하좌상순 방향 백터
    max_flw=0
    for i in range(N):
        for j in range(M):
            cnt=arr[i][j] #상하좌우 카운트하는 횟수
            cnt_flw=arr[i][j] #터진 풍선에서의 꽃가루 총 갯수
            for dx, dy in dxy:
                ni=i
                nj=j
                for _ in range(cnt):    #기준점에 들어있는 꽃가루 갯수만큼 더하는 칸수 반복
                    ni+=dx
                    nj+=dy
                    if ni<0 or ni>N-1 or nj<0 or nj>M-1:    #범위 벗어날 경우 제외
                        continue
                    cnt_flw+=arr[ni][nj]
                if cnt_flw> max_flw:
                    max_flw=cnt_flw
    return max_flw


T= int(input())
for tc in range(1,T+1):
    N, M= map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    result= count_flw(arr,N,M)
    print(f'#{tc} {result}')