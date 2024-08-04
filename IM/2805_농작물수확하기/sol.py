import sys
sys.stdin=open('input.txt')

def income(N,arr):
    # 중앙열부터 세기 시작
    # 한줄씩 위 혹은 밑으로 열이 이동할 때마다 세는 칸의 수가 두칸씩 감소
    # 중앙열의 인덱스는 N//2 행이동 횟수도 N//2
    count=0
    dx=[1,-1]
    new_i=N//2 #농장 중앙 row
    count_j=N   #해당 row에 수확하는 칸수
    upper_i=N//2
    lower_i=N//2
    for i in range(N//2+1):
        for j in range(count_j):    #row이동마다 수확하는 칸수 2칸씩 감소
            if i==0:
                count+=arr[new_i][i+j] #중앙row는 한번만 더한다
            else:
                count+=arr[upper_i][i+j]   #위아래row 더해주기
                count+=arr[lower_i][i+j]
        upper_i+=1  #중심 row 위칸으로 이동
        lower_i-=1  #중심 row 아래칸으로 이동
        count_j-=2  #수확하는 칸수 두칸 감소
    return count




T=int(input())
for tc in range(1, T+1):
    N=int(input())
    arr=[list(map(int,input())) for _ in range(N)]
    result=income(N,arr)
    print(f'#{tc} {result}')

