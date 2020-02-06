import sys
sys.stdin=open("input_파리퇴치.txt")

test=int(input())
for test in range(test):

    parichae=list(map(int,input().split())) # 파리가 있는 크기와 파리채 크기 선언
    arr=[[0 for x in range(parichae[0])] for y in range(parichae[0])] # 파리있는 구역 만들어주기

    for i in range(parichae[0]):
        arr[i]=list(map(int,input().split())) #파리개수 넣어줌

    result=[]
    for x in range(0,parichae[0]-parichae[1]+1):# 파리채가 있는 크기가 만들어짐
        for y in range(0,parichae[0]-parichae[1]+1):
            count=0
            for px in range(x,x+parichae[1]):
                for py in range(y,y+parichae[1]):
                    count+=arr[px][py]
            result.append(count)

    print("#{} {}".format(test+1,max(result)))
