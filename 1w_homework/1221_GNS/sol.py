#8-bit => 1Bytes : 주소가 부여되는 최소단위

import sys
sys.stdin =open('input.txt')

def counting_sort(lens, max_num, arr):
    sort_arr=[0]*lens
    num_dict={'ZRO':[0,'ZRO'] ,'ONE':[1,'ONE'], 'TWO':[2,'TWO'], 'THR':[3,'THR'],
              'FOR':[4,'FOR'] ,'FIV':[5,'FIV'],'SIX':[6,'SIX'], 'SVN':[7,'SVN'], 'EGT':[8,'EGT'], 'NIN':[9,'NIN']}
    counts=[0]*(max_num+1)
    for num in arr: #숫자 갯수 카운팅
        counts[num_dict[num][0]]+=1
    for i in range(1,max_num+1): #갯수 누적시키기
        counts[i]+=counts[i-1]
    for i in range(lens-1,-1,-1):   #arr의 마지막 행 부터 차례로 배치
        counts[num_dict[arr[i]][0]]-=1  #누적 개수 1개씩 줄이기
        sort_arr[counts[ num_dict[ arr[i] ][0]] ] =num_dict[arr[i]][1] #해당 위치에 값들 넣어주기
    return sort_arr

T = int(input())
for tc in range(1,T+1):
    test_len=input()
    lens=int(test_len[3:])
    arr=list(input().split())
    result=counting_sort(lens, 9, arr) #배열길이, 최고 숫자, arr
    print(f'#{tc}')
    print(*result)

