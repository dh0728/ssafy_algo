import sys
sys.stdin=open('input.txt')

def push_bttn(robo,bttn):
    global time
    if time == robo_dict[robo][0]: #시간이 같으면
        robo_dict[robo][0] += abs(bttn - robo_dict[robo][1]) + 1  # 전지점에서 현재지점까지 이동시간 + 누르는 시간(1)
        robo_dict[robo][1] =bttn
        time=robo_dict[robo][0]
    else:
        # 전 스위치가 눌러지는 시간보다 현재 스위치가 눌려지는데 필요한 시간이 큰경우
        if time - robo_dict[robo][0] > abs(robo_dict[robo][1]-bttn):
            time +=1
            robo_dict[robo][0]=time
            robo_dict[robo][1]=bttn
        # 전 스위치가 눌려지는 시간보다 현재 스위치가 눌려지는데 필요한 시간이 작은 경우
        else:
            time +=abs(robo_dict[robo][1] -bttn) - (time - robo_dict[robo][0]) + 1
            robo_dict[robo][1]=bttn
            robo_dict[robo][0]=time
    return

T=int(input())
for tc in range(1,T+1):
    arr=list(input().split())
    N=arr[0] #버튼갯수
    robo_dict = {'B': [0, 1], 'O': [0, 1]}  # 로봇: 시간, 현재위치
    bttn_list=[]
    time=0
    for i in range(1,len(arr),2):
        push_bttn(arr[i], int(arr[i+1]))

    print(f'#{tc} {time}')
