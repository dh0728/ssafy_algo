import sys
sys.stdin = open('input.txt')

def cal(left, right, oper):
    return eval(f'{left} {oper} {right}')

def postorder(node):
    '''
        이번에는 트리를 구성할 때 없는 자식 노드 번호는 기록하지 않았다.
        왼쪽, 오른쪽 자식이 반드시 있는 경우가 있다.
        언제-> 연산자인 경우만 있다.
        tree[node][1] -> '+-*/'
    '''

    if arr[node][1] in ['+','-','*','/']:
        left=postorder(arr[node][2])
        right=postorder(arr[node][3])
        # print(left, right)
        return cal(left, right,arr[node][1])
    else:
        return arr[node][1]


for tc in range(1,2):
    N = int(input())
    # node 번호 인덱스로 사용할 값만 int로 형변환 해서 tree 정보 기록
    arr=[list(map(lambda x:int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    arr.insert(0,0)
    # print(arr)
    result=postorder(1)
    print(f'#{tc} {result}')
