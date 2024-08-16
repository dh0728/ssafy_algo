import sys
sys.stdin = open('input.txt')

from collections import deque

def find_num(n,N):
    num=''
    #생성 가능한 수 리스트에 넣기
    for i in range(N):
        num+=q[i]
        if i%n==n-1:
            num_list.append(num)
            num=''
def trans_16_to_10(M):
    num_10_list=[]
    for num in num_set:
        num_10_list.append(int(num,16)) #16진수 10진수로 변환
    return num_10_list

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    n=N//4 #한변에 들어가는 숫자 수이자 회전 수
    q=deque()
    arr=list(input())
    for a in arr:
        q.append(a)
    num_list=[]
    for _ in range(n):
        find_num(n,N)
        start_num=q.popleft() # 맨앞에 숫자 빼기
        q.append(start_num) # 맨뒤로 넣기
    num_set=set(num_list) # set으로 변환
    list_10=trans_16_to_10(M)
    list_10.sort(reverse=True)
    print(f'#{tc} {list_10[M-1]}')
