import sys
sys.stdin = open('input.txt')


# Hoare Partiton 방식으로 정렬
def hoare_partiton(left,right):
    pivot= A[left] # pivot은 제일 왼쪽
    left +=1

    while True:
        # 왼쪽
        while left <= right and A[left]< pivot: # left idx가 right idx 보다 이하
            left +=1                            # left 값이 pivot 보다 작으면 이동
        # 오른쪽
        while right >= left and A[right] > pivot: # right idx가 left idx 보다 이상
            right -=1                             # right 값이 pivot 보다 크면 이동

        # 엇갈리면 right index 반환
        if left >=right:
            return right

        A[left], A[right] = A[right], A[left] # 엇갈리기 전까지는 값 교환


def quick_sort(left,right):
    if left >=right: # 더이상 조사 대상이 없다면
        return

    pivot_idx = hoare_partiton(left,right)

    A[left], A[pivot_idx] = A[pivot_idx], A[left]

    quick_sort(left,pivot_idx-1)
    quick_sort(pivot_idx+1,right)

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
    print(A)
    for b in B:
        binary_search(b,A,0)

    print(f'#{tc} {cnt}')

