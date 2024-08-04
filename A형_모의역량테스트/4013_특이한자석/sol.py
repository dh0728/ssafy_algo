import sys
sys.stdin = open('input.txt')

def rotation(arr, k): #기준 자석 회전
    idx= k[0]-1 #회전시키는 자석의 index
    N=len(arr[0]) #자석모서리 갯수
    rot_arr=[0]*N
    for j in range(N):
        if k[1]==1: #시계방향 회전
            if j==0:
                rot_arr[0]=arr[idx][-1]
            else:
                rot_arr[j]=arr[idx][j-1]
        else:   #반시계방향 회전
            if j==0:
                rot_arr[-1]=arr[idx][0]
            else:
                rot_arr[j-1]=arr[idx][j]
    arr[idx]=rot_arr
    print(arr)

T=int(input())
for tc in range(1,T+1):
    K=int(input())  #회전횟수
    arr=[list(map(int,input().split())) for _ in range(4)]  #자석배열
    k_arr =[list(map(int,input().split())) for _ in range(K)] #회전하는 자석번호, 방향 1:시계 -1:반시계
    dy=[1,-1]
    for k in k_arr:
        idx = k[0] - 1
        rotation(arr ,k)
        for c in range(len(dy)):
            ni = idx
            for d in range(len(arr)):
                ni+=c
            if ni<0 or ni>len(arr)