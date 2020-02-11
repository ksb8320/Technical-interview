import sys
sys.stdin=open("in.txt")

for test in range(10):
    t=int(input()) # 길이
    arr=[""]*8
    for i in range(len(arr)):
        arr[i]=list(map(str,input()))
    new_count=0
    count=0
    # 가로축
    for i in range(8):
        for j in range(8-t+1):
            for k in range(t//2):
                if arr[i][j+k]==arr[i][j+t-1-k]:
                    count+=1
            if count==t//2:
                new_count+=1
            count=0
    # 세로축
    for j in range(8):
        for i in range(8-t+1):
            for k in range(t//2):
                if arr[i+k][j]==arr[i+t-1-k][j]:
                    count+=1
            if count==t//2:
                new_count+=1
            count=0
    print("#{} {}".format(test+1,new_count))

