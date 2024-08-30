import sys
sys.stdin=open('5176_re_input.txt')

# def hex_to_dec(n):
#

T=int(input())
for tc in range(1,T+1):
    code=input()
    N=int(code[0]) # salf 계산용 숫자
    dec_list=[]

    for i in range(1,len(code),2):
        dec_list.append(int(code[i:i+2],16))
        # hex_to_dec(code[i:i+2]) # 두개씩 쪼개서 변환
    print(dec_list)
