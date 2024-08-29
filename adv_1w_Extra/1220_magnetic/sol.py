import sys
sys.stdin=open('input.txt')

def find_magntic(y):
    N_mag=1
    S_mag=2
    cnt=0 # 교착상태 갯수
    np=0  # 현재 순회중 만난 자석 개수
    for i in range(N):
        if arr[i][j]==N_mag: #N극 성질 자성체를 만나면
            np+=1
        elif arr[i][j]==S_mag: #S극 성질 자성체를 만났는데
            if np:  # 전에만난 자석이 n극이면 교착상태완성
                cnt+=1
                np=0
    return cnt

for tc in range(1,11):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]

    # 1 N극 성질,파란자성체 S극으로 끌려감
    # 2 S극 성질,빨간자성체 N극으로 끌러감
    sum_magn=0
    for j in range(N):
        sum_magn+=find_magntic(j)
    print(f'#{tc} {sum_magn}')

