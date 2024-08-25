import sys
sys.stdin=open('input.txt')

from collections import deque
def find_pizza():
    pizza_q=deque()
    for i in range(M): #전체 피자가 들어 있는 큐 생성
        pizza_q.append([i+1,arr[i]])

    q=deque() # 화덕 큐 생성

    # 먼저 화덕에 피자 채우기
    for i in range(N):
        q.append(pizza_q.popleft()) # [피자번호,치즈수]
    while q: #큐가 빌 때까지 반복
        piz_n, chz = q.popleft() # 1번 위치에 피자 빼기
        if not q: # 마지막 피자면 피자 번호 리턴
            return piz_n
        chz //=2
        if chz ==0: #치즈가 다 녹았으면
            if pizza_q:
                q.append(pizza_q.popleft())
            continue
        q.append([piz_n,chz]) # 치즈 덜녹으면 다시 넣기

T=int(input())
for tc in range(1,T+1):
    N, M =map(int, input().split()) # N 화덕의 크기 M 피자의 크기
    arr=list(map(int,input().split()))

    result = find_pizza()
    print(f"#{tc} {result}")








