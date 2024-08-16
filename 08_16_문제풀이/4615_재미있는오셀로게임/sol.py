import sys
sys.stdin=open('input.txt')

def f(i, j, bw, N):
    board[i][j]=bw # 지정된 돌 놓기
    dxy=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    for di, dj in dxy:
        ch = [] # 돌의 색이 바꿔야하는 위치가 들어가는 리스트
        for x in range(1,N):
            ni = i + di*x
            nj = j + dj*x
            # if 0> ni or ni >= N or 0 > nj or nj >= N: # 범위 벗어나는 경우
            #     continue
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj]==0: # 돌은 안놓은 지점이면 break
                    break
                elif board[ni][nj]==bw: # 놓은 돌과 같은 색의 돌이면
                    while ch: # 리스트에서 위치를 하나씩 빼서 색 변환
                        c = ch.pop()
                        board[c[0]][c[1]]=bw
                    break
                else: # 놓은 돌과 다른색의 돌이면 리스트 삽입
                    ch.append([ni,nj])
            else:
                break


def count_bw():
    cnt_b=0
    cnt_w=0
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                cnt_b+=1
            elif board[i][j]==2:
                cnt_w+=1
    return cnt_b, cnt_w

T=int(input())
B=1
W=2
for tc in range(1,T+1):
    N,M= map(int,input().split()) #N 보드 크기, M 놓는 횟수
    arr=[list(map(int, input().split())) for _ in range(M)]
    board =[[0]*(N) for _ in range(N)] # N X N board 준비
    #중심부 돌 배치
    board[N//2-1][N//2-1]=W
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = B
    board[N//2 ][N//2] = W

    # 돌 놓기
    for a in arr:
        f(a[1]-1,a[0]-1,a[2],N)

    b,w=count_bw()
    print(f'#{tc} {b} {w}')
