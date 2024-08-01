import sys
sys.stdin = open('input.txt')

def binary_search(P,page): #이진탐색 함수
    start=1
    end=P
    count=0
    while start <= end:
        mid= (start+end)//2
        if mid==page:
            count +=1
            return count
        elif mid > page:
            end =mid
            count +=1
        else:
            start=mid
            count +=1
    return False


T=int(input())
for tc in range(1,T+1):
    P, A, B = map(int, input().split())
    A_cnt=binary_search(P,A)
    B_cnt=binary_search(P,B)
    if A_cnt > B_cnt:   #A가 오래 걸릴 경우
        print(f'#{tc} B')
    elif B_cnt > A_cnt: #B가 오래 걸릴 경우
        print(f'#{tc} A')
    else:               #비길경우
        print(f'#{tc} 0')
