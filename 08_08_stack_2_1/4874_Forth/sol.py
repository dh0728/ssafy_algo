import sys
sys.stdin=open('input.txt')

#에러처리 다 못한 코드
def is_num(n):  #숫자가 맞는지 판단 음수나 소수도 숫자인지 판단해야함
    try:
        float(n)
    except:
        return False
    else:
        return True

# def cal_formula(trans): #후위표현식 연산
#     s=[]
#     op=['+','-','*','/']
#     for k in trans:
#         if is_num(k): #숫자면 스택리스트에 삽입
#             s.append(float(k))
#         elif k in op:   #연산자라면
#             if len(s)< 2:
#                 return 'error'
#             n1=int(s.pop()) #스택리스트에서 꺼내서 연산후 삽입
#             n2=int(s.pop()) #int 로 형변환
#             if k == '+':
#                 s.append(n2 + n1)
#             elif k== '*':
#                 s.append(n2 * n1)
#             elif k== '-':
#                 s.append(n2 - n1)
#             elif k== '/':
#                 if n1 ==0:  # 0으로 나누면 에러
#                     return 'error'
#                 s.append(n2 / n1)
#         elif k=='.':
#             if len(s)==1:   # 스택이 무조건 하나여야만 출력
#                 return s.pop()
#             else:
#                 return 'error'
#         else:
#             return 'error'  # 연산자가 알 수 없는 연산자 인 경우
#     return 'error'#연산을 다했는데 스택에 값이 남아 있거나 비어 있는 경우
#
# T=int(input())
# for tc in range(1, T+1):
#     case= list(input().split())
#     result=cal_formula(case) #후위표기식연산 함수 호출
#     print(f'#{tc} {result}')

# 정답코드
# .을 연산자일경우 보다 위에 배치

def cal_formula(trans):  # 후위표현식 연산
    s = []
    for k in trans:
        # if k.isdecimal():  # 숫자면 스택리스트에 삽입
        #     s.append(int(k))
        if is_num(k): #숫자면 스택리스트에 삽입
            s.append(float(k))
        elif k == '.':
            if len(s) == 1:  # 스택이 무조건 하나여야만 출력
                return int(s.pop())
            else:
                return 'error'
        else:  # 연산자라면
            if len(s) >= 2:
                n1 = int(s.pop())  # 스택리스트에서 꺼내서 연산후 삽입
                n2 = int(s.pop())  # int 로 형변환
                if k == '+':
                    s.append(n2 + n1)
                elif k == '*':
                    s.append(n2 * n1)
                elif k == '-':
                    s.append(n2 - n1)
                elif k == '/':
                    if n1 == 0:
                        return 'error'
                    else:
                        s.append(n2 / n1)
            else:
                return 'error' # 연산자가 알 수 없는 연산자 인 경우

T = int(input())
for tc in range(1, T + 1):
    case = input().split()
    result = cal_formula(case)  # 후위표기식연산 함수 호출
    print(f'#{tc} {result}')