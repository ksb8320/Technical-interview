T=int(input())
for t in range(T):
    n=int(input())
    arr=[0]*n
    for i in range(n):
        arr[i]=list(map(int,input()))
    sum=0
    start=end=n//2
    for i in range(n):
        for j in range(start,end+1):
            sum+=arr[i][j]
        if i<n//2: 
            start-=1
            end+=1
        else: # i가 커지다가 n//2 보다 커지면
            start+=1
            end-=1    

    print("#{} {}".format(t+1,sum))