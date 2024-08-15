import sys
sys.stdin=open('input.txt')

def find_bc_list(x,y):
    my_bc=[]
    for i in range(len(bc_list)):
        if abs((x - bc_list[i][0]))+abs(( y - bc_list[i][1])) <= bc_list[i][2]: #현재 위치가 충전범위 안이면
            my_bc.append(i)
    return my_bc

def move_user(x,y,i):
    dxy=[[0,0],[-1,0],[0,1],[1,0],[0,-1]]
    return x+dxy[i][1], y+dxy[i][0] # 좌표이동 x=j , y=i



T=int(input())
for tc in range(1,T+1):
    M, A = map(int, input().split())    # M 총 이동 시간, A BC 갯수
    a_move_li=list(map(int,input().split()))    # A 유저 이동 경로
    b_move_li=list(map(int,input().split()))    # B 유저 이동 경로
    bc_list= [list(map(int,input().split())) for _ in range(A)] # x , y, 범위, 파워
    ax=ay=1
    bx=by=10

    result=0
    for i in range(M+1):    # 현재 자리에서 power 계산 후 따라서 이동:M번 , power 계산:M+1번
        a_list= find_bc_list(ax,ay)
        b_list= find_bc_list(bx,by)

        # A 유저만 접속한 BC 가 있는 경우
        # B 유저만 접속한 BC 가 있는 경우
        # 둘다 있는 경우
        max_power=0
        if a_list and not b_list:
            for a in a_list:    # a:  A유저가 범위 안에 있는 bc의 인덱스(ap_list)
                if max_power < bc_list[a][3]:
                    max_power=bc_list[a][3]
        elif not a_list and b_list:
            for b in b_list:    # a:  B유저가 범위 안에 있는 bc의 인덱스(ap_list)
                if max_power < bc_list[b][3]:
                    max_power=bc_list[b][3]
        else:
            for a in a_list:
                for b in b_list:
                    if a==b: # 둘다 같은 BC에 있다면
                        max_power=max(max_power, bc_list[b][3])
                    else:
                        max_power=max(max_power, bc_list[a][3]+bc_list[b][3])
        result+=max_power
        if i==M:    # 시간 다 흐르면 종료
            break
        ax, ay=move_user(ax,ay,a_move_li[i])
        bx, by=move_user(bx,by,b_move_li[i])

    print(f'#{tc} {result}')

