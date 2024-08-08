import sys
sys.stdin = open('input.txt')

def trans_formula(case):
    op_dict={'+':1,'-':1,'*':2,'/':2,'(':0}
    stack=[]
    result=''
    for x in case:
        if x.isnumeric():       # x가 숫자라면 result로 넣기
            result+=x
        elif x == '(':  # 열린 괄호는 스택에 넣기
            stack.append(x)
        elif x == ')':          # ) 닫힌 괄호 만날시 stack 리스트에 )가 나올때 까지 빼서 후위식에 삽입
            while stack and stack[-1] !='(':   # stack안에 연산자가 있고 (를 만나기 전까지 반복
                result += stack.pop()
            if stack:  # 여는 괄호를 제거
                stack.pop()
        elif x in op_dict:      # x가 연산자면 우선순위에따라 처리
            if stack and op_dict[x] <= op_dict[stack[-1]]:  #스택에 연산자가 있고 현재 식에 연산자가 스택의 top의 연산자
                result +=stack.pop()                        #보다 작거나 같으면 후위식에 스택에 top을 pop해 후위식에 삽입
            stack.append(x)
    while stack:
        result +=stack.pop()    # 남은 연산자들 다 후위식에 삽입
    return result

T= int(input())
for tc in range(1,T+1):
    case=input()
    result=trans_formula(case)
    print(f'#{tc} {result}')
