import sys
sys.stdin = open('input.txt')

def dfs_route(start, end):
    visited=[0]*(end+1)
    stack=[]
    visited[start]=1    # 출발정점 방문표시
    v=start             # v는 현재 정점
    while True:
        for w in adjl[v]: # adjl[v]은 현재 정점에서 갈 수 있는 정점 리스트
            if visited[w]==0: #방문 한 적 없는 정점이면
                v=w #현재 정점 업데이트
                stack.append(v) #스택리스트에 현재 정점 삽입
                visited[v]=1 #해당 정점 방문 표시
            if w==end:
                return 1
        else:
            if stack:   # 현재정점에서 더이상 가본 정점이 없는 경우
                v=stack.pop()
            else:
                return 0


for tc in range(1,11):
    T, E = map(int, input().split())     # T: 테스트케이스 번호 , E: 간선수
    arr =list(map(int, input().split()))
    adjl=[[] for _ in range(99)]         # 인접리스트 초기화
    start=0
    end=99
    for i in range(0,E*2,2):             # 인접리스트 할당
        adjl[arr[i]].append(arr[i+1])
    result=dfs_route(start,end) #경로 찾기 함수 호출
    print(f'#{T} {result}')