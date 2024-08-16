import sys
sys.stdin =open('input.txt')

from collections import deque

T=int(input())
for tc in range(1,T+1):
    N, M, K = map(int,input().split()) # N 사람수 , M초 후 완성, K개 완성
    arr=list(map(int,input().split()))
    arr.sort()
    q=deque()
    for a in arr:
        q.append(a)
    time=1 # 시간
    cnt=0 # 붕어빵 수
    result='Possible'
    bef_cl=0
    # if tc==547:
    #     print(f'N {N} M {M} K {K}')
    #     print(q)

    while q:
        come=q.popleft() # 첫손님 방문 시간
        if come==0: #시작 시간 방문 손님
            result = 'Impossible'
            break
        if come !=bef_cl: # 다음손님이 전 손님과 다른 시간대에 방문할 경우
            for t in range(time+1,come+1):
                if t%M ==0: # M초 후마다 붕어빵 K 개 완성
                    cnt +=K
                if t==come: # 손님 오는 시간으로 시간 업데이트
                    time=t
            bef_cl = come
        # if tc==547:
        #     print(come)
        #     print(cnt)
        cnt -= 1
        if cnt < 0:  # 붕어빵 없으면 break:
            result='Impossible'
            break
    print(f'#{tc} {result}')



