import sys
sys.stdin=open('input.txt')

def check_O(N, arr):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 오른쪽, 아래, 오른쪽 아래 대각선, 오른쪽 위 대각선
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for dx, dy in directions:
                    cnt = 1
                    for k in range(1, 5):  # 4칸을 더 체크
                        ni = i + dx * k
                        nj = j + dy * k
                        if ni < 0 or ni >= N or nj < 0 or nj >= N:
                            break
                        if arr[ni][nj] != 'o':
                            break
                        cnt += 1
                    if cnt == 5:
                        return "YES"
    return "NO"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]

    result = check_O(N, arr)
    print(f'#{tc} {result}')
