import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N, M=map(int,input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]

    max_v=0 # 가장 긴 구조물 길이
    for i in range(N): # 가로 구조물 확인
        cnt = 0        # 구조물 길이
        for j in range(M):
            if arr[i][j]: # 구조물이면
                cnt +=1
                if max_v < cnt: # 구조물의 최대 길이 찾기
                    max_v = cnt
            else:
                cnt=0

    for j in range(M):
        cnt=0
        for i in range(N):
            if arr[i][j]: # 구조물이면
                cnt +=1
                if max_v < cnt: # 구조물의 최대 길이 찾기
                    max_v = cnt
            else:
                cnt=0

    # 노이즈 만 있는경우
    if max_v==1:
        max_v =0

    print(f'#{tc} {max_v}')

