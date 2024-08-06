import sys
sys.stdin = open('input.txt')

def game_start(visited,j,arr):
    i=0

    # dxy = [[1, 0], [0, -1], [0, 1]]
    dxy=[[0,-1] , [0,1] , [1,0]]
    cnt=1  #총이동한 칸수
    while i != SIZE-1:
        for dx, dy in dxy:
            ni = i+dx
            nj = j+dy
            if 0 > ni or ni >= SIZE or 0 > nj or nj >= SIZE:  #범위 벗어나면 continue
                continue
            # print(f'ni={ni} nj={nj}')
            # print(arr[ni][nj])
            if not arr[ni][nj]: # 사다리가 아닌 경우
                continue
            if visited[ni][nj]: #이미 방문한 길이면 continue
                continue
            visited[ni][nj]=1 #방문한 위치 표시
            i=ni
            j=nj
            cnt+=1
    return cnt


for tc in range(1,11):
    T=int(input())
    SIZE =100   # arr의 행 길이
    arr = [list(map(int, input().split())) for _ in range(SIZE)]
    arr_len = len(arr[0]) # arr으 col 길이
    min_route=SIZE*arr_len  #최단 경로 길이
    result=0 #최단 경로로 가는 j
    for j in range(arr_len):
        if arr[0][j]==1:
            visited = [[0]*100 for _ in range(SIZE)] #방문했는지 체크
            route_len=game_start(visited,j,arr)
            if route_len < min_route:
                min_route=route_len
                result = j
    print(f'#{tc} {result}')






