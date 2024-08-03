import sys
sys.stdin=open('input.txt')

def income(N,arr,dy):
    # 중앙열부터 세기 시작
    # 한줄씩 위 혹은 밑으로 열이 이동할 때마다 세는 칸의 수가 두칸씩 감소
    # 중앙열의 인덱스는 N//2 행이동 횟수도 N//2
    count=0
    for j in range(N):  #중심열은 전체행 다 더해짐
        count+=arr[N//2][j]
    for i in range(N//2):
        햣


T=int(input())
for tc in range(1, T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dy=[1,-1]
    result=income(N,arr,dy)

