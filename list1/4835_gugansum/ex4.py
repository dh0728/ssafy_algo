T = int(input())

for test_case in range(1, T+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    i=0
    max_v=0
    min_v=0
    while i+M <= N:
        sum=0 #더한값
        for j in range(M):
            sum +=arr[i+j]
        if max_v < sum:
            max_v=sum
            if i==0:
                min_v=sum
        elif min_v > sum:
            min_v = sum
        i +=1
    print(f'#{1} {max_v-min_v}')