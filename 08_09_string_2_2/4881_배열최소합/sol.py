import sys
sys.stdin=open('input.txt')
def sum_num(depth,sum, ch):
    global result
    if sum >= result:   # result 넘어가면 종료
        return
    if depth==N:    #row가 arr의 범위를 벗어날 경우
        if sum < result:    # 제일 큰값과 비교
            result=sum
        return
    for j in range(N):  #한줄에 하나씩 선택하면서 더하고 재귀호출
        if not ch[j]:
            ch[j]=1  #선택한 열의 방문 표시
            sum_num(depth+1,sum+arr[depth][j],ch)
            ch[j]=0  #숫자를 선택한 행의 다른 숫자를 선택하기 위해 다시 미방문 표시

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    ch=[0]*N    # 선택한 원소 표시 리스트
    result=N*10
    sum_num(0,0, ch) # 함수에 매번 변하는 것 depth(row), sum(더한값)
    print(f'#{tc} {result}')
