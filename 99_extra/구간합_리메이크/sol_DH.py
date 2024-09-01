import sys
sys.stdin=open('input.txt')

'''
#1 2
#2 13
#3 95
#4 22639
#5 34630
#6 -1
'''

def trans_arr(N):
    max_arr=0
    for i in range(N): # 가장 긴 배열 길이 뽑기
        if len(arr[i]) > max_arr:
            max_arr=len(arr[i])

    trans_arr_list=[]
    for j in range(max_arr):  # col을 중심으로 이중 반복
        new_arr=[]
        for i in range(N):
            if j<len(arr[i]):               # arr[i]가 index가 j를 가지고 있으면
                new_arr.append(arr[i][j])   # 배열리스트 추가
        trans_arr_list.append(new_arr)      # 변환한 배열 리스트에 삽입
    return trans_arr_list

def find_sum(M,arr_li):
    global max_sum
    global min_sum
    for j in range(len(arr_li)-M+1): # 총 구간합을 구하는 횟수는 = arr의 길이 - 이웃한 수 +1
        curr_sum=0                   # 구간합 초기화
        for x in range(M):           # 이웃한 M개 합 만큼 더하기
            curr_sum+=arr_li[j+x]
        if min_sum > curr_sum:       # min_sum보다 작으면 교체
            min_sum = curr_sum
        if max_sum < curr_sum:       # max_sum보다 크면 교체
            max_sum = curr_sum
    return


T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split()) # N 열의 길이 M 이웃한 수 갯수

    arr=[list(map(int,input().split())) for _ in range(N)]

    # 각 배열마다 같은 index를 가진 값끼리 모아 리스트 만들기
    trans_arr_list=trans_arr(N)
    # print(trans_arr_list)
    max_sum=0
    min_sum=1000*10
    for a in trans_arr_list:
        if len(a) < M:  # 구간합을 구할 수 없는 arr이면 패스
            continue
        find_sum(M,a)

    if min_sum - max_sum == 10000:  # min,max값이 변화가 없으면 구간이 없는 것
        print(f'{tc} {-1}')
    else:
        print(f'#{tc} {max_sum-min_sum}')




