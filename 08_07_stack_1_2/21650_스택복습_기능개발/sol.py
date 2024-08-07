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
