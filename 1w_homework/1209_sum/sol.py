import sys
sys.stdin = open('input.txt')

for _ in range(1,11):
    T = int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    max_sum=0
    cr1 = 0
    cr2 = 0
    # i가 순회할 때마다 각행의 합, 열의 합계산
    for i in range(len(arr)):
        col_sum=0   #열의 합
        row_sum=0   #행의 합
        cr1+=arr[i][i]  #왼쪽 대각선 합
        cr2+=arr[i][99-i]   #오른쪽 대각선 합
        for j in range(len(arr)):
            col_sum+=arr[i][j]
            row_sum+=arr[j][i]
        if col_sum >= row_sum:  #행 열에 값에 따라 최댓값 재할당
            if col_sum > max_sum:
                max_sum = col_sum
        else:
            if row_sum > max_sum:
                max_sum = row_sum
    if cr1 >= cr2:  #for문 종료후 행과 열을 비교해 구한 최댓값과 대각선값 들을 비교
        if cr1 > max_sum:
            max_sum = cr1
    else:
        if cr2 > max_sum:
            max_sum = cr2

    print(f'#{T} {max_sum}')



