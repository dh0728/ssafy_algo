k=4
N =8
arr = [0,4,1,3,1,2,4,1]
Temp =[0]*N

counts=[0]*5    # 0~4까지의 정수

# 1단계: arr 원소별 개수 세기
for num in arr:                         # arr의 원소 x를 가져와서 counts[x]의 개수 기록
    counts[num]+=1

# 2단계: 각 숫자까지의 누적 개수 구하기
for i in range(1, k+1):                 #count[1]~count[4]까지 누적개수
    counts[i] += counts[i-1]

# 3단계 : arr의 맨 뒤부터 temp에 자리 잡기
for i in range(len(Temp)-1,-1,-1):
    counts[arr[i]] -=1                  #누적개수 1개 감수
    Temp[counts[arr[i]]]=arr[i]

print(Temp)
