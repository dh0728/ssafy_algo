import sys
sys.stdin = open('input.txt')

def check_stack(case):
    for i in range(len(case)-1):
        if case[i] == '(' and case[i+1]==')':
            case[i]='0'
            case[i+1]=''
    s=[]    #현재 파이프의 갯수
    cnt_pi =0   #총 사용한 파이프 수
    cnt_lazer=0 #레이저의 수
    cnt=0 #잘린 쇠파이프 수
    for c in case:
        if c == '(':    #파이프 스택리스트에 추가
            s.append(c)
            cnt_pi +=1
        elif c == '0':  #레이저 만났을 때 =현재의 파이프수만큼 잘림
            cnt_lazer+=1
            cnt += len(s)
        elif c == ')':  #파이프 끝이므로 현재 파이프에서 제외
            s.pop()
    return cnt +cnt_pi  #총 잘린 파이프 수는 파이프 레이저를 만나 잘린 횟수 + 사용한 파이프 수

T=int(input())
for tc in range(1,T+1):
    case=list(input())

    result=check_stack(case)
    print(f'#{tc} {result}')