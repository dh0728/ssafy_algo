import sys
sys.stdin=open('input.txt')
# input = sys.stdin.readline

def exam_square(n):
    color=arr[n][n]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != color: # 다른 색의 종이가 있다면
                return 0
    return 1


# N = 2 , 4, 8, 16, 32, 64, 128
N= int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

blue_cnt=0
white_cnt=0
cut=N
while cut != 0:


