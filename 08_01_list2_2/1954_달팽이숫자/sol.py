import sys
sys.stdin= open('input.txt')

def snail_sort(n):
    arr =  list([0]*n for _ in range(n))
    A=[]
    for c in range(n,0,-1): #한 직선에서 이동하는 칸수 리스트로 할당
        if c == n:
            A.append(c-1)
        else:
            A.extend([c,c])
    A.insert(0,0)   #인덱스와 k를 일치시키위해 0 추가
    k = 1       #직선으로 이동하는 횟수
    arr[0][0]=1 #시작은 1로 고정
    ni = 0  #초기 row_index
    nj = 0  #초기 col_index
    cnt = 2 #arr[0][0]에 자리는 1로 고정이기 때문에 2부터 시작
    while k <= 2*n-1: # 2*n-1 :직선(방향전환없이)으로 이동하는 횟수
        div=k%4 #row와 col로의 이동 방향은 k%4의 값에 따라 규칙적
        if div==1:  # div==1일때 row값 더해짐
            for j in range(A[k]):   # A[k]만큼 칸 수가 이동
                nj+=1
                arr[ni][nj]=cnt
                cnt+=1      # 숫자를 넣고 1씩 더하기
        elif div==2:  # div==2일때 col값 더해짐
            for i in range(A[k]):
                ni+=1
                arr[ni][nj]=cnt
                cnt+=1
        elif div==3:     # div==3일때 row값 빼짐
            for j in range(A[k]):
                nj-=1
                arr[ni][nj]=cnt
                cnt += 1
        elif div==0:    # div==0일때 col값 빼짐
            for i in range(A[k]):
                ni-=1
                arr[ni][nj]=cnt
                cnt += 1
        k+=1
    return arr

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=snail_sort(N)
    print(f'#{tc}')
    for li in arr:
        print(*li)

# A
# N=1 => [1]                  총 2*1-1 = 1회
# N=2 => [2,1,1]              총 2*2-1 = 3회
# N=3 => [3,2,2,1,1]          총 2*3-1 = 5회
# N=4 => [4,3,3,2,2,1,1]      총 2*4-1 = 7회
# N=5 => [5,4,4,3,3,2,2,1,1]  총 2*5-1 = 9회

# 리스트의 길이는 방향전환 없이 이동하는 이동하는 횟수(직선의 횟수)
# 각 리스트의 값은 한 직선에서 이동하는 칸 수