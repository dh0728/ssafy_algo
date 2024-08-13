import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(1,11):
    T=int(input())
    arr=list(map(int,input().split()))
    q= deque(arr)
    while q[-1] !=0:    # 마지막 값이 0이되면 반복 종료
        for n in range(1,6):    # 사이클 만큼 순회
            num=q.popleft()     # 앞에 값 꺼내기
            num-=n              # 원하는 값만큼 빼기
            if num <= 0:        # 뺀 값이 0이하가 될 경우 중지
                q.append(0)
                break
            q.append(num)       # 0아니면 계속 맨뒤로 다시 넣어주기
    print(f'#{tc}', end=' ')
    while q:
        print(q.popleft(), end=' ')
    print()
