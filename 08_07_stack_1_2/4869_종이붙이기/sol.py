import sys
sys.stdin= open('input.txt')

def paper(n):
    if n >= 3:
        memo[n]=paper(n-1) + 2*paper(n-2)   # DP(N)= DP(N-1)-2DP(N-2)
    return memo[n]                          # N=2 or N=1일 때는 해당값 반환

T = int(input())
for tc in range(1,T+1):
    N=int(input())  # 가로의 크기
    N //=10         # 보기 좋기 N 자르기 N=30 -> 3
    memo=[0]*(N+1)  # N에 따른 결과 N=index인 곳에 넣기위해 N+1크기에 리스트 생성
    memo[1]=1       # N=10 일때 1
    memo[2]=3       # N=30 일때 3
    paper(N)
    print(f'#{tc} {memo[-1]}')