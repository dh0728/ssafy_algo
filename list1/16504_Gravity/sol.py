# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     result = 0
#     for i in range(0, N - 1):
#         count = 0
#         for j in range(i + 1, N):
#             if arr[i] > arr[j]:
#                 count += 1
#         if count > result:
#             result = count
#
#     print(f'#{test_case} {result}')

import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_cnt=0
    for i in range(0,N-1):
        count = 0
        for j in range(i+1, N):
            A = N -i - 1
            if arr[i] <= arr[j]:
                count += 1
            else:
                count += 0
        A -=count
        if max_cnt < A:
            max_cnt = A

    print(f'#{test_case} {max_cnt}')





