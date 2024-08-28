import sys
sys.stdin = open('input.txt')

def enq(target):   # 삽입을 위한 함수 , target 트리의 위치
    # 단순히 tree에 삽입 대상을 집어 넣는게 아니라..
    # 삽입 한 후에, 부모 노드와 내 노드의 크기를 비교해서
    # 부모 노드의 값이 내 노드 값보다 크다면, 위치 스왑
    while target //2:
        parent = target //2
        if tree[target] <= tree[parent]:
            tree[target],tree[parent] = tree[parent],tree[target]
        target = parent


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))

    tree=[0]
    last_node =0
    for n in arr:
        tree.append(n)
        last_node +=1
        enq(last_node)