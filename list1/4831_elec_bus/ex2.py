T = int(input())

for test_case in range(1, T+1):
    # N=정류장 갯수 , K = 한번 충전으로 최대한 이동할 수 있는 정류장 수, M= 충전기가 설치된 정류장 수
    K, N, M= map(int,input().split())
    arr = list(map(int,input().split()))
    diff_bs=[]  #충전소 간의 거리 차이
    for i in range(0,M-1):
        if i==0:
            diff_bs.append(arr[i]-0)
        else:
            diff_bs.append(arr[i]-arr[i-1])

    print(diff_bs )


