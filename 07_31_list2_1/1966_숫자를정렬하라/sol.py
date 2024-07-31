import sys
sys.stdin = open('input.txt')

# T=int(input())
# for ts in range(1,T+1):

array =[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
#지그재그
for i in range(3):
    for j in range(4):
        array[i][j + (4-1-2*j) * (i%2)]=1
        print(array)


