import sys
sys.stdin = open('input.txt')

# pivot이 맨왼쪽일때
# 역순정렬되어있을때가 최악 N**2

# 피벗: 제일 왼쪽 요소

# Lomuto partition : swap이 많아서 좀 더 느리다
# 무조건 오른쪽을 pivot
# 같은 수가 많을 때 문제가 많이 생긴다.

# 퀵정렬 시간복잡도 = > 평균적으로 매우 빠라다 -> O(N log n)

# 이진 검색(Binary Search)
# 무조건 정렬된 상태여야 한다.


def quick_sort(div_arr):
    if len(div_arr) <= 1:
        return div_arr
    else:
        pivot = div_arr[0] # 왼쪽을 피봇으로 잡음
        left, right= [],[]
        for i in range(1, len(div_arr)):
            if div_arr[i] < pivot:
                left.append(div_arr[i])
            else:
                right.append(div_arr[i])
        return [*quick_sort(left),pivot,*quick_sort(right)]


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr = list(map(int,input().split()))
    # result=quick_sort(arr)
    # print(f'#{tc} {result[N//2]}')
    print(f'#{tc} {sorted(arr)[N//2]}')