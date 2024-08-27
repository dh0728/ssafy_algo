import sys
sys.stdin=open('input.txt')


def preorder(node):
    global root_num , n_2_num, i
    if node == 0:   # node가 0이면 리턴
        return

    preorder(left[node])

    i += 1  # 중위 순휘에 따흔 노드 순회 순서에 따라 노드에 값이 들어감
    if node==1: # node==1 이 루프 노드의 노드 번호
        root_num=i  # root_num에 루프에 들어간 값 넣기
    if node==N//2:  # 노드번호가 N//2 일때
        n_2_num=i   # 값 넣기

    preorder(right[node])

# 중위 순회 (테스트케이스1)
# N=6
# left [0, 2, 4, 6, 0, 0, 0]
# right [0, 3, 5, 0, 0, 0, 0]
# 답 #1 4 6

# pre_order(1) 로 시작
# node=1 -> pre_o(left[1]=2) -> node=2 -> pre_o(left[2]=4) -> node=4 -> pre_o(left[4]=0) -> node=0 ->return
# node=4 일 때 i = 1 -> pre_o(right[4]=0) -> return ->
# node=2 일 때 i = 2 ->pre_o(right[2]=5) -> node=5 -> pre_o(left[5]=0) -> node=0 -> return 0 ->
# node=5 일 때 i = 3 -> pre_o(right[5]=0) -> return ->
# node=1 일 때 i = 4 -> node=1이므로 root_num=i
# pre_o(right[1]=3) -> node=3 -> pre_o(left[3]=6) -> node=6 -> pre_o(left[6]=0) -> return ->
# node=6 일 때 i=5 -> pre_o(right[6]=0) -> return ->
# node=3 일 때 i=6 node==N//2이므로 n_2_num=6 -> pre_o(right[3]=0) -> return


T=int(input())
for tc in range(1,T+1):
    N=int(input())

    # 중위 순회 문제
    left=[0]*(N+1)
    right=[0]*(N+1)

    for i in range(1,N//2+1):   # 부모 번호를 인덱스로 자식 노드 번호를 저장
        if i*2 <=N: #노드 번호가 N 이하 일 경우 많 넣기
            left[i]=i*2
        if i*2+1 <=N:
            right[i]=i*2+1

    print(left)
    print(right)
    root_num=0  # 루트에 저장된 값 초기화
    n_2_num=0   # N//2번 노드에 저장된 값
    i=0
    preorder(1) # root 노드부터 순회 시작
    print(f'#{tc} {root_num} {n_2_num}')