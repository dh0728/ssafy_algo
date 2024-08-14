import sys
sys.stdin = open('input.txt')

def dfs(cnt, string):
    global result

    if result: # 이미 조합완성한 단어가 있으면
        return

    if abs(cnt[1]-cnt[2]) >1: # 01 과 10의 차이가 2개 이상인 경우는 존재 할 수 없다
        return

    if sum(cnt) ==0: #모두 조합했으면 리턴
        result = string
        return

    # 마지막 문자가 0 으로 끝나는 경우 00, 01만 나올 수 있음.
    # 마지막 문자가 1 로 끝나는 경우 10, 11 만 나올 수 있음.
    if string[-1] == '0':   # 조합 끝이 0 인 경우
        if cnt[0] > 0:      # 00 선택
            cnt[0]-=1       # 선택 문자열 개수 감소
            dfs(cnt,string+'0')
            cnt[0]+=1       # 다른 선택을 위해 복원

        if cnt[1] > 0:      # 01 선택
            cnt[1]-=1
            dfs(cnt,string+'1')
            cnt[1]+=1

    if string[-1] == '1':   # 조합 끝이 1 인 경우
        if cnt[2] > 0:      # 10 선택
            cnt[2]-=1       # 선택 문자열 개수 감소
            dfs(cnt,string+'0')
            cnt[2]+=1       # 다른 선택을 위해 복원

        if cnt[3] > 0:      # 11 선택
            cnt[3]-=1
            dfs(cnt,string+'1')
            cnt[3]+=1
    # return

T = int(input())
for tc in range(1, T+1):
    binary_cnt=list(map(int, input().split()))
    binary_list=['00','01','10','11']
    result=''

    for i in range(len(binary_list)):
        if binary_cnt[i]==0:   # 없는 문자열의 경우 사용 X
            continue

        binary_cnt[i]-=1 # 선택 문자열 개수 감소
        dfs(binary_cnt,result+binary_list[i])
        binary_cnt[i]+=1 # 다른 문자열 선택을 위해 복원
    if result:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} impossible')


