import sys
sys.stdin=open('input.txt')

def dfs(depth ,sum_n):
    global min_n
    if depth==N: # 다 더한 경우
        if sum_n >=B:
            if min_n > sum_n:
                min_n=sum_n
        return
    if sum_n >= B: # 보다 커지면 중지
        if min_n > sum_n:
            min_n=sum_n
        return

    dfs(depth+1,sum_n+arr[depth]) # 현재 점원 탑에 쌓기 선택
    dfs(depth + 1, sum_n)   # 현재 점원 패스

T=int(input())
for tc in range(1,T+1):
    N,B=map(int,input().split()) # N 점원수, B 선반 높이
    arr=list(map(int,input().split()))

    min_n=10000*N
    dfs(0,0)
    print(f'#{tc} {min_n-B}')

