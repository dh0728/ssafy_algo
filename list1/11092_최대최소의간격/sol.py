import sys
sys.stdin = open('input.txt')

T= int(input())

for test_case in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))

    min_num=11
    max_num=0

    min_i=0
    max_i=0
    for i,v in enumerate(arr):
        if v < min_num:
            min_num = v
            min_i = i+1
        else:
            pass

        if v > max_num or v == max_num:
            max_num=v
            max_i = i+1
        else:
            pass
    print(f'#{test_case} {abs(max_i-min_i)}')