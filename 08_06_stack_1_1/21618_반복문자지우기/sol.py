import sys
sys.stdin =open('input.txt')

def pop_word(arr):
    s=[]
    for a in arr:
        # 비어 있거나 top과 일치하지 않는다면 그냥 삽입
        if not s or a != s[-1]:
            s.append(a)
        # 스택 리스트에 top과 겹치는 경우
        elif a == s[-1]:
            s.pop()
    return len(s)


T =int(input())
for tc in range(1,T+1):
    arr=list(input())
    result= pop_word(arr)
    print(f'#{tc} {result}')