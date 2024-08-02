import sys
sys.stdin = open('input.txt')

def read_col(arr):
    max_j=0     #단어들 중 제일 긴 단어의 길이 찾기
    for li in arr:
        if len(li)>max_j:
            max_j=len(li)

    word=''
    for j in range(max_j):
        for i in range(len(arr)):
            if j < len(arr[i]): #j가 현재 읽는 단어의 index이내 일때문 받아오기
                word += arr[i][j]
    return word

T=int(input())
for tc in range(1,T+1):
    arr =[list(input()) for _ in range(5)]
    result=read_col(arr)
    print(f'#{tc} {result}')
