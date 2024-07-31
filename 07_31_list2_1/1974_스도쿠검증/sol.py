import sys
sys.stdin = open('input.txt')

T= int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result=1
    for i in range(9): #행 과 열의 숫자 비교
        cnt_row = [0] * 10  #행의 숫자 카운트 배열
        cnt_col = [0] * 10  #열의 숫자 카운트 배열
        for j in range(9):
            cnt_row[arr[i][j]]+=1   #있는 숫자 카운팅
            cnt_col[arr[j][i]]+=1
        if (2 in cnt_row) or (2 in cnt_col):    # 두번 들어가는 경우 찾기
            result=0
            break
    if result==1:
        for i in range(0,9,3):  #3 X 3 사각형에서 숫자 확인
            for j in range(0,9,3):
                cnt= [0] * 10
                for x in range(3):
                    for y in range(3):
                        cnt[arr[i+x][j+y]]+=1   #있는 숫자 카운팅
                if 2 in cnt:                    #두번 들어가는 경우 찾기
                    result=0
                    break
    print(f'#{tc} {result}')