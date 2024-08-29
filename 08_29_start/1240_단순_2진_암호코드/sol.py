import sys
sys.stdin = open('input.txt')

def exam_condition(num_list):
    even=0  #짝수
    odd=0   #홀수
    for i in range(1,9):
        if i%2: #홀수이면
            odd+=num_list[i]
        else:   #짝수이면
            even+=num_list[i]
    sum_code=odd*3+even
    if sum_code%10==0:  # 10에 배수이면 조건 만족
        return sum(num_list)
    return 0

def cal_code(code):
    code_dict={'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
    num=[0]*(8+1) #암호 코드의 숫자개수 +1
    for i in range(8):
        n=code_dict.get(code[i * 7:(i + 1) * 7], -1)    # 비트7개씩 슬라이싱해서 code_dict에 키값 존새할시 value 반환
        if n==-1:       # 올바르지 않은 코드이면 바로 0리턴
            return 0
        num[i+1]=n      # 변환된 코드 숫자로 리스트에 저장 [0, 7, 5, 7, 5, 5, 0, 2, 7]
    return num

def find_code(arr):
    for a in arr:
        # 끝에서부터 문자열 인덱스 55까지 1있으면 그 순간 부터 암호
        # index M-1(맨끝) 부터 55까지 순회
        for j in range(M-1,54,-1):
            if a[j]=='1':    #1찾으면
                tran_code=cal_code(a[j-55:j+1]) # 암호 숫자로 변환하는 함수 호출
                if tran_code !=0:               # 숫자로 잘 변환되면
                    return tran_code            # 변환된 숫자암호리스트 리턴
                else:
                    return 0                    # 변환실패시 0리턴

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())    # N 세로의 길이 , M 가로의 길이
    arr=[input() for _ in range(N)]

    trans_code=find_code(arr)   # 암호코드 찾는 함수 호출
    if trans_code !=0:
        result = exam_condition(trans_code) # 변환 성공시 올바른 코드인지 검사
    print(f'#{tc} {result}')


