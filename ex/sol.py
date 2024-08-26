import sys
sys.stdin=open('input.txt')

N, M = map(int,input().split()) # N 바구니 개수, M 공을 넣는 횟수
arr=[list(map(int,input().split())) for _ in range(M)]

basket=[0]*(N+1)
for li in arr:
    for i in range(li[0],li[1]+1): # 바구니의 범위 만큼 공 넣기
        basket[i]=li[2]

for i in range(1,N+1):
    print(basket[i], end=' ')
print()



