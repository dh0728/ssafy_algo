import sys
sys.stdin=open('input.txt')

# A < B < C
# 만족하려면 최소 먹어야하는 사탕 개수는?
# 만족하는 경우가 없으면 -1 출력

def eat_candy():
    cnt=0
    if arr[-1] <3 : # 세번째 상자가 3보다 작으면 만족시킬 수 없다.
        return -1
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>=arr[i+1]: # 다음 상자보다 사탕수가 크거나 같은 경우
            cnt+=arr[i]-arr[i+1]+1 # 먹어야 하는 최소 사탕수
            arr[i]=arr[i+1]-1
            if arr[i] <=0: # 상자가 비워지면 -1 리턴
                return -1
    return cnt

T=int(input())
for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    result=eat_candy()
    print(f'#{tc} {result}')