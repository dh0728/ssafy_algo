import sys
sys.stdin =open('input.txt')

def is_True(case):
    stack=[]
    for c in case:
        if not stack and (c=='}' or c==')'): #닫힌 괄호부터 만나면
            return 0
        if c == '{' or c=='(':  #열린 괄호들 만나면 리스트에 추가
            stack.append(c)
        if c=='}':  #짝이 맞는지 확인
            if stack[-1] != '{': #짝이 안맞으면 리턴
                return 0
            stack.pop() #맞으면 리스트에서 빼기
        if c==')':  #짝이 맞는지 확인
            if stack[-1] != '(':  #짝이 안맞으면 리턴
                return 0
            stack.pop() #맞으면 리스트에서 빼기
    if stack:   # 괄호가 남아 있으면 틀린것
        return 0
    return 1

T=int(input())
for tc in range(1,T+1):
    case=input()
    result=is_True(case)
    print(f'#{tc} {result}')