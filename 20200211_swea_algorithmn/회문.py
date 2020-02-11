import sys
sys.stdin=open("in.txt")
test=int(input())
for test in range(test):
    n,m=map(int,input().split())
    arr=[0 for _ in range(n)]
    for i in range(n):
        arr[i]=list(input())
    # temp=""
    # 가로축
    count=0
    print("#{} ".format(test+1),end="")
    for i in range(n):
        for j in range(0,n-m+1):
            for k in range(m//2):
                if arr[i][j+k]==arr[i][j+m-1-k]:
                    count+=1
            if count==m//2:
                for l in range(j,j+m):
                    print(arr[i][l],end="")
            count=0
    # 세로축
    count=0
    for j in range(n):
        for i in range(0,n-m+1):
            for k in range(m//2):
                if arr[i+k][j]==arr[i+m-1-k][j]:
                    count+=1
            if count==m//2:
                for l in range(i,i+m):
                    print(arr[l][j],end="")
            count=0
    print("")