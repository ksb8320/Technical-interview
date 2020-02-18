import sys
sys.stdin=open("sampleinput.txt")

def iswall(test_x,test_y,n): # 벽체크
        if n>test_y and n>test_x and test_x>=0 and test_y>=0: 
            return True
        return False

def maze():
    while len(stack)>0:
        start=stack.pop()
        for k in range(4):
            test_x=start[0]+dx[k]
            test_y=start[1]+dy[k]
            if iswall(test_x,test_y,n)==True: # 벽이 아닐때
                if arr[test_x][test_y]==3: # 목적지에 도착했으므로 1 리턴
                    return 1
                elif arr[test_x][test_y]==0:
                    stack.append([test_x,test_y]) # 스택에 담아주고
                    arr[test_x][test_y]=1  # 지나갔다는 흔적을 남겨줌
    return 0

test=int(input())
for test in range(test):
    n=int(input())
    arr=[[int(x) for x in input()] for _ in range(n)]

    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    stack=[]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                arr[i][j]=1 # 방문표시
                stack.append([i,j])
            elif arr[i][j]==3:
                ex=i
                ey=j
                break

    print("#{} {}".format(test+1,maze()))