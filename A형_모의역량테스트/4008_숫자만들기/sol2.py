import sys
sys.stdin=open('input.txt')

def cal_num(a,b,op): # 현재까지 연산한 값, 연산할 값, 연산자리스트의 index
    if op==0: # 0이면 +
        return a+b
    elif op==1: # -
        return a-b
    elif op==2: # *
        return a*b
    else: # %
        return int(a/b)

def dfs(depth, num):
    global max_n
    global min_n
    if depth >=N-1: # 계산이 끝나면 최대 최소 비교후 삽입
        if num > max_n:
            max_n=num
        if num < min_n:
            min_n=num
        return
    for i in range(len(op_list)): # 연산자 종류만큼 반복
        if op_list[i]:  # 사용되는 연산자의 경우
            op_list[i]-=1 # 사용처리
            dfs(depth+1, cal_num(num,num_list[depth+1],i)) # 재귀호출 cal_num으로 현재까지 계산한 숫자, 다음 계산할 숫자, 연산자넘겨줘 계산
            op_list[i]+=1

T=int(input())
for tc in range(1,T+1):
    N=int(input()) # 숫자의 갯수
    op_list=list(map(int,input().split())) # 연산자 리스트 + - * / 순
    num_list=list(map(int,input().split())) # 숫자 리스트
    min_n=float("inf")
    max_n=float("-inf")
    dfs(0,num_list[0])
    print(f'#{tc} {max_n-min_n}')