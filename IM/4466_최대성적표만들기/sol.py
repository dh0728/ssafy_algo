import sys
sys.stdin = open('input.txt')

def select_sort(li):
    for i in range(len(li)-1):
        for n in range(i,len(li)):
            if li[i]< li[n]:
                li[i],li[n] = li[n], li[i]
    return li

T = int(input())
for tc in range(1, T+1):
    N,K=map(int, input().split())
    li= list(map(int, input().split()))
    sort_li= select_sort(li)
    count=0
    for i in range(K):
        count+=sort_li[i]
    print(f'#{tc} {count}')