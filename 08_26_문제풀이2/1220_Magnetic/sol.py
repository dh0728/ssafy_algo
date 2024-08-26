import sys
sys.stdin= open('input.txt')

N_pole = 1
S_pole = 2

for tc in range(1,11):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    # 1= N극에 끌림(위로 이동), 2= S극에 끌림(아래로 이동)
    # 위에 N극 밑에 S극

    cnt = 0 # 교착상태 갯수
    for j in range(N): # 열 우선순회
        np=0           # 아래로 향하는 N극이 있는지 표시
        for i in range(N):
            if arr[i][j]==N_pole:
                np=1
            elif arr[i][j]==S_pole and np ==1: # 교착상태 발생
                cnt +=1
                np=0
    print(f'#{tc} {cnt}')








