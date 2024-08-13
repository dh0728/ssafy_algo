from collections import deque

def solution(bridge_length, weight, truck_weights):
    # bridge_length : 다리에 올라갈 수 있는 트럭 수 이자 다리 길이
    # weight : 다리가 견딜 수 있는 무게
    # truck_weights : 트럭 별 무게
    total_truck = deque()
    n=len(truck_weights)
    for k in truck_weights:
        total_truck.append([k, 0])  # (트럭무게, 다리에서의 시간)
    bridge_truck = deque()
    end = []  # 다리를 건넌 트럭
    w = 0  # 현재 건너고 있는 트럭무게
    t = 0  # 시간
    while len(end) < n:
        t += 1  # 시간 증가
        for i in range(len(bridge_truck)):  # 다리위에 트럭들 시간 증가시키기
            bridge_truck[i][1] += 1

        if bridge_truck:    # 다리위에 트럭있고
            if bridge_truck[0][1] > bridge_length: #트럭이 다리를 건너면
                out_truck = bridge_truck.popleft()
                w -= out_truck[0]           # 현재 다리에 트럭들 무게합에서 빼기
                end.append(out_truck[0])    # 건넌 트럭이 담긴 리스트에 추가
        if total_truck:
            if bridge_length > len(bridge_truck) and weight >= w + total_truck[0][0]:
                truck = total_truck.popleft()  # 예시 truck=[7,0]
                bridge_truck.append([truck[0], 1])  # 트럭출발
                w += truck[0]   # 현재 다리에 트럭들의 무게합에 무게 추가
    return t

bridge_length=2
weight=10
truck_weights=[7,4,5,6]
result = solution(bridge_length, weight, truck_weights)
print(result)

