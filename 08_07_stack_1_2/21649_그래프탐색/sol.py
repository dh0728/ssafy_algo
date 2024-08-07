import sys
sys.stdin = open('input.txt')

def DFS(s, V): # s 시작 ,V 간선개수
    visited[s]=1
    stack=[]
    v=s #현재 정점
    result=[v]
    while True:
        for w in adjl[v]:
            if visited[w]==0:   # 방문 안한 정점이면
                stack.append(v) # 스택리스트에 정점 넣기
                visited[w]=1    # 방문표시
                v=w             # 현재 정점 업데이트
                result.append(v)
                break           # 인접 간선 없을 시 break
        else:
            if stack:           # 더이상 갈 정점 없으면 이전 정점으로 돌아가기
                v=stack.pop()
            else:
                break
    return result

V,E = map(int, input().split()) # V 정점의 개수 E 간선의 개수
arr = list(map(int, input().split()))
visited=[0]*(V+1)   #방문한 노드
adjl=[[] for _ in range(V+1)]       #인접리스트 초기화
s =1 #시작정점은 1
for i in range(E):
    v1 = arr[i*2]   # 무향그래프
    v2 = arr[i*2+1]
    adjl[v1].append(v2)
    adjl[v2].append(v1)
print(adjl)
result=DFS(s, V)
print(f'#1 {"-".join(map(str,result))}')


