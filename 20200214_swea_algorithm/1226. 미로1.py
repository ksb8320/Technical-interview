def func():
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    
    for i in range(4):
        check_x=x+dx[i]
        check_y=y+dy[i]
    
    while stack:
        for i in range():


    




# 메인
for test in range(10):
    t=int(input())
    miro=[0]*16
    for i in range(16):
        miro[i]=list(map(str,input())) # 미로 생성
    
    stack=[] # 스택 생성
    visited=[False]*100 # 방문했늕지 확인해주는 리스트 생성
    stack.append(miro[1][1]) # 시작점이 1,1 이라 해줬으니
    visited[0]=True # 시작점을 방문했으니 흔적을 남겨줌


