import sys
sys.stdin = open('input.txt')

pwd = {
    (3,2,1,1):0,
    (2,2,2,1):1,
    (2,1,2,2):2,
    (1,4,1,1):3,
    (1,1,3,2):4,
    (1,2,3,1):5,
    (1,1,1,4):6,
    (1,3,1,2):7,
    (1,2,1,3):8,
    (3,1,1,2):9
}

hex_to_bin={
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010', #10
    'B':'1011', #11
    'C':'1100', #12
    'D':'1101', #13
    'E':'1110', #14
    'F':'1111', #15
}

def exam_condition(num_list):
    even=0  #짝수
    odd=0   #홀수
    for i in range(1,8):
        if i%2: #홀수이면
            odd+=num_list[i]
        else:   #짝수이면
            even+=num_list[i]
    sum_code=odd*3+even+num_list[8]
    if sum_code%10==0:  # 10에 배수이면 조건 만족
        return sum(num_list) # 조건 만족시 더한 값 리턴
    return 0    # 불만족시 0 리턴
def exam_code(code):
    global result
    idx=code.rfind('1')
    # print(code)
    dec_code=[0]
    while idx >=0:
        if code[idx]=='1':
            ratio=[0,0,0] # 암호별 맨앞에 0의 비율을 제외한 비율
            while code[idx]=='1':   #pwd (3,2,1,1) 비율중 맨뒤 1의 비율
                ratio[2]+=1
                idx -=1
            while code[idx]=='0':   #pwd (3,2,1,1) 비율중 중간 0의 비율
                ratio[1]+=1
                idx -=1
            while code[idx]=='1':   #pwd (3,2,1,1) 비율중 중간 1의 비율
                ratio[0]+=1
                idx -=1
            code_len=min(ratio) # 하나의 코드의 개수는 7의 배수 bit 7,14,21,28,35..
            n1=7*code_len-sum(ratio)    # pwd (3,2,1,1) 비율중 처음 0의 비율
            ratio.insert(0,n1)   # 처음 0의 비율은 코드개수에서 나머지 비율을 뺀값
            idx -= 1
            ratio=list(map(lambda x : x//code_len, ratio))
            dec_code.insert(1,pwd[(ratio[0],ratio[1],ratio[2],ratio[3])]) #pwd[(3,2,1,1)]=0
            if len(dec_code)==9:    # 8개 코드 다 변환 완료시 검사 함수로 검사
                code_sum=exam_condition(dec_code)
                result+=code_sum    # 결과값 더하기 올바르지 않은 코드는 0이 더해짐
                if tc==13:
                    print(code_sum)
                dec_code=[0]        # 다시 다른 암호 검사를 위해 초기화
        else:
            idx -=1

T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # N 세로의 길이 M 가로의 길이
    arr=set([input() for _ in range(N)]) #그냥 바로 set으로 받기
    result=0
    for a in arr:
        hex_to_bin_code=''
        check=0
        for j in range(M):
            if a[j] !='0': # 0이아니면
                check=1 # 암호있는 코드 체크
            hex_to_bin_code += hex_to_bin[a[j]]
        if check:
            exam_code(hex_to_bin_code) # 암호있는 코드만 변환 함수 호출
    print(f'#{tc} {result}')



