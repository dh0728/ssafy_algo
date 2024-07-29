T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(0, N - 1):
        count = 0
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                count += 1
        if count > result:
            result = count

    print(f'#{test_case} {result}')






