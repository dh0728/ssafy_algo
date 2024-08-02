import sys
sys.stdin = open('input.txt')

def mirror():
    mir_word=[0]*len(arr)
    for i in range(len(arr)):
        if arr[i]=='b':
            mir_word[-i-1]='d'
        elif arr[i]=='d':
            mir_word[-i-1]='b'
        elif arr[i]=='p':
            mir_word[-i-1]='q'
        else:
            mir_word[-i-1]='p'
    return mir_word

T=int(input())
for tc in range(1,T+1):
    arr=list(input())
    result=mirror()
    print(f'#{tc} {"".join(result)}')