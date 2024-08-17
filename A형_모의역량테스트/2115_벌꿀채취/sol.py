import sys
sys.stdin=open('input.txt')


def subset(depth,h_li,sum_c, v): # 꿀 선택 깊이, 꿀통배열, 선택한 꿀의 합
    if sum_c > C: #채취할 수 있는 최대양 넘어가면 return
        return
    if depth == len(h_li) and sum_c <=C: # 현재 부분집합에서 채취 끝나면
        res.append(v)
        return
    subset(depth+1,h_li,sum_c+h_li[depth],v+h_li[depth]**2)
    subset(depth+1,h_li,sum_c,v)
def cal_profit(arr1,arr2): #
    # if tc==3:
        # print(arr1,arr2)
    global max_profit
    global res
    subset(0,arr1,0,0)
    max_h1=max(res)
    res=[]
    subset(0,arr2,0,0)
    max_h2=max(res)
    res=[]
    if max_h1+max_h2 > max_profit:
        max_profit=max_h1+max_h2

def find2(row,col): # 첫번째 사람의 행, 마지막으로 선택한 벌꿀통 열
    arr2=[]
    if (N-1)-col >=M: # 2번 벌꿀통이 1번과 같은 열에 존재할 수 있으면
        for i in range(1,M+1):
            arr2.append(honey[row][col+i])  # 2번 사람 벌꿀 삽입
        cal_profit(arr1,arr2)
    else:   # 같은 줄에 존재 못하면 다음 줄로
        for i in range(row+1,N):
            for j in range(N - M + 1):  # 1행에서 꿀을 채취할 수 있는 경우 = 행길일 - 벌통개수 +1
                arr2= []
                for x in range(M):
                    arr2.append(honey[i][j+x])
                cal_profit(arr1,arr2)

T=int(input())
for tc in range(1,T+1):
    N, M, C = map(int,input().split())
    honey=[list(map(int,input().split())) for _ in range(N)]
    max_profit=0
    res=[]

    #첫번째 사람의 벌꿀통 먼저 선택
    for i in range(N-1): #첫번 째 사람은 마지막줄의 꿀통 채취할 필요 없음
        for j in range(N-M+1): # 1행에서 꿀을 채취할 수 있는 경우 = 행길일 - 벌통개수 +1
            arr1=[]
            for x in range(M):
                arr1.append(honey[i][j+x])
                find2(i,j+M-1)  # 두번째 사람 벌꿀 선택 함수 호출
    print(f'#{tc} {max_profit}')