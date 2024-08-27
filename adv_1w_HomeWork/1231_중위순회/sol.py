import sys
sys.stdin=open('input.txt')

def preorder(node):
    global result
    if node==0:
        return
    preorder(left[node])
    result += word[node]    # 중위 순회, 노드 방문 시마다 노드에 알파벳 값 추가
    preorder(right[node])

T=10
for tc in range(1,T+1):
    N=int(input())
    arr=[list(input().split()) for _ in range(N)]

    # 셋다 부모 노드의 번호를 인덱스로 사용하는 리스트
    left=[0]*(N+1)  # 왼쪽 자식노드
    right=[0]*(N+1) # 오른쪽 자식노드
    word=[0]*(N+1)  # 노드별 들어있는 알파벳
    for g in arr:
        g[0]=int(g[0])
        if len(g)==4:   # 자식 노드가 왼, 오 다 있을 때
            word[g[0]]=g[1]         # 해당 노드에 알파벳 값 넣기
            left[g[0]]=int(g[2])    # 왼쪽 자식노드 삽입
            right[g[0]]=int(g[3])   # 오른쪽 자식노드 삽입
        elif len(g)==3: # 자식 노드가 왼쪽만 있을 때
            word[g[0]]=g[1]
            left[g[0]] = int(g[2])
        else:   # 자식 노드가 없을 때
            word[g[0]]=g[1]
    result=''
    preorder(1) # 루프 노드부터 순회 시작
    print(f'#{tc} {result}')