def func():
    stack=[] # 스택 생성
    start=s
    visited=[False]*(v+1) # 방문한 배열들 방문안했다는 흔적을 만들고 만들어줌
    stack.append(s) # 초기값 스택에 넣어줌
    visited[s]=True # 첫번째 값 CHECK해줌

    while stack:
        for value in graph[start]:
            if not visited[value]: # 방문 안한곳만 감
                stack.append(value) # 갔음
                visited[value]==True # 갔으니깐 true로 만들어줌
                start=value
                if start==g:
                    return 1
                break
        else:
            start=stack.pop() # start를 팝한 값으로 바꿔줌
    return 0
tests=int(input())
for test in range(tests):
    v,e=map(int,input().split()) # v와 e를 받아줌
    graph={i:[] for i in range(1,v+1)} # 딕셔너리 만들어주기
    for i in range(e):
        n1,n2=map(int,input().split()) # 시작값과 끝값을 받아줌
        graph[n1].append(n2) # 딕셔너리 완성
    s,g=map(int,input().split())

    print("#{} {}".format(test+1,func()))