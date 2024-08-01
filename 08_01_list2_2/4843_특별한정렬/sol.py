import sys
sys.stdin =open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    n=1
    while n<N+1:
        for i in range(0,N-1):
            for j in range(i+1,N):
                if n%2==0:  #큰값찾기
                    if arr[i]<arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]
                else:  #작은값찾기
                    if arr[i] > arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]
            n+=1
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()