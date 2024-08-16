import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(S,G):
    global cnt
    visited= [0]*(V+1)
    q=deque()   # 출발노드 큐삽입
    q.append(S)
    visited[S]=1 # 출발노드 방문표시
    cnt+=1
    while q:
        current_node=q.popleft() # 현재 노드 큐에서 빼기
        cnt+=1
        visited[current_node]=1 #방문노드 방문처리
        # print(current_node)
        if current_node ==G:
            return
        for n in adj[current_node]:
            if not visited[n]:
                q.append(n)

T=int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())
    adj=[[] for _ in range(V+1)]
    for k in arr:
        adj[k[0]].append(k[1])
        adj[k[1]].append(k[0])
    # print(adj)
    cnt=0
    BFS(S,G) #출발 S 도착 G
    print(f'#{tc} {cnt}')

