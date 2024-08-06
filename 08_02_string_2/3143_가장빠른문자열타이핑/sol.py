import sys
sys.stdin = open('input.txt')

def write_count(case,word):
    res=''
    cnt=0
    for i in range(len(case)):
        if len(res)==len(case): #타이핑이 끝나면 break
            break
        if len(res)>i:  #문자열 인덱스로 입력시 i가 일치될때 까지 continue
            continue
        if case[i:i+len(word)]==word:   #문자열을 타이핑 하는 경우
            res+=word   #문자열 입력
            cnt+=1  #타이핑 횟수 +1
        else:
            res+=case[i]
            cnt+=1
    return cnt

T=int(input())
for tc in range(1,T+1):
    arr =list(input().split(' '))
    result=write_count(arr[0],arr[1])
    print(f'#{tc} {result}')