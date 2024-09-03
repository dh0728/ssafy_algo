import sys
sys.stdin=open('input.txt')

# 그리디의 핵심 조건
# 탐욕적 선택 조건(Greedy Choice Property): 각 단계의 선택이 이후 선택에 영향을 주지 않는다.
# 최적 부분 구조(Optimal Substructure): 각 단계의 최선의 선택이, 전체 문제의 최선의 해가 된다

# 탑욕은 항상 이게 맞는지 증명을 해야한다
# 반례는 없는가? 수식표현은?

# 1. 각 단계에서 최적해를 찾아야한다.
# 2. 단계의 결과들을 합하는 방법을 찾아야 한다.
# 3. 각 단계의 합 == 전체 문제의 합이라는 것을 증명해야 한다.

def sort_finish_time():
    for i in range(N-1):
        for j in range(i,N):
            if arr[i][1]> arr[j][1]: # 종료시간이 더 작은 값을 발견하면
                tmp=arr[i]           # 임시변수에 더 큰값 저장
                arr[i]=arr[j]        # 더작은값 앞으로 이동
                arr[j]=tmp           # 임시변수에 저장한 큰값 뒤로 이동
    return

def find_max_work():
    cnt=1
    curr=arr[0][1]
    for i in range(1,len(arr)):
        if arr[i][0]< curr: # 작업시간이 겹친다면
            continue
        cnt+=1              # 작업시간 안겹치면
        curr=arr[i][1]
    return cnt


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    sort_finish_time() # 종료시간을 기준으로 오름차순 정렬

    result=find_max_work()
    print(f'#{tc} {result}')
