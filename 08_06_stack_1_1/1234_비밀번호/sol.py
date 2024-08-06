import sys
sys.stdin = open('input.txt')

def check_stack(case):
    s= []
    for c in case:
        if not s or c != s[-1]: #스택리스트 비어 있거나 전 숫자와 다른 경우 스택에 삽입
            s.append(c)
            continue
        s.pop() # 연속되는경우 top값 빼기
    return s

for tc in range(1,11):
    case = list(input().split(' '))
    result=check_stack(case[1])
    print(f'#{tc} {"".join(result)}')