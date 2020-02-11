badukpan=[[0 for y in range(20)] for x in range(20)]

a=int(input()) # 바둑알 개수 입력
for k in range(a):
    x,y=map(int,input().split( )) # 좌표입력
    for i in range(len(badukpan)): # 바둑판의 크기만큼 탐색
        for j in range(len(badukpan)): # 마찬가지
            if i==x-1 and j==y-1:
                badukpan[i][j]=1
print(badukpan)