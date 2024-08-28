import sys
sys.stdin = open('input.txt')


T=int(input())
for tc in range(1,T+1):
    N, M, L= map(int,input()) # N 노드 갯수, M 리프노드 갯수, L 값을 출력할 노드 번호
    # 테스트 케이스 1
    # 5 3 2

    arr=list(map(int,input().split()))
    tree=[0]*(N+1)
    for a in arr:
        tree[a[0]]=a[1]



