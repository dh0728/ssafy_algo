import sys
sys.stdin=open('input.txt')

def pascal(N):
    arr = []
    dx = [0, -1] #해당 지점에 더해지는 전 row의 col 방향백터
                 #예시 arr[3][2]에 더해지는 값은 arr[2][2]+arr[2][1]
    for i in range(1, N + 1):   # [0]이 들어가 있는 삼각형 생성
        arr.append([0] * i)

    for i in range(N):  # row
        for j in range(i + 1): #col
            if i == 0:  # 첫행은 그냥 1넣기
                arr[i][j] = 1
                continue
            for x in dx: #방향벡터 만큼 j값 +
                nx = j + x
                if 0 <= nx < len(arr[i - 1]) and i - 1 >= 0: #범위 포함하는 부분만 더하기
                    arr[i][j] += arr[i - 1][nx]
    return arr

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    result=pascal(N)  #파스칼 삼가형 생성함수 호출
    print(f'#{tc}')
    for li in result:
        print(' '.join(map(str,li)))

