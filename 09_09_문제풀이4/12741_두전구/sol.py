import sys
sys.stdin=open('input.txt')

def light_time(a,b):
    if a[0]> b[0]: # b전구가 먼저 켜졌다면
        a,b=b,a # 순서 바꾸기

    if a[1]<b[0]: # 동시에 켜지는 시간 없으면
        return 0
    else:
        if a[1]<b[1]:# a전구가 먼저 꺼졌으면
            return a[1]-b[0] #
        else: # b전구가 먼저꺼졌으면
            return b[1]-b[0]

T=int(input())
result=[]
for tc in range(1,T+1):
    times=list(map(int,input().split()))
    A=times[:2] # A 전구 켜진시간
    B=times[2:] # B 전구 켜진시간

    result.append(light_time(A,B))
for tc in range(1,T+1):
    print(f'#{tc} {result[tc-1]}')