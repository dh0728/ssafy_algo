import sys
sys.stdin = open('input.txt')
#1208
for test_case in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
    # N 덤프 횟수: 0이되면 종료
    while N > 0:
        for i in range(100): #최솟값 index찾기
            if arr[i] < arr[i+1]:
                min_index=i
                break
            elif arr[i] == arr[i+1]:
                continue
            else:
                min_index = i+1

        for j in range(99,-1,-1): #최댓값 index찾기
            if arr[j] > arr[j-1]:
                max_index= j
                break
            elif arr[i] == arr[i+1]:
                continue
            else:
                max_index = j+1

        arr[max_index]-=1
        arr[min_index]+=1
        N -=1
    print(f'#{test_case} {arr[-1]-arr[0]}')

