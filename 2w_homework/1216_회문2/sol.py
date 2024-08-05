import sys
sys.stdin=open('input.txt')

def find_word(arr):
    for i in range(100):
        for j in range(100,3,-1): #회문을 발견할 때 까지 실행줄여 나가면서 확인
            if j



    # max_cnt=0
    # for i in range(100):
    #     for j in range(100):
    #         n = 2  # 비교 문자 수
    #         while j_r<100:
    #             j_l = j
    #             j_r = j + n - 1
    #             for _ in range(n//2): #일치할 시
    #                 if arr[i][j_l]==arr[i][j_r]:
    #                     j_l+=1
    #                     j_r-=1
    #                 elif arr[i][j_l]!=arr[i][j_r]:   #일치 안할시
    #                     if n > max_cnt:
    #                         max_cnt = n
    #                     break
    #             n+=1
    #
    # for j in range(100):
    #     for i in range(100):
    #         n = 2  # 비교 문자 수
    #         while i_r < 100:
    #             i_l = i
    #             i_r = i + n - 1
    #             for _ in range(n//2):
    #                 if arr[i_l][j]==arr[i_r][j]:
    #                     i_l+=1
    #                     i_r-=1
    #                 elif arr[i_l][j]!=arr[i_r][j]:
    #                     if n > max_cnt:
    #                         max_cnt = n
    #                     break
    #             n+=1
    # return max_cnt

T=10
for tc in range(T):
    tc=input()
    arr=[list(input()) for _ in range(100)]
    result=find_word(arr)
    print(f'#{tc} {result}')
