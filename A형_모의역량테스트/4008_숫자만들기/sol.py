import sys
sys.stdin=open('input.txt')


## 시간초과 발생코드
from collections import deque

def cal_num(ch):
    global max_n
    global min_n
    res=num_list[0]
    for i in range(len(ch)):
        if ch[i]==0:
            res +=num_list[i+1]
        elif ch[i]==1:
            res -=num_list[i+1]
        elif ch[i]==2:
            res *=num_list[i+1]
        else:
            res = int(res/num_list[i+1])
    if max_n < res:
        max_n = res
    elif min_n > res:
        min_n = res


def comb(arr,n):
    used=[0 for _ in range(len(arr))] #선택한 op 표시
    combin_lst=[]
    def generate(chosen,used):
        if len(chosen) ==n: # 갯수만큼 선택 완료 했으면
            cal_num(chosen)
            # combin_lst.append(chosen[:])
            return

        for i in range(len(arr)):
            if not used[i]: # 선택하지 않은 연산자이면
                chosen.append(arr[i]) # 선택
                used[i]=1   #방문 처리
                generate(chosen,used) # 재귀호출
                used[i]=0   # 다시 선택으로 복원
                chosen.pop() # 선택한 op리스트에서 빼기 

    generate([],used)
    return combin_lst


T=int(input())
for tc in range(1,T+1):
    N=int(input()) # 숫자의 갯수
    op_list=list(map(int,input().split())) # 연산자 리스트 + - * / 순
    num_list=list(map(int,input().split())) # 숫자 리스트
    op_li=[]
    min_n=float("inf")
    max_n=float("-inf")
    for i,op in enumerate(op_list): #숫자들 넣기 0:+ , 1:-, 2:*, 3:/
        for _ in range(op):
            op_li.append(i)
    comb(op_li, len(op_li))
    print(f'#{tc} {max_n-min_n}')
