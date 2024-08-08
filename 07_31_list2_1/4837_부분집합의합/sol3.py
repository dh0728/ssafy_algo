import sys
sys.stdin=open('input.txt')

# 4837_부분집합의 합
def dfs_find(v, num, sum):
    global count
    if v > 12 or num>N or sum>K: # 원소 숫자가 N개 이상, 합이 K이상일시 return
        return
    if num==N and sum==K:   #num이 N이거나 sum==K이면 count+1
        count +=1           #만족하는 부분집합수 +1
        return
    else:
        visited[v]=1
        dfs_find(v+1,num+1, sum+v)
        visited[v]=0
        dfs_find(v+1, num, sum)

T=int(input())
for tc in range(1,T+1):
    N, K=map(int, input().split())
    count=0     # N개의 원소를 가지고 합이 K인 부분집합의 갯수
    visited = [0] * (12 + 1) #visited의 index가 집합이 가지는 원소
    dfs_find(1, num=0, sum=0)
    print(f'#{tc} {count}')
