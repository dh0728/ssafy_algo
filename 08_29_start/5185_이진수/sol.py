import sys
sys.stdin = open('input.txt')

import string

# 이건 2~36진법까지 변환할 경우
# tmp=string.digits+string.ascii_lowercase #0123456789abcdefghijklmnopqrstuvwxyz

tmp='0123456789abcdef'
def convert(num,base):
    q,r =divmod(num,base) # 연산결과 q=몫 r=나머지
    if q == 0:
        return tmp[r]
    else:
        return convert(q,base)+tmp[r]

T=int(input())
for tc in range(1,T+1):
    arr=list(input().split())
    # int(num,base) -> base 진수인 num을 10진수로 변환해주는 함수수
    # convert(16진수를 10진수로 변환한 값, 최종 변환 진수값)
    bin_num=convert(int(arr[1],16),2)

    if len(bin_num)%4: #나머지가 있으면 앞에 0을 붙여야한다
        for _ in range(4-len(bin_num)%4):   #부족한 숫자 개수만큼 0 더해주기
            bin_num= '0'+bin_num
    print(f'#{tc} {bin_num}')