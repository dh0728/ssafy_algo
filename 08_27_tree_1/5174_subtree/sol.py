import sys
sys.stdin=open('input.txt')

def preorder(node):
    global cnt
    if node==0:
        return
    cnt +=1
    preorder(left[node])
    preorder(right[node])

T=int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split()) # E 간선수, N 루프
    arr=list(map(int,input().split()))

    left=[0]*(E+2)
    right=[0]*(E+2)

    for i in range(0, len(arr), 2): # 부모 번호를 인덱스로 자식 번호를 저장
        if left[arr[i]]==0:         # 왼쪽에 없으면 왼쪽에 저장
            left[arr[i]]=arr[i+1]
        else:                       # 왼쪽에 있으면 오른쪽에 저장
            right[arr[i]]=arr[i+1]

    cnt=0
    preorder(N)
    # print(left)
    # print(right)
    print(f'#{tc} {cnt}')