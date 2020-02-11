import sys
sys.stdin=open("in.txt")

for test in range(10):
    t=int(input()) # 길이
    arr=[""]*100
    for i in range(len(arr)):
        arr[i]=list(map(str,input()))
    result=0
    # 가로축
    for x in range(30, 10, -1):
        for i in range(100):
            for j in range(100-x+1):
                for k in range(x//2):
                    if arr[i][j+k]==arr[i][j+x-1-k]:
                        continue
                    else:
                        break
                else:
                    if x>result:
                        result=x
    # 세로축
    for x in range(30, 10, -1):
        for j in range(100):
            for i in range(100-x+1):
                for k in range(x//2):
                    if arr[i+k][j]==arr[i+x-1-k][j]:
                        continue
                    else:
                        break
                else:
                    if x>result:
                        result=x
    print("#{} {}".format(test+1,result))