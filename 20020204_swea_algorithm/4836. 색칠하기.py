import sys
sys.stdin=open("sample_input.txt")

test=int(input())
for t in range(1,test+1):
    arr = [[0 for x in range(10)] for y in range(10)]
    n=int(input())
    
    for x in range(n):
        
        cnt=0
        lst=list(map(int, input().split( )))
        if lst[-1]==1: # 리스트의 끝이 빨강일 경우
            for i in range(lst[0],lst[2]+1):
                for j in range(lst[1],lst[3]+1):
                    arr[i][j]+=1 # 배열의 인덱스에 1을 더해줌
        elif lst[-1]==2: # 리스트의 끝이 파랑일 경우
            for i in range(lst[0],lst[2]+1):
                for j in range(lst[1],lst[3]+1):
                    arr[i][j]+=2 # 배열의 인덱스에 2를 더해줌

        for i in range(len(arr)): 
            for j in range(len(arr)): 
                if arr[i][j]==3:
                    cnt+=1

    print("#{} {}".format(t,cnt))