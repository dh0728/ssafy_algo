import sys
sys.stdin = open('input.txt')

T = int(input())
def selectionSort(arr, n):  #선택정렬
    for i in range(n-1):
        min_i=i
        for j in range(i+1,N):
            if arr[min_i]>arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = selectionSort(arr,N)
    print(f'#{tc} {" ".join(map(str,result))}')