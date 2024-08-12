import math
def find_angle(myball,target):
    x=abs(hole4[0]-myball[0])
    y=abs(hole4[1]-myball[1])

    ga=math.atan2(y,x)   #가
    print(f'x: {x}')
    print(f'y: {y}')
    print(f'가 라디안{ga}')
    print(f'가 degree {math.degrees(ga)}')

    # 공과 홀 사이의 거리 구하기(a, b, c)
    # 공식 -> 거리= 루트( (x1-x2)^2 + (y1-y2)^2 )
    my_dis=math.sqrt((hole4[0]-myball[0])**2+(hole4[1]-myball[1])**2)  # 내공과 홀 사이의 거리 a
    tar_dis = math.sqrt((hole4[0] - target[0]) ** 2 + (hole4[1] - target[1]) ** 2)  # 목적구 와 홀 사이의 거리 b
    my_tar_dis = math.sqrt((myball[0] - target[0]) ** 2 + (myball[1] - target[1]) ** 2)  # 내공과 목적구 사이의 거리 c
    print(f'내공과 홀 사이 거리 :{my_dis}')
    print(f'목적구와 홀 사이 거리 :{tar_dis}')
    print(f'내공과 목적구 사이거리 :{my_tar_dis}')

    # 다 구하기 제2 코사인 법칙 응용
    da=math.acos( (my_dis**2+tar_dis**2-my_tar_dis**2) / (2*my_dis*tar_dis) ) #다
    # d 구하기 제 2 코사인 법칙
    print(f'다 : {math.degrees(da)}')
    d= math.sqrt((my_dis**2+(tar_dis+r2)**2)-2*my_dis*(tar_dis+r2))
    print(f'd : {d}')
    # 나 구하기 제2 코사인 법칙 이용
    na_angle=(my_dis**2+d**2-(tar_dis+r2)**2)/(2*my_dis*d)
    print(f'나각 : {na_angle}')
    if na_angle >1:
        na_angle=1
    elif na_angle <-1:
        na_angle=-1
    na=math.acos(na_angle)
    print(f'나 : {math.degrees(na)}')
    angle=ga+na
    result=math.degrees(angle)
    return result

r2=5.78
    #공의 직경 5.78
hole1=[0,0]
hole2=[127,0]
hole3=[254,0]
hole4=[0,127]
hole5=[127,127]
hole6=[254,127]

myball=[127, 63.5]
target=[80,90]
reuslt= find_angle(myball, target)
print(f'각도:{reuslt}')



