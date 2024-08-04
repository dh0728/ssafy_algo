import sys
sys.stdin= open('input.txt')

# 정답1
# def snail_sort(N):
#     dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
#     dy = [1, 0, -1, 0]
#     arr = [[0] * N for _ in range(N)]
#     i = 0  # 초기 row
#     j = 0  # 초기 col
#     dir = 0  # 방향에 따른 dxy값 dxy[dir]
#
#     for n in range(1, N * N + 1):
#         arr[i][j] = n
#         ni = i + dx[dir]  # i 방향 백터 +
#         nj = j + dy[dir]  # j 방향 백터 +
#
#         # 범위를 벗어나거나 이미 숫자가 채워진 경우 방향 전환
#         if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
#             i, j = ni, nj
#         else:
#             dir = (dir + 1) % 4
#             i = i + dx[dir]
#             j = j + dy[dir]
#
#     return arr


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     result = snail_sort(N)
#     print(f'#{tc}')
#     for li in result:
#         print(' '.join(map(str, li)))

# 런타임 에러1
# def snail_sort(N):
#     dxy= [[0,1],[1,0],[0,-1],[-1,0]] #오른쪽,아래,왼,위
#     i=0 #초기 row
#     j=0 #초기 col
#     dir=0   #방향에 따른 dxy값 dxy[dir]
#     arr=[[0]*N for _ in range(N)]
#     for n in range(1, N*N+1):
#         arr[i][j]=n
#         ni=i+dxy[dir][0]  # i 방향 백터 +
#         nj=j+dxy[dir][1]  # j 방향 백터 +
#         if 0 <= i < N and 0 <= j < N and arr[ni][nj] == 0:
#             i= ni
#             j= nj
#         else:
#             dir = (dir + 1) % 4
#             i= i+dxy[dir][0]
#             j= j+dxy[dir][1]
#     return arr
#
# T=int(input())
# for tc in range(1,T+1):
#     N=int(input())
#     result=snail_sort(N)
#     print(f'#{tc}')
#     for li in result:
#         print(' '.join(map(str,li)))

# 런타임에러2
# def snail_sort(N):
#     dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 오른쪽,아래,왼,위
#     i = 0  # 초기 row
#     j = 0  # 초기 col
#     dir = 0  # 방향에 따른 dxy값 dxy[dir]
#     arr = [[0] * N for _ in range(N)]
#     for n in range(1, N ** 2 + 1):
#         arr[i][j] = n
#         i += dxy[dir][0]  # i 방향 백터 +
#         j += dxy[dir][1]  # j 방향 백터 +
#         if i < 0 or i > N - 1 or j < 0 or j > N - 1:  # 범위 벗어나는지 체크
#             continue
#         if arr[i][j] != 0:
#             dir = (dir + 1) % 4  # 오아왼위로 순서대로 방향전환되면서 숫자 채워짐
#     return arr
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     reuslt = snail_sort(N)
#     print(f'#{tc}')
#     for li in reuslt:
#         print(*li)