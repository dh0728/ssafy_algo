import sys
sys.stdin=open('input.txt')

T=10
for tc in range(1,T+1):
    N,S=map(int,input().split())
    arr=list(map(int,input().split()))
    node=[[]*101]

