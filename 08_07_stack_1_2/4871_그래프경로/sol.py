import sys
sys.stdin=open('input.txt')

def dfs_route(start, end, V):
    stack=[]
    visited=[0]*(V+1)
    v=start
    visited[v]=1
    while True:
        for w in adjl[v]:
            if visited[w]==0:
                v=w
                stack.append(v)
                visited[v]=1
                if v == end:
                    return 1
        else:
            if stack:
                v=stack.pop()
            else:
                return 0

T=int(input())
for tc in range(1,T+1):
    V, E= map(int,input().split())  # V 정점 수 E 간선 수
    arr=[]
    for _ in range(E):
        arr.append(list(map(int,input().split()))) # 간선 리스트
    start,end = map(int,input().split()) # start 시작 정점, end 종료 정점
    adjl=[[] for _ in range(V+1)]
    for li in arr:
        adjl[li[0]].append(li[1])   #인접리스트 할당
    # print(adjl)
    result=dfs_route(start, end, V)
    print(f'#{tc} {result}')
