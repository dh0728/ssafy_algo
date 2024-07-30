import sys
sys.stdin = open('input.txt')

T=int(input())

div = [2,3,5,7,11]  #소인수분해 할 리스트
for ts in range(1,T+1):
    num = int(input())  #num:소인수분해할 숫자
    print(f'#{ts}', end=' ')
    for data in div:    #리스트만큼 반복
        count=0
        while True:
            if num%data==0:     #나머지가없을시
                count+=1        #count+1
                num//=data      #num나눈 값으로 재할당
            else:
                print(count, end=' ')
                break   #인수분해 종료시 break
    print('')