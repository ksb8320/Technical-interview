t=int(input())
for test in range(t):
    n=int(input())
    arr=[0]*n
    for i in range(n):
        arr[i]=list(map(str,input().split()))

    new_lst=['']*n
    # 90도 회전
    for j in range(n):
        for i in range(n-1,-1,-1):
            new_lst[j]+=arr[i][j]
        new_lst[j]+=" "
        
    # # 180도 회전
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            new_lst[n-i-1]+=arr[i][j]
        new_lst[n-i-1]+=" "

    # # 270도 회전
    for j in range(n-1,-1,-1):
        for i in range(n):
            new_lst[n-j-1]+=arr[i][j]
        new_lst[n-j-1]+=" "
    print("#{}".format(test+1))
    for i in new_lst:
        print("{}".format(i))


    
    