import sys
sys.stdin=open('input.txt')
#input = sys.stdin.readline


N = int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
result=0

for i in range(1,N):
    for j in range(i+1):
        if j==0: # 왼쪽 끝이면
            arr[i][j] +=arr[i-1][j]
        elif j==i: # 오른쪽 끝이면
            arr[i][j] +=arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j]) #윗줄에 왼쪽 오른쪽중 더큰 것 넣기

print(max(arr[N-1]))



