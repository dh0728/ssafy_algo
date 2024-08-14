import sys
sys.stdin = open('input.txt')

def change_state(B,N,stu_list): #버튼 수, 학생수, 학생리스트
    for s in stu_list:
        if s[0] ==1:    # 남자
            for i in range(s[1]-1,B,s[1]):  # 배수만큼 반복
                if state[i]:
                    state[i]=0 #1이면 0으로
                else:
                    state[i]=1 #0이면 1로
        else:   #여자이면
            if B==1 or B==2:   #버튼수가 1또는 2
                if state[i]:
                    state[i]=0 #1이면 0으로
                else:
                    state[i]=1 #0이면 1로
            else:
                i1=s[1]-1
                i2=s[1]-1
                for i in range((B-1)//2):  #최대 버튼수-1//2 만큼 탐색
                    i1+=1   #오른쪽으로
                    i2-=1   #왼쪽으로
                    if i1>=B or i2<0: #밖이면 break
                        i1 -=1
                        i2 +=1
                        break
                    if state[i1] != state[i2]: #대칭이 아니면
                        i1 -= 1
                        i2 += 1
                        break
                for i in range(i2,i1+1): # 상태바꿔야하는 것 까지 변환
                    if state[i]:
                        state[i] = 0  # 1이면 0으로
                    else:
                        state[i] = 1  # 0이면 1로

button_num= int(input())                # 버튼 수
state = list(map(int, input().split())) # 버튼상태
student_num = int(input())              # 학생수
student_list=[]                         # 학생 리스트 [성별, 받은 번호]
for _ in range(student_num):
    student_list.append(list(map(int,input().split())))

change_state(button_num, student_num,student_list)
c=0
for i in range(len(state)):
    c += 1
    print(state[i], end=' ')
    if c%20==0:
        print()
print()