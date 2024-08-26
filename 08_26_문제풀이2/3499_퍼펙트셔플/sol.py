import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N = int(input()) #카드 수
    card = input().split()
    deck = [0]*N

    d = (N+1)//2 #아래오는 카드 시작

    i1=0
    i2=d
    i3=0 # 새로만들 덱
    while i3 < N: # 셔플이 끝나기 전이면
        if i1 < d:
            deck[i3] = card[i1]
            i1 += 1
            i3 += 1
        if i2 < N:
            deck[i3] = card[i2]
            i2 += 1
            i3 += 1
    print(f'#{tc}', *deck)