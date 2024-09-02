import sys
sys.stdin = open('input.txt')


def cal_spend(p):
    global result
    cnt=0                           # 현재 경로 순열에서
    for i in range(len(p)-1):       # 사무실에서 사무실로 이동시 발생하는
        cnt+=arr[p[i]-1][p[i+1]-1]  # 베터리 소비량 모두 더하기
    if result > cnt:                # 최소 소비량 발견시 교체
        result=cnt

def permutation(depth): # 출발지점은 항상 1
    if len(depth)==N:   # 모든 지점을 다 돌았으면
        path.append(depth+[1])  # 마지막에 출발지로 돌아오므로 출발지 추가
        return                  # 해서 path 리스트에 넣고 리턴
    for i in range(2,N+1):
        if visited[i]==1:       # 방문한적있는 사무실이면 패스
            continue
        visited[i]=1            # 사무실 방문처리
        permutation(depth+[i])  # 다음 사무실 방문을 위해 재귀호출
        visited[i]=0            # 현재 사무실 다시 미방문 처리


T=int(input())
for tc in range(1,T+1):
    N=int(input())              # 사무실 수
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=100*N
    path=[]
    visited=[0]*(N+1)
    visited[1]=1                # 1번 사무실 방문처리
    permutation([1])            # 방문 경로 순열리스토로 생성
    for p in path:              # 방문 경로별 베터리 소비량 계산
        cal_spend(p)

    print(f'#{tc} {result}')

