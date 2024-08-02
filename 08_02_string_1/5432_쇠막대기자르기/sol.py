import sys
sys.stdin = open('input.txt')

def find_lazer(arr): #레이저를 00으로 바꿔주는 함수
    for i in range(len(arr)-1):
        if arr[i]=='(' and arr[i+1]==')':
            arr[i]=0
            arr[i+1]=''
            i+=1

def count_stick(arr):
    new_s=0 #현재 있는 파이프수
    all_stick=0
    cnt=0   #레이저 만난수
    for i in range(len(arr)):
        if arr[i]=='(': #막대기만남
            new_s+=1
            all_stick+=1
        elif arr[i]==')': #막대기이별
            new_s-=1
        elif arr[i]==0: #레이저만남
            cnt +=new_s
    return cnt +all_stick #총 막대수는 각자의 막대기 수가 레이저를 만난 수 + 사용된 막대기 수
                          # 한 막대기가 잘려서 생기는 수는 레이져 만난횟수 +1
                          #예시 막대기 하나가 레이저를 두번 만나면 총 세개로 쪼개짐
T=int(input())
for tc in range(1,T+1):
    arr=list(input())
    find_lazer(arr)#레이저 찾기
    result=count_stick(arr) #파이프 숫자 세주는 함수
    print(f'#{tc} {result}')
