import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = input()
    max_num=0       #1이 최대로 반복된 횟수
    count=0         #반복중 1이 연속해서 나오는 수
    for i in range(N):
        if arr[i] == '1':   #1일 때 count +1
            count+=1
            if i==N-1 and count > max_num:  #마지막숫자가 1일때
                max_num=count               #count가 max_num보다 클경우 교체
        elif arr[i] != '1' and count != 0:  #1이 중간에 끊겼을 경우
            if count > max_num:
                max_num = count
            count=0
    print(f'#{tc} {max_num}')



