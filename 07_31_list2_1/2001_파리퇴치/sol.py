import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N,M= map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    result=0
    for i in range(N):
        for j in range(N):
            sum_num=0
            for k in range(M):  #파리채의 세로크기
                for r in range(M):  #파리채의 가로크기
                    if i+k < N and j+r < N: #배열을 넘어가는 부분을 예외처리
                        sum_num += arr[i+k][j+r]
            if sum_num > result:
                result = sum_num
    print(f'#{tc} {result}')
