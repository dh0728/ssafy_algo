import sys
sys.stdin= open('input.txt')
import math

def dfs(depth, kg_l, kg_r): #ch 현재 올려진 무게추 리스트, 현재 왼쪽 무게, 오른쪽 무게
    global cnt
    if kg_l < kg_r: # 오른쪽이 더크면 리턴
        return
    if kg_l >= total_w/2:	# 무게 절반 넘어가면
        n= N-depth	 # 선택 안한 무게추들 카운트
        cnt += (2**n)*math.factorial(n) #선택안한 무게추들 배열되는 경우 만큼 더하고 리턴
        return
    # 다 계산하는 건 너무 비효율적
    # if sum(ch_list)==N: #무게추 다 사용하면 방법 수 +1
    #     cnt+=1

    for i in range(N):
        if ch[i]:  #이미 사용한 무게 추는 패스
            continue
        ch[i]=1

        dfs(depth+1, kg_l+arr[i], kg_r)

        dfs(depth+1, kg_l,kg_r+arr[i])
        ch[i]=0

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        arr= list(map(int,input().split()))
        ch=[0]*N
        cnt=0
        total_w=sum(arr)
        for i in range(N):
            ch[i]=1
            dfs(1, arr[i], 0) #왼쪽에 무게추 주고 시작
            ch[i]=0

        print(f'#{tc} {cnt}')