import sys
sys.stdin = open('input.txt')

# A,B=map(int,input().split())
# if (A-B)%3==1:
#     print('A')
# else:
#     print('B')

# def ro_pa_scis(arr,st):
#     global win
#     l=len(arr)
#     arr2 = []  # 이긴 사람의 카드가 들어가는 리스트
#     st2 = []  # 이긴 사람의 번호가 들어가는 인덱스
#     if l>=3:    # 사람 수가 3명 이상
#         for i in range(0,l//2,2):   #앞 그룹
#             if i+1 == l//2:   # 가위바위보 할 사람이 없을 경우
#                 arr2.append(arr[i])
#                 st2.append(st[i])
#             elif arr[i]-arr[i+1]==0:  #비기는 경우 번호가 낮은 사람이 들어감
#                 arr2.append(arr[i])
#                 st2.append(st[i])
#             elif (arr[i] - arr[i + 1]) % 3 == 1:  # 앞사람이 이기는 경우
#                 arr2.append(arr[i])
#                 st2.append(st[i])
#             else:                                 # 뒷사람이 이기는 경우
#                 arr2.append(arr[i+1])
#                 st2.append(st[i+1])
#         for i in range(l//2,l,2):   # 두번째 그룹
#             if i+1 == l:   # 가위바위보 할 사람이 없을 경우
#                 arr2.append(arr[i])
#                 st2.append(st[i])
#             elif arr[i]-arr[i+1]==0:  #비기는 경우 번호가 낮은 사람이 들어감
#                 arr2.append(arr[i])
#                 st2.append(st[i])
#             elif (arr[i] - arr[i + 1]) % 3 == 1:  # 앞사람이 이기는 경우
#                 arr2.append(arr[i])
#                 st2.append(st[i])
#             else:                               # 뒷사람이 이기는 경우
#                 arr2.append(arr[i+1])
#                 st2.append(st[i+1])
#         ro_pa_scis(arr2,st2)
#     if l==2:
#         if arr[0]-arr[1] == 0:  # 비기는 경우 번호가 낮은 사람이 들어감
#             win=st[0]+1         # 비기는 경우 먼저 뒤에 가면 틀림
#             return
#         elif (arr[0]-arr[1])%3 == 1:
#             win=st[0]+1
#             return
#         win=st[1]+1
#         return
#
# T= int(input())
# for tc in range(1,T+1):
#     win= 0
#     N = int(input())
#     arr= list(map(int, input().split()))
#     st= [n for n in range(N)]
#     ro_pa_scis(arr, st)
#     print(f'#{tc} {win}')
#     # 가위 1, 바위 2, 보 3

def ro_pa_scis2(arr,st):    # 가위바위보 하는 함수
    l = len(arr)    # 가위바위보 할 사람 수
    arr_win=[]  # 승자 카드가 들어가는 리스트
    st_win=[]   # 승자 번호가 들어가는 리스트
    if l==1:
        return [arr[0],st[0]]
    for i in range(0,l,2):
        if i+1 == l:   # 가위바위보 할 사람이 없을 경우
            arr_win.append(arr[i])
            st_win.append(st[i])
        elif arr[i]-arr[i+1]==0:  #비기는 경우 번호가 낮은 사람이 들어감
            arr_win.append(arr[i])
            st_win.append(st[i])
        elif (arr[i] - arr[i + 1]) % 3 == 1:  # 앞사람이 이기는 경우
            arr_win.append(arr[i])
            st_win.append(st[i])
        else:                                 # 뒷사람이 이기는 경우
            arr_win.append(arr[i+1])
            st_win.append(st[i+1])
    return ro_pa_scis2(arr_win,st_win)        # 승자끼리 다시 가위바위보

def group(arr,st):  # 그룹 나누는 함수
    win1=ro_pa_scis2(arr[:N//2], st[:N//2])  # 그룹 나누기
    win2=ro_pa_scis2(arr[N//2:], st[N//2:])
    result = win1[0]-win2[0]                 # 나눈 그룹 승자들 뽑아서 다시 가위바위보
    if result == 0:  # 비기는 경우 번호가 낮은 사람이 들어감
        return win1[1]+1
    elif result % 3 == 1:  # 앞사람이 이기는 경우
        return win1[1]+1
    return win2[1]+1

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr= list(map(int, input().split()))
    st= [n for n in range(N)]
    result=group(arr,st)
    print(f'#{tc} {result}')
    # 가위 1, 바위 2, 보 3


