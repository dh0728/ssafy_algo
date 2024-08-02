import sys
sys.stdin= open('input.txt')

N = int(input())
arr = [n for n in range(1,N+1)]
for i, n in enumerate(arr):
    if n < 10:
        if n%3==0:
            arr[i]='-'
    else:
        ch=''
        for w in str(n):
            if int(w)!=0 and int(w)%3==0:
                ch+='-'
        if len(ch)>0:
            arr[i]=ch

print(' '.join(map(str,arr)))
