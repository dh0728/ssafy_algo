T = int(input())

for test_case in range(1, T+1):
    N =int(input())
    a = input()
    new_dict={}
    for num in a:
        state = new_dict.get(num,-1)
        if state==-1:
            new_dict[num]=1
        else:
            new_dict[num]= state +1

    count =0
    for k,v in new_dict.items():
        if v > count:
            count =v
            num = k
        elif v == count:
            if int(k) > int(num):
                num=k
    print(f'#{test_case} {num} {count}')