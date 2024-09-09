import sys
sys.stdin=open('input.txt')

def permutaion():
    pass

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    # 각 연산자의 개수 '+' 2 개, '-' 1 개, '*' 0 개, '/' 1 개
    oper_list=list(map(int,input().split()))
    num_list=list(map(int,input().split()))
