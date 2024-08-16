import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(S,G):
    q=deque()
    q.append([S,0])  # [출발노드,깊이] 큐삽입
    visited[S]=1 # 출발노드 방문표시
    while q: # 큐에 값 있을 때까지 반복
        current_node, depth =q.popleft() # 현재 노드 큐에서 빼기
        visited[current_node]=1 # 방문노드 방문처리
        if current_node ==G: # 목적지 도착시 깊이 반환
            return depth
        for n in adj[current_node]:
            if not visited[n]:
                q.append([n, depth+1]) # [인접노드,깊이+1]해서 삽입
    return 0
T=int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split()) # V 노드 개수 ,E 간선 정보
    arr=[list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split()) # S 출발 , G 도착
    adj=[[] for _ in range(V+1)]
    visited = [0] * (V + 1) #방문표시 리스트 초기화
    for k in arr:   # 노드 연결 리스트 삽입
        adj[k[0]].append(k[1])
        adj[k[1]].append(k[0])
    # print(adj)
<<<<<<< HEAD
    cnt=0
    BFS(S,G) #출발 S 도착 G
    print(f'#{tc} {cnt}')

=======
    result=BFS(S,G) #출발 S 도착 G
    print(f'#{tc} {result}')
>>>>>>> 60dfab632e0a2e0ba7305529e7706babf276864d
