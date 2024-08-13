from collections import deque

def solution(priorities, location):
   q=deque()
   for i in range(len(priorities)):
      q.append([priorities[i],i])  # [우선순위,순서]
   cnt=0 #실행 순서 초기화
   while True:
       process=q.popleft()
       for i in range(len(q)):
           if q[i][0]>process[0]:   #우선순위 더 높은거 발견하면
               q.append(process) #다시 q에 넣기
               break
       else:
           cnt+=1
           if process[1]==location: #원하는 위치에 값이 실행된거 확인
               return cnt
