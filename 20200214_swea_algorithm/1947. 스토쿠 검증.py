def func():
    lst=[]
    # 첫번째: 정사각형
    for i in range(0,7,3):
        for j in range(0,7,3):
            lst=[]
            for x in range(i,i+3):
                for y in range(j,j+3):
                    lst.append(arr[x][y])
            if len(set(lst))!=9:
                return 0

    #두번째: 가로 직사각형
    for i in range(9):
        lst=[]
        for j in range(9):
            lst.append(arr[i][j])
        if len(set(lst))!=9:
            return 0

    #세번째: 세로 직사각형
    for j in range(9):
        lst=[]
        for i in range(9):
            lst.append(arr[i][j])
        if len(set(lst))!=9:
            return 0
    return 1


# 메인문
test=int(input())
for test in range(test):
    arr=[0]*9
    for i in range(9):
        arr[i]=list(map(int,input().split()))
    

    print("#{} {}".format(test+1,func()))