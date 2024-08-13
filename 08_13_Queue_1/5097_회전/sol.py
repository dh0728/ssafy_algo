import sys
sys.stdin = open('input.txt')

from collections import deque

T=int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    q=deque(list(input().split()))
    i=1
    while i<=M:
        n= q.popleft() #앞에 숫자 빼기
        q.append(n)    #뒤로 넣기
        i += 1         #횟수 카운트
    print(f'#{tc} {q[0]}')