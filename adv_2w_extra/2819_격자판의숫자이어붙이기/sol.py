import sys
sys.stdin=open('input.txt')

def dfs(depth,x,y,num):
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    if depth==end:
        # set 사용 X
        # if num not in num_list: # 동일한 것이 없다면 넣기
        #     num_list.append(num)
        num_list_set.add(num) # set 사용한것
        return
    for dx,dy in dxy:
        ni=x+dx
        nj=y+dy
        if 0 >ni or ni>=N or 0 > nj or nj>=N: # 범위 벗어나면 패스
            continue
        dfs(depth+1,ni,nj,num+arr[ni][nj])

T=int(input())
for tc in range(1,T+1):
    N=4
    end=7
    num_list=[]
    num_list_set=set()
    arr=[list(input().split()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dfs(1,i,j,arr[i][j])
    # print(f'#{tc} {len(num_list)}')
    print(f'#{tc} {len(num_list_set)}')