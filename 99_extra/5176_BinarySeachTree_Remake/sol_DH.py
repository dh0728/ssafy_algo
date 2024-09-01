import sys
sys.stdin=open('5176_re_input.txt')

'''
input
3
90A141E28323C4650
21115191D22262C31
4060D161D2A2F3F48

output
#1 53724681
#2 49071635
#3 20553302
'''
def in_order(node):
    global i
    if node == 0:
        return
    in_order(g[node][0])
    tree[node]=dec_list[i]%10 #방문 순서에 따라 dec_list값의 10으로 나머지 나눗셈한 값을
    i+=1                      #순서대로 삽입
    in_order(g[node][1])

T=int(input())
for tc in range(1,T+1):
    code=input()
    N=int(code[0]) # self 계산용 숫자
    dec_list=[]

    # 암호문 2자리씩 10진수로 변환
    for i in range(1,len(code),2):
        dec_list.append(int(code[i:i+2],16))

    # 암호문 위치에 따라 빼기
    for i in range(len(dec_list)):
        dec_list[i]-=(i+1)*N
    # print(dec_list)

    tree_l=len(dec_list)          # 트리의 노드 개수
    tree=[None]*(len(dec_list)+1) # 완전 이진트리 초기화
    g=[0]                         # 자식노드 연결리스트
    for i in range(1,tree_l+1):   # 연결리스트 자식노드 삽입
        left=2*i                  # 왼쪽 자식노드
        right= 2*i+1              # 오른쪽 자식노드
        if left >tree_l:          # 리프노드는 0 삽입
            left=0
        if right > tree_l:        # 리프노드는 0 삽입
            right=0
        g.append([left,right])
    i=0 # dec_list의 index
    in_order(1) # 루프노드부터 중위순회시작
    tree.pop(0)
    print(f'#{tc} {"".join(map(str,tree))}')





