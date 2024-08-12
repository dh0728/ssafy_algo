import sys
sys.stdin = open('input.txt')

def find_binary(word,words):
    if len(word)==N:
        return word
    for i in range(len(words)):
        if len(word)==0:    #공백이면 시작문자 넣어주기
            if words[i]>0:  #사용가능한 문자열인 경우
                words[i]-=1
                result = find_binary(word+bi_list[i],words)
                if result:
                    return result
                words[i]+=1  #다른 경우를 위해 다시 +1
        elif words[i]>0:     #이진 단어가 들어가야 할때
            if word[-1]== bi_list[i][0]: #현재 word의 마지막 숫자와 이어질 경우
                words[i] -= 1
                result=find_binary(word+bi_list[i][1],words)
                if result:
                    return result
                words[i] += 1   #다른 경우를 위해 다시 +1
    return None

T=int(input())
for tc in range(1, T+1):
    words = list(map(int,input().strip().split()))
    # 00 01 10 11
    # words = list(map(int,input().split()))
    N=1
    for n in words:
        N+=n
    bi_list = {0: '00' , 1: '01' , 2: '10' , 3: '11'}
    result=find_binary('', words)
    if result:
        print(f'{tc} {result}')
    else:
        print(f'{tc} impossible')
