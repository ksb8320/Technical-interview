import sys
sys.stdin=open("sample_input_이진탐색.txt")

test=int(input())
for a in range(test):
    number=list(map(int,input().split( )))
    student_a=number[1]
    student_b=number[2]
    cnt_a,result=0,0
    start=1
    end=number[0]
    
    # 학생 a의 경우
    while 1:
        mid=(start+end)//2
        if mid==student_a:
            break
        elif mid>student_a:
            end=mid
            cnt_a+=1
        else:
            start=mid
            cnt_a+=1

    cnt_b=0
    start=1
    end=number[0]
    # 학생 b의 경우
    while 1:
        mid=(start+end)//2
        if mid==student_b:
            break
        elif mid>student_b:
            end=mid
            cnt_b+=1
        else:
            start=mid
            cnt_b+=1

    # a와 b의 개수 비교
    if cnt_a<cnt_b:
        result='A'
    elif cnt_a>cnt_b:
        result='B'
    elif cnt_a==cnt_b:
        result=0
    print("#{} {}".format(a+1,result))
