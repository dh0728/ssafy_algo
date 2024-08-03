import sys
sys.stdin=open('input.txt')

def count_m(N):
    money=[50000,10000,5000,1000,500,100,50,10]
    count=[]
    for m in money:
        count.append(N//m)
        N%=m
    return count



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result=count_m(N)
    print(f'#{tc}')
    print(' '.join(map(str,result)))