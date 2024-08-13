

import sys
sys.stdin = open('input.txt')
from collections import deque

def enque(item):   #삽입
    global rear
    rear = (rear + 1) % (N+1)
    c_queue[rear] = item

def dequeue():    #삭제
    global front
    front = (front + 1) % (N+1)
    return c_queue[front]

def isFull():   #포화 검사
    return (rear + 1) % (N+1) == front

def isEmpty():  #공백 검사
    return front == rear

def Qpeek():    #빼기
    return c_queue[(front + 1) % (N+1)]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 화덕의 크기, M 피자의 수
    arr = list(map(int, input().split()))   #치즈 수가 있는 피자 배열
    pizza_q= deque()
    for i in range(1,len(arr)+1):
        pizza_q.append([arr[i-1], i]) #피자의 치즈양과 번호가 들어있는 리스트로 이루어진 큐 생성
                                      #케이스1 결과 값 deque([[7, 1], [2, 2], [6, 3], [5, 4], [3, 5]])

    c_queue = [0] * (N + 1) # 원형 큐 초기화
    rear = 0
    front =0
    result=0
    # 화덕 가득 채워주기
    for _ in range(N):
        enque(pizza_q.popleft())

    # 화덕이 완전히 비게되면 종료되는 while 문
    while True:
        check = dequeue()  # 출구에 있는 피자를 확인
        if front ==rear:
            result =check[1]
            break
        if check[0] // 2 == 0:  # 치즈가 다 녹았다면
            if pizza_q: #아직 안넣은 피자가 있다면 넣기
                enque(pizza_q.popleft())
        else:  # 치즈 안녹았으면
            check[0] //= 2  # 치즈 양 줄이고
            enque(check)  # 다시 넣어준다

    print(f'#{tc} {result}')

