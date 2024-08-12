import sys
sys.stdin = open('input.txt')

def find_binary(word,words):
    if len(word)==N:
        return word
    for i in range(len(words)):
        if len(word)==0:    #공백이면 시작문자 넣어주기
            if words[i]>0:
                words[i]-=1
                result = find_binary(word+bi_list[i],words)
                if result:
                    return result
                words[i]+=1
        elif words[i]>0:   #이진 단어가 들어가야 할때
            if word[-1]== bi_list[i][0]:
                words[i] -= 1
                result=find_binary(word+bi_list[i],words)
                if result:
                    return result
                words[i] += 1
    return None

        # 길이 N인 어떤 이진 문자열을 가짐
T=int(input())
for tc in range(1, T+1):
    # words = [input().strip() for _ in range(N)]
    words = list(map(int,input().split()))
    N=1
    for n in words:
        N+=n
    bi_list = {0: '00' , 1: '01' , 2: '10' , 3: '11'}
    result=find_binary('', words)
    if result:
        print(f'{tc} {result}')
    else:
        print(f'{tc} impossible')
    # 00 01 10 11
    # 순열로 모든 경우를 나열 해야 하나?
    # 어떻게 나열할까
    # 문자열을 반복문이나 재귀로 하나씩 추가
    # 추가할 때 현재 문자에서 1글자로 추가시 들어갈 수 있는 문자열만 추가되게하고 없을 시 종료
