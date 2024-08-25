
import sys
sys.stdin = open('input.txt')

def check_stack(case):
    ch_dict={')':'(' , '}':'{'}
    s=[]
    for c in case:
        if c in ch_dict.values(): # c:(일 떄 스택리스트에 삽입
            s.append(c)
        elif c in ch_dict.keys(): # c:)일 때
            if not s or s[-1] != ch_dict[c]: # 스택리스트에 짝이 있는지 올바른 순서 인지 확인
                return False
            s.pop()
    return not s

T=int(input())
for tc in range(1,T+1):
    case=input()
    result =check_stack(case)
    if result:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

