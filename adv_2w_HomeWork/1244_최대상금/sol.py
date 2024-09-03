import sys
sys.stdin=open('input.txt')

## 틀린코드 테케 1개 오류남
def find_same_num(num):
    for i in range(len(num)-1):
        if num[i]==num[i+1]:
            return 0
    return 1

def dfs(cnt):
    if cnt==N: # 종료조건
        ch_list.append(int(''.join(num_arr)))
        return
    for i in range(num_len-1):
        for j in range(i+1,num_len):
            num_arr[i],num_arr[j]=num_arr[j],num_arr[i] # 값들 교환
            if num_arr[i]== num_arr[j]: # 같은 값은 교환 x
                continue
            if int(''.join(num_arr)) == max_num:
                ch_list.append(max_num)
                return
            dfs(cnt+1)
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i] # 값들 교환

T=int(input())
for tc in range(1,T+1):
    arr=list(input().split())
    num_arr=list(arr[0]) # 숫자판
    N=int(arr[1]) # 교환횟수
    if N >=7:
        if N%2: #홀수
            N=5
        else:
            N=6
    max_num=int(''.join(map(str,sorted(map(int,num_arr),reverse=True))))
    num_len=len(num_arr)
    ch_list=[]
    dfs(0) # 종료조건= 교환횟수 도달시 종료
    result=max(ch_list)
    if N>=5 and not N%2: # N이 5이상이면서 짝수이면
        result=list((str(result)))
        sm=find_same_num(result) # 같은수가 있는경우는 1과 10의 자리 바꿀 필요 X
        if sm:
            result[-1],result[-2] = result[-2], result[-1] # 1의 자리와 10의 자리만 바꿔서 출력
        print(f'#{tc} {"".join(result)}')
    else:
        print(f'#{tc} {result}')

