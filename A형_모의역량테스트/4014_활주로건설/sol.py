import sys
sys.stdin=open('input.txt')

def find_route_row(start, x): # start: 시작좌표, x: 경사로의 길이
    cnt =1
    for i in range(1,N):
        if arr[start][i] == arr[start][i-1]: # 같은 높이면 길이 +1
            cnt+=1
        elif arr[start][i] - arr[start][i-1] ==1: # 높이가 한칸 높아지면
            if cnt >=X: # 경사로를 설치하기 길이 가 충분하면
                cnt =1
            else:
                return 0
        elif arr[start][i-1] - arr[start][i] ==1: # 높이가 한칸 낮아지면
            if cnt >=0: # 경사도가 낮아졌다가 또 낮아질 때 또 낮아지기 전에
                        # 높이에서의 경사로 설치는 cnt가 0이상일 때 가능
                cnt = 1 -X # 낮아지는 경우 경사로를 -로 해서 길이가 충분한지 판단
            else:
                return 0
        else: # 높이차가 2이상 이면
            return 0
    if cnt >=0:
        return 1
    return 0

def find_route_col(start, x): # start: 시작좌표, x: 경사로의 길이
    cnt =1
    for i in range(1,N):
        if arr[i][start] == arr[i-1][start]: # 같은 높이면 길이 +1
            cnt+=1
        elif arr[i][start] - arr[i-1][start] ==1: # 높이가 한칸 높아지면
            if cnt >=X: # 경사로를 설치하기 길이 가 충분하면
                cnt =1
            else:
                return 0
        elif arr[i-1][start] - arr[i][start] ==1: # 높이가 한칸 낮아지면
            if cnt >=0: # 경사도가 낮아졌다가 또 낮아질 때 또 낮아지기 전에
                        # 높이에서의 경사로 설치는 cnt가 0이상일 때 가능
                cnt = 1 -X # 낮아지는 경우 경사로를 -로 해서 길이가 충분한지 판단
            else:
                return 0
        else: # 높이차가 2이상 이면
            return 0
    if cnt >=0:
        return 1
    return 0

T= int(input())
for tc in range(1, T+1):
    N, X=map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    result=0
    for i in range(len(arr)):
        result +=find_route_row(i,X)
        result +=find_route_col(i,X)
    print(f'#{tc} {result}')