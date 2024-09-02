import sys
sys.stdin = open('input.txt')




def find_winner(p):
    pass


T=int(input())
for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    p1=[]
    p2=[]
    result=0
    for i in range(len(arr)):
        if (i+1)%2: #홀수
            p1.append(arr[i])
            p1.sort()
            # if len(p1)>=3:
            #     find_winner(p1)
        else:
            p2.append(arr[i])
            p2.sort()
            # if len(p1)>=3:
            #     find_winner(p2)
        if len(p1)>=3 and len(p1)==len(p2):
            r1=find_winner(p1)
            r2=find_winner(p2)
            if r1 and not r2:
                result=1
                break
            elif r2 and not r1:
                result=2
                break
            elif r2 and r1:
                result=0
                break
    print(f'#{tc} {result}')
