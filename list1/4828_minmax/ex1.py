import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    test_list = list(map(int, input().split()))
    max_num=0
    min_num= test_list[0]
    for li in test_list:
        if max_num < li:
            max_num=li
        elif min_num > li:
            min_num=li
    print(f'#{test_case} {max_num-min_num}')