import sys
sys.stdin=open('input.txt')

def find_min(depth,cost):
    global min_cost
    if cost > min_cost: # cost가 최소를 넘어가면 더이상 계산 필요 없음
        return
    if depth==N:
        if min_cost > cost:
            min_cost =cost
    for i in range(N):
        if visited[i]:
            continue
        visited[i]=1
        find_min(depth+1,cost+arr[i][depth])
        visited[i]=0

T=int(input())
for tc in range(1,T+1):
    N=int(input())  # N 제품 수
    arr=[list(map(int,input().split())) for _ in range(N)]
    min_cost=N*99
    visited=[0]*N
    find_min(0,0)
    print(f'#{tc} {min_cost}')