import sys
sys.stdin=open('input.txt')

# 풀었지만 메모리와 시간이 ㅈㄴ 걸리는 풀이
def dfs(cnt):
    if cnt==N: # 종료조건
        ch_list.append(int(''.join(num_arr)))
        return
    for i in range(num_len-1):
        for j in range(i+1,num_len):
            if num_arr[i]== num_arr[j]: # 같은 값은 교환 x
                continue
            num_arr[i],num_arr[j]=num_arr[j],num_arr[i] # 값들 교환
            dfs(cnt+1)
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i] # 값들 교환

T=int(input())
for tc in range(1,T+1):
    arr=list(input().split())
    num_arr=list(arr[0]) # 숫자판
    N=int(arr[1]) # 교환횟수
    num_len = len(num_arr)  # 숫자의 길이

    # N이 7이상이면 홀수는 N=5일때 짝수는 N=6일때와 같다.
    if N >=7:
        if N%2: #홀수
            N=5
        else:   #짝수
            N=6
    num_len=len(num_arr) # 숫자의 길이
    ch_list=[]
    dfs(0) # 종료조건= 교환횟수 도달시 종료
    print(f'#{tc} {max(ch_list)}')

