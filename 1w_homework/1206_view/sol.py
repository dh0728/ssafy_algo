for test_case in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))
    result=0
    for i in range(2,N-2):
        l_view_p1 = arr[i]-arr[i-1]
        l_view_p2 = arr[i]-arr[i-2]
        r_view_p1 = arr[i]-arr[i+1]
        r_view_p2 = arr[i]-arr[i+2]
        if l_view_p1 > 0 and l_view_p2 > 0 and r_view_p1 > 0 and r_view_p2 > 0:
            if l_view_p1 < l_view_p2:
                min_left_v = l_view_p1
            else:
                min_left_v = l_view_p2

            if r_view_p1 < r_view_p2:
                min_right_v = r_view_p1
            else:
                min_right_v = r_view_p2

            if min_left_v >= min_right_v:
                result += min_right_v
            else:
                result += min_left_v
    print(f'#{test_case} {result}')

