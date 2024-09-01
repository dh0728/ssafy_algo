import sys
sys.stdin=open('input.txt')
'''
input
5
ABC
ABCC
NNNASBBSNV
UKABHGGHCFTCRRCTWLALX
ZYXW

output
#1 ABC 0
#2 AB 1
#3 NNNANV 2
#4 UKCFTCRRCTWLALX 3
#5 ZYXW 0
'''
def exam_word(arr):
    cnt=0
    word=[] #검사 완료한 단어 넣어 주기
    s=[]
    i=0
    while i <len(arr):
        if not s:   # 스택비어있으면 넣기
            if word: # 조건을 만족해 지웠을 때 검사완료한 알파벳의 마지막 알파벳부터 다시 검사를 해야하기 때문에
                s.append(word.pop())
            else:
                s.append(arr[i]) # 검사중인 알파벳 없고 검사완료한 알파벳도 없다면
                i+=1
        else:   # s(검사중인 단어리스트) 안비어 있으면
            if s[-1] == arr[i]: # 같은 알파벳일경우
                s.append(arr[i]) #검사리스트에 추가
                i+=1
                while i < len(arr): # 같은 알파벳일 때까지 검사
                    if s[-1] == arr[i]:
                        s.append(arr[i])
                        i+=1
                    else:
                        break
                if len(s)==2:   # 길이가 2면 최대 2연속이니 지우고 점수 추가
                    cnt+=1
                    s=[]
                else: # 3개 이상이면
                    while len(s)>1: #마지막 알바벳 빼고 word에 넣기
                        word.append(s.pop(0))
            elif ord(s[-1]) + 1 == ord(arr[i]): # 연속된 알파벳일 경우
                s.append(arr[i])
                i += 1
                while i < len(arr): # 연속된 알파벳 나열이 끝날때까지 반복
                    if ord(s[-1]) + 1 == ord(arr[i]):
                        s.append(arr[i])
                        i += 1
                    else:   # 더이상 연속아니면 break
                        break
                if len(s) == 2: # 길이가 2면 최대 2연속이니 지우고 점수 추가
                    cnt += 1
                    s = []
                else:  # 3개 이상이면
                    while len(s) > 1:  # 마지막 알바벳 빼고 word에 넣기
                        word.append(s.pop(0))
            else: # 연속, 같은 알파벳이 아닐경우
                word.append(s.pop())    # 검사 완료 알파벳리스트에 추가
                s.append(arr[i])        # 검사 알파벳리스트에 단어추가
                i+=1
    while s:
        word.append(s.pop(0))
    return word,cnt
T=int(input())
for tc in range(1,T+1):
    arr=list(input())
    w,c=exam_word(arr)
    print(f'#{tc} {"".join(map(str,w))} {c}')

