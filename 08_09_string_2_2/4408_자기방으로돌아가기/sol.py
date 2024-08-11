import sys
sys.stdin=open('input.txt')

def go_room(arr):
    for x in arr:
        if x[0]>x[1]:   # 반대로 가는 애들 예외 처리
            x[0], x[1]=x[1],x[0]
        go=(x[0]+1)//2
        here=(x[1]+1)//2
        for i in range(go, here+1): #이동경로 만큼 +1
            room[i]+=1

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    room=[0]*201    # 1,2  3,4  5,6 처럼 두개의 방이 경로가 겹침
    go_room(arr)
    result=0
    for x in room:  #room순회하면서 숫자가 제일큰값 찾기
        if x > result:  # 숫자가 제일 큰값 == 동선이 겹치는 횟수
            result=x
    print(f'#{tc} {result}')

