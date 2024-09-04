import sys
sys.stdin=open('input.txt')

arr=list(map(int,input().split()))

sum_n=0
for a in arr:
    sum_n+=a*a
print(sum_n%10)