import sys
sys.stdin=open('input.txt')

from collections import deque

def BFS(start):
    visted=[0]*(max_num+1)
    q=deque()
    q.append([start,1])
    visted[start]=1
    while q:
        node,depth=q.popleft() #현재 노드, depth
        for n in adj[node]:    #인접 노드 찾기
            if visted[n] == 0: #방문 한적 없으면
                q.append([n,depth+1])   # 큐에 추가
                visted[n]=depth+1   # 현재 노드 depth+1 visite에 삽입
    return visted

def find_person(m,v):
    for i in range(100,0,-1):
        if v[i]==m:
            return i

T=10
for tc in range(1,T+1):
    max_num=100 #최대로 존재할 수 있는 사람 수
    N,S=map(int,input().split()) #  N 데이터 길이, S 시작점
    adj=[[] for _ in range(max_num+1)]
    arr=list(map(int,input().split()))
    for i in range(0,N,2):
        adj[arr[i]].append(arr[i+1])
    v=BFS(S)

    max_depth = max(v)
    result=find_person(max_depth,v)
    print(f'#{tc} {result}')


