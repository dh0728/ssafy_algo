import sys
sys.stdin = open('input.txt')

def start(arr, j):
    i=1
    while i < 100:
        if arr[i][j-1]==1:  #왼쪽으로 이동하는 경우
            j -= 1
            while True:
                if arr[i][j-1]==1:  #왼쪽으로 이동하는 만큼 이동
                    j -=1
                else:
                    i +=1       #더이상 오른쪽으로 이동하지 않으면 밑으로
                    break
        elif arr[i][j+1]==1:   #오른쪽으로 이동하는 경우
            j+=1
            while True:
                if arr[i][j+1]==1:  #오른쪽으로 이동하는 만큼 이동
                    j +=1
                else:
                    i+=1        #더이상 오른쪽으로 이동하지 않으면 밑으로
                    break
        elif 0<=i<=98:
            i+=1
        if i==99:               #도착지 도착했을 때
            if arr[i][j]==2:
                return True
            else:
                return False

for ts in range(10):
    T=int(input())
    arr= [list(map(int,input().split())) for _ in range(100)]
    for li in arr:  #제로패딩
        li.insert(0,0)
        li.append(0)
    for j in range(101):
        if arr[0][j]==1:
            result = start(arr, j)
            if result:
                print(f'#{T} {j-1}')
                break
