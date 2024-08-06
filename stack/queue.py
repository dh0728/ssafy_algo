from collections import deque

total_candy = 20    # 총 마이쮸 개수
last_person = None  #마지막에 마이쭈를 받는 사람
person_queue = deque()  # (사람, 받는 개수)를 저장하는 공간(큐)

person_queue.append((1,1)) #첫번 째 사람이 1개를 받는다고 줄섬
total_person_cnt=1

#마이쭈가 남아 있는 동안
while total_candy >0:
    # 마이쭈 받아가고, 줄서고, 다른 사람 합류하고
    # 줄 선 사람 중에 제일 앞에 있는 사람이 누구인지와 받을 마이쮸 개수를 꺼낸다.
    person, candy_to_receive = person_queue.popleft()

    # 남은 마이쮸가 받을 마이쭈보다 개수가 작거나 같을 경우
    # 마지막으로 마이쮸를 받은 사람을 현재 사람으로 설정, 나눠주는 행위 스탑
    if total_candy - candy_to_receive <=0:
        last_person = person
        break
    # 받은 마이쮸만큼 총 개수에서 뺌
    total_candy -=candy_to_receive
    # 다음 사람 번호를 늘리고
    total_person_cnt +=1
    #받은 사람이 다시 줄을 서고
    person_queue.append((person, candy_to_receive+1))
    #다음 받을 사람도 줄을 선다.
    person_queue.append((total_person_cnt))

print(f"마지막 마이쮸는 {last_person}")