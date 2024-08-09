def construct_candidate(a,k,n,c):
    in_perm =[False]*(NMAX+1)   #사용했는지 체크하는 배열

    for i in range(k):
        in_perm[a[i]]=True  #선택된 원소들만 True로 표시

    ncandidates =0
    for i in range(1,NMAX+1):
        if in_perm[i]==False:
            c[ncandidates]=i # 후보 원소가 들어가는 배열에 원소들 넣기
            ncandidates +=1  # 선택안된 후보 수만큼 후보 갯수 카운팅
    return ncandidates  #후보의 갯수

def backtrack(a,k,n):   # a 주어진 배열, k 결정할 원소 n 원소의 개수
    c = [0]*MAX_CAN     # 순열이 들어갈수 있는 숫자 후보들 넣는 리스트 a=[1]이면 c=[2,3]
    if k == n:          # 최종적으로 순열 만들어지면 print
        for i in range(0,k):
            print(a[i],end=' ')
        print()
    else:
        ncandidates = construct_candidate(a,k,n,c)  # 후보들 갯수
        for i in range(ncandidates):    # 후보들 갯수만큼 반복
            a[k]=c[i]                   # a=[1,0,0] a=[2,0,0] a=[3,0,0]
            backtrack(a, k+1,n)         # 하나씩 다른 원소를 넣고 재귀함수 호출

MAX_CAN=3
NMAX=3
a=[0]*NMAX
backtrack(a,0,3)