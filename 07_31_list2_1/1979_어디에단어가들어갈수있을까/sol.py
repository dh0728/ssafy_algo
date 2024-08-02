import sys
sys.stdin = open('input.txt')

def sh_row_word(N,K,arr):
    word=0
    for i in range(N):
        for j in range(N-K+1):
            if arr[i][j]==1:
                if j>0 and arr[i][j-1]==1:  #카운팅시작 앞 글자가 비어 있으면 크 순회단계는 무시
                    continue
                count=1 #글자수 카운트
                nj=j+1
                while True:
                    if nj<N and arr[i][nj]==1: #col이 N이하이고 arr 값이 1일 경우
                        nj+=1
                        count+=1
                    else:
                        break   #글자 수 끝나면 break
                if count==K:
                    word+=1
    return word

def sh_col_word(N,K,arr):
    word=0
    for i in range(N-K+1):
        for j in range(N):
            if arr[i][j]==1:
                if i>0 and arr[i-1][j]==1: #카운팅시작 앞 글자가 비어 있으면 크 순회단계는 무시
                    continue
                count=1 #글자수 카운트
                ni=i+1
                while True:
                    if ni<N and arr[ni][j]==1: #col이 N이하이고 arr 값이 1일 경우
                        ni+=1
                        count+=1
                    else:
                        break   #글자 수 끝나면 break
                if count==K:
                    word+=1
    return word

T=int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split())
    arr= [list(map(int, input().split())) for _ in range(N)]
    count=sh_row_word(N,K,arr)
    count+=sh_col_word(N,K,arr)
    print(f'#{tc} {count}')
