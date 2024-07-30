import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N=정류장 갯수 , K = 한번 충전으로 최대한 이동할 수 있는 정류장 수, M= 충전기가 설치된 정류장 수
    K, N, M= map(int,input().split())
    arr=[0]*(N+1)
    li=list(map(int,input().split()))
    for v in li:
        arr[v]=1 #버스 정류장 있는 곳 1로 표시

    count=0     #충전횟수
    loc=K       #현재위치 초기값:K
    bef_ch=0    #전 충전 위치 초기값:시작지점
    while loc < N:  #현재위치가 정류장개수보다 작을 때 까지 반복
        if arr[loc]==1: #한번에 최대로 이동 가능한 곳에 충전소 있으면 count+1
            count +=1
            bef_ch=loc
            loc+=K
        elif arr[loc]==0:   #현재 위치에서 충전이 불가능 하면 한칸 뒤로
            loc-=1
            if bef_ch==loc: #전 충전 위치까지 돌아오면 충전 불가로 처리
                count =0
                break
    print(f'#{tc} {count}')





    # diff_bs=[]  #충전소 간의 거리 차이
    # for i in range(0,M):
    #     if i==0:
    #         diff_bs.append(arr[i]-0)
    #     elif i == M-1:
    #         diff_bs.append(N-arr[i])
    #     else:
    #         diff_bs.append(arr[i]-arr[i-1])




