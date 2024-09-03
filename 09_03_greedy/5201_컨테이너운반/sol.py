import sys
sys.stdin=open('input.txt')

def find_w():
    max_w=0
    while t_list and w_list: # 컨테이너와 트럭별 적재중량 리스트 둘 중하나라도 비면 종료
        t=t_list.pop()
        while w_list:
            w=w_list.pop()
            if t >=w: # 트럭에 실을 수 있으면
                max_w+=w
                break
    return max_w

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split()) # N 컨테이너 수, M 트럭의 수
    w_list=list(map(int,input().split())) # N개의 컨테이너의 무게
    t_list=list(map(int,input().split())) # M개의 트럭별 적재용량

    # 트럭당 1개의 컨테이너만 운반 할 수 있음
    # 옮겨진 화물의 전체 무게 출력
    # 한개도 못옮기는 경우 0 출력

    w_list.sort()
    t_list.sort()
    result=find_w()
    print(f'#{tc} {result}')


