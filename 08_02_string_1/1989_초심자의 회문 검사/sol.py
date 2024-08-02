import sys
sys.stdin = open('input.txt')

def pail_ex(word):
    start=0
    end=-1
    for n in range(len(word)//2): #글자 일치 확인 횟수는 글자수//2
        if word[start] == word[end]:
            start+=1
            end-=1
        else:
            return 0
    return 1


T = int(input())
for tc in range(1,T+1):
    word=input()
    result = pail_ex(word)  #회문 검사 함수 호출
    print(f'#{tc} {result}')
