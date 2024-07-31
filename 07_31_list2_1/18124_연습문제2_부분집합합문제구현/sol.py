import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    result=0
    n = len(arr)
    set_list=[] #부분집합이 담기는 리스트
    for i in range(1<<n):  #2**n
        li=[] #부분집합하나가 들어가는 리스트
        for j in range(n):
            if i & (1<<j):  #2진법으로 변환해 비교해 공통적인 부분만 참
                li.append(arr[j])   #해당 index에 값만 부분집합리스트에 추가
        set_list.append(li)
    for set_li in set_list:
        sum_set = 0
        if len(set_li) >0:  #처음에 빈배열이 들어가서 빈배열은 예외처리
            for v in set_li:
                sum_set += v
            if sum_set ==0: #부분집합이 합이되는 순간 result=1후 break
                result=1
                break
    print(f'#{tc} {result}')

