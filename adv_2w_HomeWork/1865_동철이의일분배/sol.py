import sys
sys.stdin=open('input.txt')

def dfs(depth,p):
    global max_p
    if p <=max_p: # 1보다 작은 값을 항상 곱하기 때문에 한번 max값보다 작아지면 절대 커질수 없음
        return
    if depth==N: # 확률 계산 끝나면
        if max_p<p:
            max_p=p
        return
    for i in range(N): # depth번 직원이 i번 일을 배분 받기
        if visited[i]:
            continue
        visited[i]=1 #
        dfs(depth+1,p*arr[depth][i]*0.01)
        visited[i]=0
    return

T=int(input())
for tc in range(1,T+1):
    N=int(input()) # N 직원 수
    arr=[list(map(int,input().split())) for _ in range(N)]
    max_p=0
    visited=[0]*N
    dfs(0,100)
    print(f'#{tc} {max_p:.6f}')