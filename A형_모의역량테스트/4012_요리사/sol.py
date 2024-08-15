import sys
sys.stdin=open('input.txt')

def cal_synergy(li):    # 시너지 계산 리스트
    score=0
    for i in range((N//2)-1):   # 재료 2개씩 정해서 시너지 계산
        for j in range(i+1,N//2):
            score += arr[li[i]][li[j]] + arr[li[j]][li[i]]
    return score

def dfs(depth):
    global min_score
    if depth >= N:  # depth 가 범위 넘어가면 종료
        return
    if ch.count(1)==N//2:   # 4개가 정해지면 A,B리스트에 각 재료 정리
        A=[]
        B=[]
        for i in range(N):
            if ch[i]:
                A.append(i) # 선택한 재료 이면 A
            else:
                B.append(i) # 선택 안한 재료이면 B
        A_score=cal_synergy(A)  # 시너지 계산
        B_score=cal_synergy(B)  # 시너지 계산
        sc=abs(A_score-B_score)
        if sc < min_score:
            min_score=sc
        return
    ch[depth]=1 # 해당 재료 선택
    dfs(depth+1) # 선택한 경우로 재귀호출
    ch[depth]=0 # 해당 재료 선택 취소
    dfs(depth+1) # 선택안한 경우로 재귀 호출


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    ch=[0]*N
    min_score=float('inf')
    dfs(0)
    print(f'#{tc} {min_score}')

