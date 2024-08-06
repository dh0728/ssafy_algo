import sys
sys.stdin =open('input.txt')

def stack_fun(case):
    check_dict={')':'('}
    s=[]
    for c in case:
        if c in check_dict.values(): # ( 만나는 경우
            s.append('(')
        elif c in check_dict.keys(): # ) 만나는 경우
            if not s or check_dict[c] != s[-1]: # 스택리스트가 비어있지 않거나 짝이 맞지 않는 경우
                return False
            s.pop()
    return not s    # 최종적으로 s가 완전히 비어있어야 온전한 형태


T = int(input())
for tc in range(1, T+1):
    case = input()
    result= stack_fun(case)
    if result:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {-1}')