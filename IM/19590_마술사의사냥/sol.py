import sys
sys.stdin = open('input.txt')

def magic(arr, K, N):
    dxy=[[1,1],[-1,1],[-1,-1],[1,-1]] #오른쪽위, 오른쪽아래, 왼쪽아래, 왼쪽위(시계방향)
    max_cnt=0   #최고값
    for i in range(N):  #중심죄표arr[i][j]
        for j in range(N):
            count=0
            for dx,dy in dxy: #방향백터 만큼 반복
                ni = i
                nj = j
                for _ in range(K):  #K값만큼 칸수 이동
                    ni+=dx
                    nj+=dy
                    # print(ni, nj)
                    if ni < 0 or ni > N-1 or nj < 0 or nj > N-1: continue #범위 벗어나면 무시
                    count+=arr[ni][nj]
            if count > max_cnt:
                max_cnt=count
    return max_cnt

N=int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K=int(input())
result= magic(arr,K,N)
print(result)


# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# K = int(input())
#
# di = [-1, 1, 1, -1]
# dj = [1, 1, -1, -1]
#
# max_value = 0
# for i in range(N):
#     for j in range(N):
#         S = 0
#         for e in range(len(di)):
#             for k in range(1,K+1):
#                 ni = i + di[e]*k #di[e]=-1 k=1 ni= i + -1, k=2 ni= i + -1 + -1
#                 nj = j + dj[e]*k #di[e]=1
#                 if 0 <= ni < N and 0 <= nj < N:
#                     S += arr[ni][nj]
#         if max_value < S:
#             max_value = S
#
# print(f'{max_value}')