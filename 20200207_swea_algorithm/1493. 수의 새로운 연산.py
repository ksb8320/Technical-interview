
# test=int(input())
# arr=[0 for x in range(350)] 
# arr[0]=0
# for test in range(test):
#     find=list(map(int,input().split( )))
#     # for i in range(1,len(arr)):
#     #     arr[i]=arr[i-1]+i
# print(arr)

def mysum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum


def find_num(x,y): # 초기 좌표값을 넣어줌
    count=y-1 # y는 1이 될때까지 반복해야하므로 y-1을 카운트에 넣어줌
    x+=count # x는 카운트만큼 추가
    y-=count # y는 카운트만큼 감소
    # x = 4, y = 1
    return mysum(x) - count
# print(find_num(2,3))
def val(num):
    count=0
    a=0 # 라인찾는다 a는 라인임
    for i in range(400): # 배열의 크기는 그렇게 중요하지는 않음
        if num<=mysum(i): # 입력받은 값이 좌표에 해당하는 값보다 작다면
            a=i # 라인에 i 값을 넣어줌 i는 라인에 해당되는 값임
            break
    # 라인의 가장 우측하단 좌표 : a,1
    # 그 값 = mysum(a) 
    count = mysum(a) - num # a,1에 해당되는 값에서 입력한 값을 빼주면 그게 카운트
    a -= count  # 좌표값 a 에서 카운트만큼 빼줌
    y = 1+count # y는 그 반대로
    return [a,y] # 그 값에 해당되는 좌표를 리턴해줌
# print(val(13))

#def plus(a,b):
    #를 들어, &(1)=(1,1), &(5) = (2,2)이므로, 
    #1★5 = #(&(1)+&(5)) = #((1,1)+(2,2)) = #(3,3) = 13이 된다.
    #a+b=  



# print("#{} {}".format(test+1,value))