import sys
sys.stdin = open('input.txt','r',encoding='UTF-8')

def search_pat(word,case):
    count =0
    for i in range(len(case)-len(word)+1):
        if case[i:len(word)+i]==word: #비교할 부분만 슬라이싱해서 비교
            count+=1
    return count

for tc in range(1,11):
    T=input()
    word=input()
    case=input()
    result=search_pat(word,case)
    print(f'#{tc} {result}')
