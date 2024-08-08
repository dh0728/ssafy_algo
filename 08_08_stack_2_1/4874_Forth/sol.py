import sys
sys.stdin=open('input.txt')

def cal_formula(trans): #후위표현식 연산
    s=[]
    for k in trans:
        if k.isnumeric(): #숫자면 스택리스트에 삽입
            s.append(k)
        else:   #연산자라면
            n1=int(s.pop()) #스택리스트에서 꺼내서 연산후 삽입
            n2=int(s.pop()) #int 로 형변환
            if k == '+':
                s.append(n1 + n2)
            elif k== '*':
                s.append(n1 * n2)
            elif k== '-':
                s.append(n1 - n2)
            elif k== '/':
                s.append(n1 / n2)
            elif k=='.':
                print(s)
                return s.pop()
    return s.pop()

T=10
for tc in range(1, T+1):
    case= list(input().split())
    result=cal_formula(case) #후위표기식연산 함수 호출
    print(f'#{tc} {result}')