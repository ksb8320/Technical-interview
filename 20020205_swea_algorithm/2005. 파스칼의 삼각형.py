

test=int(input())
for test in range(test):
    num=int(input())
    arr=[[0 for x in range(2*num-1)] for y in range(num)]
    arr[0][num-1]=1

    for i in range(1,num):
        for j in range(2*num-1):  
            if arr[i-1][j]!=0:
                arr[i][j-1] += arr[i-1][j]
                arr[i][j+1] += arr[i-1][j]   
    print('#{}'.format(test+1))

    for i in range(num):
        for j in range(2*num-1):
            if arr[i][j] != 0:
                print(arr[i][j],end=' ')
        print('')