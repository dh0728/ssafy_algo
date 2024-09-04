import sys
sys.stdin = open('input.txt')


arr=bytearray(300*1024*1024)


def quick_sort(div_arr):
    if len(div_arr) <= 1:
        return div_arr
    else:
        pivot = div_arr[0]
        left, equal, right = [], [], []
        for i in range(len(div_arr)):
            if div_arr[i] < pivot:
                left.append(div_arr[i])
            elif div_arr[i] == pivot:
                equal.append(div_arr[i])
            else:
                right.append(div_arr[i])
        return [*quick_sort(left), *equal, *quick_sort(right)]

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
    result=quick_sort(A)
    # A.sort()
    for b in B:
        binary_search(b,result,0)

    print(f'#{tc} {cnt}')
