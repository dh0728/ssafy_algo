import sys
sys.stdin = open('input.txt')

# lomuto_sort
def lomuto_sort(left,right):
    pivot=A[right]
    idx=left-1

    for next in range(left,right):
        if A[next] < pivot:
            idx+=1
            A[idx], A[next] = A[next], A[idx]
    A[idx+1],A[right] =A[right], A[idx+1]
    return idx+1

def quick_sort(left,right):
    if left >= right:
        return
    pivot_idx=lomuto_sort(left,right)
    quick_sort(left,pivot_idx-1)
    quick_sort(pivot_idx+1, right)

def binary_search(n,s_list,bef_bir):
    if len(s_list)==0:
        return
    global cnt
    l=0              # 탐색구간의 시작 index
    r=len(s_list)-1  # 탐색구간의 끝 index
    m=(l+r)//2

    if n==s_list[m]: # 숫자 찾으면
        cnt+=1
    if n < s_list[m]: # 왼쪽
        bir=-1
        if bef_bir==bir: # 같은 방향으로 탐색시
            return
        binary_search(n, s_list[0:m], bir)
    elif n > s_list[m]: # 오른쪽
        bir=1
        if bef_bir==bir: # 같은 방향으로 탐색시
            return
        binary_search(n, s_list[m + 1:], bir)


T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))

    cnt=0
    quick_sort(0,len(A)-1)
    # A.sort()
    for b in B:
        binary_search(b,A,0)

    print(f'#{tc} {cnt}')