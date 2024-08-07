def solution(progresses, speeds):
    answer = []
    day=[]
    for i in range(len(progresses)):
        n=100-progresses[i]
        cnt=n//speeds[i] #몫 구하기
        if cnt < n/speeds[i]: #몫이 나눈 값보다 작으면 +1
            cnt+=1
        day.append(cnt) #작업완료 날짜 리스트에 삽입
    s=[]
    for i in range(len(day)):
        if not s:
            s.append(day[i])      # 처음에 스택리스트 비어있으면 초기값 넣기
        elif s[0] >= day[i]:      # 처음 작업 완료 기능보다 먼저 완료되는 경우 스택 리스트 삽입
            s.append(day[i])
        elif s[0] < day[i]:       # 처음 작업 완료 기능보다 더 오래
            answer.append(len(s)) # 걸리는 기능 발견시 배포 후 스택리스트 비우고 새기능 만 삽입
            s=[day[i]]
    if s:                         # for문 완료 후 남아있는 기능 있으면 마저 배포
        answer.append(len(s))
    return answer

# progresses                speeds              return
# [93, 30, 55]	            [1, 30, 5]	        [2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

#다른 풀이

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): # Q리스트가 비어 있거나 이전 기능의 배포가능 날짜보다 배포날짜가 큰 경우
            Q.append([-((p-100)//s),1])         # (p-100)//s -> (30-100)//30= -3 음수의 //나눗셈은 -2.3 -> -3
        else:
            Q[-1][1]+=1                         # 이전 기능의 배포가능 날짜가 현재 보고 있는 기능의 배포 날짜가능 날짜보다 큰경우
                                                # +1 ->한번에 배포하는 기능 +1한다는 의미
    return [q[1] for q in Q]                    # 한번에 배포하는 기능 수만 가진 리스트 생성

