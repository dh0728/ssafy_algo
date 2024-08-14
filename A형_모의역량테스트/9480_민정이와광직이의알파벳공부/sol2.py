import sys
sys.stdin=open('input.txt')

def dfs(depth, alpa_set):   # depth :단어 set에서 선택여부를 결정하는 단어의 index
    global cnt              # alpa_set : 선택한 단어 집합
    if depth ==N:
        if len(alpa_set)==26: # 알파벳이 26개가 다들어가면 단어세트완성
            cnt +=1           # 단어세트 개수 1증가
        return            # 재귀종료

    # depth 에 해당하는 단어를 선택한 경우
    dfs(depth+1, alpa_set | word_sets[depth]) # | => 파이썬에서 합집합으로 사용
    # depth 에 해당하는 단어를 선택안한 경우
    dfs(depth+1, alpa_set)

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    words = [input().strip() for _ in range(N)] # 단어 리스트로 받기
    word_sets = [set(word) for word in words] # set으로 단어별 알파벳 중복제거
    # print(words)
    # print(word_sets)

    cnt=0
    dfs(0, set())
    print(f'#{tc} {cnt}')
