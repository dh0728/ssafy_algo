import sys
sys.stdin = open('input.txt')
def find_winner(card_cnt):
    run_cnt=0
    for i in range(len(card_cnt)):
        if card_cnt[i]==3: # 연속인 숫자가 3개 이상(run)
            return 1
        if card_cnt[i]>=1: # i번 카드를 가지고 있다면
            idx=i
            while idx<len(card_cnt):   # 카운팅_배열 만큼 반복하면서 횟수 세기
                if card_cnt[idx]>=1:   # 연속해서 카드를 가지고 있는 횟수 카운트
                    run_cnt+=1
                    idx+=1
                else:                  # 연속이 끊기면
                    break
            if run_cnt==3:             # 연속해서 카드를 가지고 있는 횟수가 3이면
                return 1
            else:
                run_cnt=0              # 3회 이하면 다시 카운팅 변수 0으로 초기화
    return 0

T=int(input())
for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    p1_card_cnt=[0]*10 # player1의 카드 카운팅 리스트
    p2_card_cnt=[0]*10 # player2의 카드 카운팅 리스트
    result=0    # 기본값 무승부
    for i in range(len(arr)):
        if (i+1)%2: #홀수이면 player1에게 카드 주기
            p1_card_cnt[arr[i]]+=1
            if i>=4: # 카드 3장이상이면 run이거나 triple인지 검사
                if find_winner(p1_card_cnt): # run or triple 이면
                    result=1
                    break
        else:  #짝수이면 player2에게 카드 주기
            p2_card_cnt[arr[i]]+=1
            if i>=5: # 카드 3장이상이면 run이거나 triple인지 검사
                if find_winner(p2_card_cnt): # run or triple 이면
                    result=2
                    break
    print(f'#{tc} {result}')

