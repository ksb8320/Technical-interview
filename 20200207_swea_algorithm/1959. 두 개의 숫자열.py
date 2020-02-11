import sys
sys.stdin=open("input_두개의숫자열.txt")

test=int(input())
for test in range(test):
    n,m=map(int,input().split( ))
    a=list(map(int,input().split( ))) # 첫번째 배열입력
    b=list(map(int,input().split( ))) # 두번째 배열입력

    if n>m: # 변수를 만들어줘서 입력해줌
        longer,shorter=n,m
        long_list,short_list=a,b
    elif n<m:
        longer,shorter=m,n
        long_list,short_list=b,a

    result=-1000
    for i in range(longer-shorter+1): # 긴것의 인덱스는 그대로 둠
        sum=0
        for j in range(i,i+shorter): # 짧은것을 옮겨야하는 경우
            sum+=long_list[j]*short_list[j-i] # sum에 곱해주기
        if sum>result:
            result=sum

    print("#{} {}".format(test+1,result))