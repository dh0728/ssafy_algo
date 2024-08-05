import sys
sys.stdin=open('input.txt')

def find_word(arr):
    max_len = 0
    for i in range(100): #가로 검사
        for k in range(100,1,-1): #회문을 발견할 때 까지 실행줄여 나가면서 확인
            for j in range(0, 101-k): #j =col
                find = True
                for c in range(k//2): #k//2번 비교
                    nj_l=j+c #비교할거 맨 왼쪽 끝값부터 c만큼 점점 더해짐
                    nj_r=j+k-c-1 #비교할거 맨 오른쪽 끝부터 c만큼 점점 빼짐
                    if arr[i][nj_l]!=arr[i][nj_r]:
                        find=False
                        break
                if find:
                    if k > max_len:
                        max_len =k
                        break

    for j in range(100): #세로 검사
        for k in range(100,1,-1): #회문을 발견할 때 까지 실행줄여 나가면서 확인
            for i in range(0, 101-k): #j =col
                find = True
                for c in range(k//2): #k//2번 비교
                    ni_l=i+c #비교할거 맨 왼쪽 끝값부터 c만큼 점점 더해짐
                    ni_r=i+k-c-1 #비교할거 맨 오른쪽 끝부터 c만큼 점점 빼짐
                    if arr[ni_l][j]!=arr[ni_r][j]: #회문아니면 false 하고 break
                        find=False
                        break
                if find:
                    if k > max_len:
                        max_len =k
                        break
    return max_len

T=10
for tc in range(T):
    tc=input()
    arr=[list(input()) for _ in range(100)]
    result=find_word(arr)
    print(f'#{tc} {result}')

