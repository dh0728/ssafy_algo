import sys
sys.stdin = open('input.txt')

def cal(left,right,oper):
    # return eval(f'{left} {oper} {right}')
    if oper=='+':
        return left+right
    elif oper=='-':
        return left-right
    elif oper=='*':
        return left*right
    else:
        return left/right
def postorder(node):
    # if str(tree[node]) in '+-*/': # 문자열쓰면 문자열로 안바꿔주면 오류남
    if tree[node] in ['+','-','*','/']: # node 값이 연산자이면
        left=postorder(g[node][0])  # left값 확인
        right=postorder(g[node][1]) # right값 확인
        # print(left, right)
        return cal(left, right, tree[node]) # 후위순회로 둘다 숫자로 만들고 계산
    else:
        return tree[node]   # 숫자면 바로 리턴해서 left or right에 값이 들어가게 하기

for tc in range(1,11):
    N=int(input())
    arr=[list(input().split()) for _ in range(N)]

    tree=[0]*(N+1)
    g=[0]*(N+1)

    # 트리에 값들 해당 노드에 값들 넣어주기
    for a in arr:
        if a[1] in '+-*/':  # 연산자이면 길이가
            tree[int(a[0])]=a[1]
            g[int(a[0])]=[int(a[2]),int(a[3])]  # 연결리스트에 값 넣기
        else:   # 숫자면 int로 변환해서 넣기
            tree[int(a[0])]=int(a[1])

    result=postorder(1)
    print(f'#{tc} {int(result)}')

