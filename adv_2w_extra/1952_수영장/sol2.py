import sys
sys.stdin=open('input.txt')

# 접근 방법2
# 3월 기준으로 생각: 2월 까지의 최소 금액 + 본인의 금액 중 최소 금액
# 이전의 최소 금액들을 활용해서 내 최소금액을 구할 수 있다
# DP 활용하기
# 왜 DP로 활용한가
# 1. 작은 문제로 분할이 가능해야 한다
#   - 전체 문제의 합 = 각 달까지의 최소 금액들이 쌓여서 완성
#   -> 각 달까지의 최소 금액 문제로 생각
# 2. 뒤에 결과를 구할 때 앞에서 구했던 결과가 변하면 안된다.

T = int(input())
for tc in range(1,T+1):
    cost = list(map(int,input().split()))
    # index 너무 헷갈려
    days = [0] + list(map(int,input().split()))
    dp = [0]*13 # 1에서 12월 최소 금액들을 저장
    dp[1] = min(days[1]*cost[0],cost[1])
    dp[2] = min(days[1] * cost[0], cost[1])

    for i in range(1,13):
        # 현재 달의 최소 비용을 계산
        # 1~2월까지는 이전달 +1 일권 구입 / 이번달 + 1달 권 구입
        # 3월 이후 이전 달 + 1일 권 구입 / 이전 달 + 1달 권 / 3달 전에 3달권 구입 중 최소
        dp[i]= min(dp[i-1]+(days[i]*cost[0]),dp[i-1]+cost[1])

        # index 오류를 피하기위해 3월 이후로 계산
        if i>=3:
            # 1일권 vs 1달권 vs 3달권
            dp[i] = min(dp[i],dp[i-3]+cost[2])
    result= min(dp[12],cost[-1])
    print(f'#{tc} {result}')