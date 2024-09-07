import sys
sys.stdin=open('input.txt')

from collections import deque

def bfs():
    visited=[0]*(N+1)
    visited[1]=0
    q=deque()
    q.append([1,-1]) # 1번 정류장에서 시작, 충전횟수는 1번에서 다른 정류장으로 갈때부터
    while q:         # 카운팅 하고 1번에서 충전기 장착은 카운팅하지 않음 따라서 -1로 시작
        node, cnt = q.popleft()
        if node==N: # 마지막 정류장 도착시 return
            return cnt
        for next in g[node]:
            if visited[next]: # 이미 방문한 정류장은 패스
                continue
            visited[next]=1
            q.append([next,cnt+1]) # [다음 정류장, 충전횟수]

T=int(input())
for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    N=arr[0] # N 정류장 수

    g=[0]
    for i in range(1,len(arr)): # 정류장별 충전기교체에 따른 최대 갈 수 있는 정류장을
        p=[]                    # 연결리스트로 변환
        for j in range(1,arr[i]+1):
            if i+j>N:
                break
            p.append(i+j)
        g.append(p)
    # print(g)
    result=bfs()
    print(f'#{tc} {result}')


