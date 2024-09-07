import sys
sys.stdin=open('input.txt')

def dfs(month,sum_cost):
    global ans
    if month >12:
        ans= min(ans,sum_cost)
        return
    if sum_cost> ans: # 이미 커지면 더이상 계산 X
        return
    # 1일권으로 모두 구매
    dfs(month+1,sum_cost+(cost[0]*days[month]))
    # 1달권 구매
    dfs(month+1,sum_cost+cost[1])
    # 3달권 구매
    dfs(month+3,sum_cost+cost[2])

T = int(input())
for tc in range(1,T+1):
    cost = list(map(int,input().split()))
    # index 너무 헷갈려
    days = [0] + list(map(int,input().split()))
    ans= cost[-1]
    dfs(1,0)

    print(f'#{tc} {ans}')