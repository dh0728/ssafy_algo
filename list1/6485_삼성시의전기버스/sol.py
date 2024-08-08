import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1,T+1):
#     N=int(input())  #버스갯수
#     bus_dict={}
#     for n in range(1,N+1):  #노선 딕셔너리생성 {'1': [1, 3], '2': [2, 5]}
#         bus_dict[f'{n}']=list(map(int,input().split()))
#     P=int(input())  #버스정류장 갯수
#     p_list=[]
#     for n in range(P):  #안쓸예정
#         p_list.append(int(input()))
#     counts=[0]*(P+1)    #지나가는 노선을 카운팅하는 배열 생성
#     for li in bus_dict.values():    #li는 i번째 버스가 다니는 노선 번호 리스트
#         while li[0] <= li[1]:       #시작에서 끝까지 while문으로 카운팅
#             counts[li[0]]+=1
#             li[0]+=1
#     result=[]
#     for p in p_list:
#         result.append(counts[p])
#     print(f'#{tc}', ' '.join(map(str, result)))


# 1   //테스트 케이스 개수
# 2   //첫 번째 테스트 케이스, N=2
# 1 3 // A1 = 1, B1 = 3
# 2 5 // A2 = 2, B2 = 5
# 5   // P = 5
# 1   // 이하 C1 = 1, C2 = 2, C3 = 3, C4 = 4, C5 = 5
# 2
# 3
# 4
# 5

T = int(input())
for tc in range(1,T+1):
    N=int(input())  # N 버스노선의 수
    bus_list=[]
    counts = [0] *5001
    for n in range(1,N+1):
        A, B = (map(int, input().split())) # 버스노선 A이상 B이하
        for i in range(A,B+1):             # 다니는 버스 노선 count[i]=1
            counts[i] += 1
    P=int(input())  # 몇개의 버스가 다니는지 알고 싶은 버스정류장 갯수
    p_list=[]       # 몇개의 버스가 다니는지 알고 싶은 버스 정류장의 번호
    for n in range(P):  # 예시 p_list=[1,2,3,4,5]
        p_list.append(int(input()))
    result=[]
    for p in p_list: # 예시 p= 1 ,2 ,3 ,4 ,5
        result.append(counts[p]) # 결과리스트에 해당 리스트에 다니는 버스 수를 삽입
    print(f'#{tc}', ' '.join(map(str, result)))

