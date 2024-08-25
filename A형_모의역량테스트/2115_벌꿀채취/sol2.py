import itertools
import sys
sys.stdin=open('input.txt')

'''
벌통의 개수만큼 선택을 하고, 그 안에서 부분집합을 구한뒤에 부분집합 중에서 최대 수익을 찾아내고
그 수익의 합을 구하자
'''

def cal_square_sum(num_list):
    # 각 값을 제곱해서 더한 값을 반환
    # 이조합이 최대 용량 C를 넘으면 안된다
    if sum(num_list) > C:
        return 0
    return sum(num **2 for num in num_list)

def cal_max_honey(honey_list):
    max_honey=0
    # 부분 집합을 구하는 코드
    # 주어진 리스트(fst_select_honey_list)에서 1개,2개 ..., 전부다 선택한 조합
    for select_cnt in range(1, M + 1):
        # 부분 집합의 조합을 구한다.
        comb = itertools.combinations(honey_list, select_cnt)
        # 각각의 부분집합들의 이익을 구한다.
        # comb의 각 인자를 제공해서 더한 값을 반환하는 함수를 만들어서 map으로 각자 적용
        comb_list = list(map(cal_square_sum, comb))
        # 여태까지 조합중에 가장 이익이 높은 것들로 계속 갱신이 됨
        max_honey = max(max_honey, max(comb_list))
    return max_honey


T=int(input())
for tc in range(1,T+1):
    # N = 벌통의 크기, M = 벌통의 개수, C : 꿀을 채취할 수 있는 최대 양
    N, M, C = list(map(int, input().split()))
    honey_matrix=[list(map(int, input().split())) for _ in range(N)]
    max_sum = 0 # 총 수익을 저장할 변수

    # 일꾼 1이 전체적으로 순회를 돈다
    # 대신 벌통의 개수(M)직전까지만 순회를 해야한다.
    for fst_i in range(N):
        for fst_j in range(N-M+1):
            # 일꾼 1이 선택한 인덱스
            fst_select_honey_list = honey_matrix[fst_i][fst_j:fst_j+M]

            # 위에서 선택한 꿀 목록에서 부분집합을 구하고 이 부분 집합 중에서 최대 이익을 구한다.
            fst_select_honey_max=cal_max_honey(fst_select_honey_list)

            for snd_i in range(fst_i,N):
                for snd_j in range(0, N-M+1):
                    # 첫번째 일꾼과 두번째 일꾼이 같은 행을 골랐을 때
                    # 두번 째 일꾼이 첫번째 일꾼보다 앞을 선택한 경우 스킵
                    if fst_i == snd_i and snd_j < fst_j+M:
                        continue
                    snd_select_honey_list = honey_matrix[snd_i][snd_j:snd_j + M]
                    snd_select_honey_max = cal_max_honey(snd_select_honey_list)
                    max_sum = max(max_sum, fst_select_honey_max+snd_select_honey_max)
    print(f'#{tc} {max_sum}')