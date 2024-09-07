N=int(input())
n=6
start=1
cnt=1
while True:
    if start>=N:
        print(cnt)
        break
    start+=n
    n+=6
    cnt+=1