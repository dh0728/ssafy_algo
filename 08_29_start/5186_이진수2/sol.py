import sys
sys.stdin = open('input.txt')

def hex_to_bin(num):
    bin_num=''

    # num에 2를 곱해주고 정수부분 1이면 bin_num에 1 삽입하고 num에 1빼기
    # 0이면 그냥 0 만삽입
    # 1이면 1삽입해주고 종료
    while num != 1.0: # 1이 아닐때 까지 반복
        if len(bin_num)>=13:    # 13자리 이상이면
            return 'overflow'
        num*=2
        if num>1:           # 1보다 커지면
            num-=1
            bin_num+='1'
        elif 1>num>0:       # 1보다 작고 0보다 크면
            bin_num+='0'
        else:               # 1이면
            bin_num+='1'
            return bin_num

T=int(input())
for tc in range(1,T+1):
    N=float(input())
    result=hex_to_bin(N)
    print(f'#{tc} {result}')