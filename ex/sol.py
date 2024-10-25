import sys
sys.stdin=open('input.txt')
#input = sys.stdin.readline

# 부르는 수 체크
def check_x(number):
    for i in range(5):
        for j in range(5):
            if maps[i][j]==number:
                maps[i][j]=0
                return
    return

def bingo():
    bingo_cnt=0
    for i in range(5):
        sum_num=0
        for j in range(5):
            sum_num +=maps[i][j]
        if sum_num ==0:
            bingo_cnt+=1

    for j in range(5):
        sum_num=0
        for i in range(5):
            sum_num +=maps[i][j]
        if sum_num ==0:
            bingo_cnt+=1

    sum_num1=0
    sum_num2=0
    i=0
    j=4
    for x in range(5):
        sum_num2+=maps[i][j]
        sum_num1+=maps[x][x]
        i+=1
        j-=1

    if sum_num1 == 0:
        bingo_cnt += 1
    if sum_num2 == 0:
        bingo_cnt += 1

    return bingo_cnt


maps= [list(map(int,input().split())) for _ in range(5)]
numbers=  [list(map(int,input().split())) for _ in range(5)]

cnt=0
cnt_bingo=0
for i in range(5):
    if cnt_bingo >=3:
        break
    for j in range(5):
        if cnt_bingo >= 3:
            break
        check_x(numbers[i][j])
        cnt+=1
        if cnt >=12:
            cnt_bingo=bingo()

print(cnt)