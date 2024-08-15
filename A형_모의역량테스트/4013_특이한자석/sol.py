import sys
sys.stdin = open('input.txt')

def dfs(mag, dir): #mag = 회전자석, dir 1 시계방향, -1 반시계방향
    ch[mag]=1
    l_mag=mag-1
    r_mag=mag+1
    if mag >0: #왼쪽 범위 안에 들어가고
        if arr[mag][6] != arr[l_mag][2] and not ch[l_mag]:
            dfs(l_mag,-1*dir)
    if mag <3: # 오른쪽 범위 안에 들어가고
        if arr[mag][2] != arr[r_mag][6] and not ch[r_mag]:
            dfs(r_mag, -1*dir)

    if dir==1: # 시계방향 뒤에꺼 때고 앞에 넣기
        # m=arr[mag].pop()
        # arr[mag].insert(0,m)
        arr[mag]= [arr[mag].pop()] + arr[mag]
    else:   # 반시계 방향 앞에꺼 때고 뒤에 넣기
        arr[mag]=arr[mag][1:] + [arr[mag][0]]



T=int(input())
for tc in range(1,T+1):
    K=int(input()) #회전 횟수
    num=4
    arr=[list(map(int,input().split())) for _ in range(num)]
    # [회전자석, 방향]
    # 1 시계방향, -1 반시계방향
    # N =0 , S=1
    rotaion_list=[list(map(int,input().split())) for _ in range(K)]

    for i in range(K):
        ch = [0] * num
        dfs(rotaion_list[i][0]-1, rotaion_list[i][1]) # 기준자석(index라 -1), 방향

    result=0
    for i in range(num):
        if arr[i][0]:
            result+=2**i
    print(f'#{tc} {result}')

