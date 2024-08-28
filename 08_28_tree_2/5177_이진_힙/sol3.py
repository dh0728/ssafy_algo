import sys
sys.stdin=open('input.txt')

# 노드의 끝으로 보내고 차례로 비교하면서 올림
def enq(num):
    global last
    last +=1    # 현재 마지막 노드 번호
    tree[last]=num  # 마지막 노드에 타겟 번호 넣기
    child = last    # 현재 노드가 자식노드
    parent = child//2   # 자식노드//2 한게 부모노드
    while parent >=1 and tree[parent] > tree[child]: # 타겟 노드에서 부모 노드가 있거나 부모노드가 값이 더 클 경우
        tree[parent], tree[child] = tree[child], tree[parent] # 두개 값 바꿔주기
        child =parent   # 자식 노드 번호 한 높이 올려주기
        parent = child//2   # 부모 노드 번호 한 높이 올려주기

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))

    tree=[0]*(N+1)
    last=0

    for n in arr:
        enq(n)
    # print(tree)
    result=0
    while last:
        last//=2
        result +=tree[last]
    print(f'#{tc} {result}')