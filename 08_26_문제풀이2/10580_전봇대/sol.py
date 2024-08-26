import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,1+T):
    N  =int(input()) # 전선 개수

    ab =[list(map(int,input().split())) for _ in range(N)]

    ab.sort()
    print(ab)

    cnt =0 # 교차점 수
    for i in range(1,N):
        for j in range(i): #A는 더 낮지만 B가 더 높은 경우 교차
            if ab[j][1] > ab[i][1]:
                cnt +=1

    print(f'#{tc} {cnt}')
