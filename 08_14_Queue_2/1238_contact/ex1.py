import sys
sys.stdin=open('input.txt')

from collections import deque
def BFS(start):
    visited=[0]*101
    visited[start]=1
    q=deque()
    q.append([start,1])
    while q:
        n ,depth = q.popleft()
        for k in node[n]:
            if visited[k] != 0:
                continue
            q.append([k,depth+1])
            visited[k]=depth+1
    return visited

def find_maz(v,m):
    for i in range(100,-1,-1):
        if v[i] ==m:
            return i


T=10
for tc in range(1,T+1):
    N,S=map(int,input().split())
    arr=list(map(int,input().split()))
    node=[[] for _ in range(101)]
    for i in range(0,N,2):
        node[arr[i]].append(arr[i+1])

    v=BFS(S)
    max_depth=max(v)
    result=find_maz(v,max_depth)
    print(f'#{tc} {result}')

