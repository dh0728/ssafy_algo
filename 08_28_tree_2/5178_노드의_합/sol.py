import sys
sys.stdin = open('input.txt')


# g 연걸 리스트에 index의 값 부터 하나씩 접근해 더하기
# 오른쪽 노드가 0일 경우는 그냥 0 만 더하기
# 부모 노드가 L 이면 계산 종료
def enq():
    for i in range(len(g),0,-1): # i는 부모 노드의 번호
        left_i=2*i
        right_i=2*i+1
        if right_i > N: # 마지막 노드번호보다 보다 오른쪽 노드번호가 크면 0
            right_i=0
        tree[i]=tree[left_i]+tree[right_i] # 자식 노드의 값들 더하기
        if i==L:    # 원하는 값의 부모노드 값 찾으면 리턴
            return tree[i]

T=int(input())
for tc in range(1,T+1):
    N, M, L= map(int,input().split()) # N 노드 갯수, M 리프노드 갯수, L 값을 출력할 노드 번호
    # 테스트 케이스 1
    # 5 3 2

    arr=[list(map(int,input().split())) for _ in range(M)]
    tree=[0]*(N+1)

    g=[]
    for i in range(1,N//2+1):
        left = 2*i  # 왼쪽 자식 리스트 번호
        right = 2*i+1   # 오른쪽 자식 리스트 번호
        if right > N:   # 노드 번호가 개수 이상이면
            g.append([left,0])  # 0 값 넣기
        else:
            g.append([left,right])

    # 리프 노드에 값들 다 넣기
    for a in arr:
        tree[a[0]]=a[1]

    # print(tree)
    # print(g)
    result=enq()
    print(f'#{tc} {result}')





