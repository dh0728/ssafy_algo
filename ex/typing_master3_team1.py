import sys
sys.stdin =open('input.txt', encoding='UTF8')

def team_sort():
    for i in range(N-1):
        for j in range(i+1,N):
            # 점수차 부터 비교
            if team[i][3] > team[j][3]: # 점수차가 더 작은거 앞으로
                team[i] , team[j] = team[j] ,team[i]
            elif team[i][3] == team[j][3]: # 만약 차이 같다면
                if team[i][0] < team[j][0]: # 원점수 더 높은게 앞으로
                    team[i], team[j] = team[j], team[i]
                elif team[i][0] == team[j][0]: # 점수차도 같고, 원점수도 같다면
                    if team[i][2] > team[j][2]: # 먼저 제출한거 앞으로
                        team[i], team[j] = team[j], team[i]

# 계산한 점수 조합하는 함수
def permutation_num(depth,str_n,num_list):
    global min_diff
    if depth==len(num_list): # 수정 전  if depth == 3
        diff=abs(teacher - int(str_n))
        if abs(teacher-int(str_n)) < min_diff:
            min_diff=diff
        return
    for i in range(len(num_list)): # 수정전 for i in range(3):
        if visited[i]:
            continue
        visited[i]=1
        permutation_num(depth+1,str_n+num_list[i],num_list)
        visited[i]=0

# 팀별 점수 계산 함수
def cal_score(s1,s2,team_num):
    # 개인별 점수 우선 계산
    s1_score = int(s1[0]) * int(s1[1]) * 0.01
    s2_score = int(s2[0]) * int(s2[1]) * 0.01

    # 한글일 경우 0.7 곱해주기
    if s1[2]=='K':
        s1_score *=0.7
    if s2[2]=='K':
        s2_score *=0.7

    # 소수점 버리기
    s1_score = int(s1_score)
    s2_score = int(s2_score)

    # 평균 계산
    aver= (s1_score+s2_score)//2

    # 강사님과 점수 비교
    team.append([aver, f'{s1[3]} {s2[3]}',team_num])


N=int(input()) # 팀 수
S, P = input().split() # S 강사님 점수, P 강사님 정확도

# 강사님 결과 부터 구하기
num_len=len(S)
teacher=int(int(S)*int(P)*0.01)
team=[]

for i in range(N):
    s1=list(input().split()) # 504 100 E 김조장
    s2=list(input().split())
    cal_score(s1,s2,i+1)

for i in range(N): # 순회하면서 점수차 가장 작은 값 찾아서 리스트에 넣기
    min_diff=10000000000
    num_list=list(str(team[i][0]))
    if len(num_list) < num_len: # 강사님 타자 속도보다 자리수가 작으면
        while len(num_list) < num_len: # 자릿수 만큼 0 채워주기
            num_list.insert(0,'0')

    visited = [0] * len(num_list) # 0으로 채워준 만큼 visited 리스트 생성
    permutation_num(0,'',num_list)
    team[i].append(min_diff)

# 정렬 함수 호출
# 최종적으로 team 리스트에는 아래와 같은 팀별 리스트가 들어있음
# [원점수, 팀원, 팀번호, 최소 점수차]=[643, '주조장 사팀원', 8, 0]
team_sort()

for i in range(N):
    print(f'{i+1}등 : {team[i][1]} ({team[i][2]} 팀)| 점수 차 : {team[i][3]} | 원점수 : {team[i][0]}')