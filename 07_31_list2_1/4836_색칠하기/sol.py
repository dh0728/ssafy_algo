import sys
sys.stdin = open('input.txt')

def c1_draw(c_li):  # 빨강(1) 색칠 함수
    cnt=0
    for i in range(c_li[1],c_li[3]+1):
        for j in range(c_li[0],c_li[2]+1):
            if arr[i][j]==1 or arr[i][j]==3:    #이미 칠해져 있거나 겹친부분 패스
                continue
            else:
                arr[i][j]+=1    #색칠하기
                if arr[i][j]==3:    #겹쳐지면 cnt++
                    cnt+=1
    return cnt
def c2_draw(c_li):  #파랑(2)색칠함수
    cnt=0
    for i in range(c_li[1],c_li[3]+1):
        for j in range(c_li[0],c_li[2]+1):
            if arr[i][j]==2 or arr[i][j]==3:    #이미 칠해져 있거나 겹친부분 패스
                continue
            else:
                arr[i][j]+=2    #색칠하기
                if arr[i][j] == 3:   #겹쳐지면 cnt++
                    cnt += 1
    return cnt


T=int(input())
for tc in range(1,T+1):
    N = int(input())
    color_list=[list(map(int,input().split())) for _ in range(N)] #칠한부분
    arr=[[0]*10 for _ in range(10)]  # 격자
    count=0
    for i in range(N):
        if color_list[i][4]==1:
            count+=c1_draw(color_list[i])   #빨강부분 색칠함수 호출
        else:
            count+=c2_draw(color_list[i])   #파란부분 색칠함수 호출

    print(f'#{tc} {count}')