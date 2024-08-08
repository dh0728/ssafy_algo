T = int(input())

for test_case in range(1, T + 1):
    N = int(input())    # N 가로 길이
    arr = list(map(int, input().split())) # 각 줄에 쌓여 있는 상자 수
    result = 0
    for i in range(0, N - 1):   # 마지막 줄은 낙차 존재 X 마지막 줄 전 줄까지 낙차 계산
        count = 0
        for j in range(i + 1, N):   # j = 낙차를 계산하는 줄의 오른쪽에 존재하는 줄
            if arr[i] > arr[j]:     # i 줄보다 높게 j 줄에 상자가 높게 낮게 쌓였으면 낙차 +1
                count += 1
        if count > result:          # 한 줄의 낙차 계산이 끝나면 낙차가 가장 높은 줄과 비교
            result = count

    print(f'#{test_case} {result}')

# import sys
# sys.stdin = open("input.txt")
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     max_cnt=0
#     for i in range(0,N-1):
#         count = 0
#         for j in range(i+1, N):
#             A = N -i - 1
#             if arr[i] <= arr[j]:
#                 count += 1
#             else:
#                 count += 0
#         A -=count
#         if max_cnt < A:
#             max_cnt = A
#
#     print(f'#{test_case} {max_cnt}')





