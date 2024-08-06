import sys
sys.stdin= open('input.txt')
#계산기 푸는법
# 1. 중위표현식을 후위표현식으로 변환
# 방법
# - 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시표현
# - 각 연산자를 그에 대응하는 오른쪽 괄호 뒤로 이동
# - 괄호를 제거 예시) (6 + ((5*(2-8))/2)) -> 6528-*2/+

# 2. 스택을 활용해서 피연산자(숫자)를 스택에 삽입
# - 피연산자를 만나면 스택에 삽입
# 3. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산 결과를 다시 스택에 push
# 4. 스식이 끝나면, 마지막으로 스택을 pop하여 출력
def trans_formula(arr):
    op_dict={'+':1, '-':1, '*':2, '/':2} #연산자우선순위 정리
    s= [] #스택 정의
    result=''
    for a in arr:   #변환식 순회
        if a.isnumeric():   # a가 숫자인지 검사
            result += a #숫자이면 바로 결과에 삽입
        elif a in op_dict:  # a가 연산자라면
            if len(s) != 0 and op_dict[a] <= op_dict[s[-1]]: #스택리스트가 비어 있지 않고 a연산자의 우선순위가
                result += s.pop()                            #스택리스트의 최신값의 연산자가 a 우선순위보다 높거나 같으면 result에
                                                             #스택 리스트에 최신값 삽입
            s.append(a) #
    while s:
        result +=s.pop()
    return result

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
    return s.pop()

T=10
for tc in range(1, T+1):
    N= int(input())
    arr=list(input())
    trans= trans_formula(arr) #후위표기식으로 변환
    result=cal_formula(trans) #후위표기식연산 함수 호출
    print(f'#{tc} {result}')