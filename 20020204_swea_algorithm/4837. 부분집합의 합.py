import sys
sys.stdin=open("sample_input_부분집합.txt")

test=int(input())
for x in range(test):
    a=[1,2,3,4,5,6,7,8,9,10,11,12]
    lst=list(map(int,input().split( )))
    cnt=0
    n=len(a)
    for i in range(1<<n):
        arr=[]
        for j in range(n):
            if i&(1<<j)!=0: # 비트가 1인지 아닌지 체크
                arr.append(a[j]) # 0이 아닌경우에 해당되면 넣음
        if len(arr)==lst[0] and lst[1]==sum(arr):
            cnt+=1

    print("#{} {}".format(x+1,cnt))