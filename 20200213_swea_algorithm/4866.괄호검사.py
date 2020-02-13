def a(string):
    for i in range(len(string)):
        now=string[i]
        if now=="(" or now=="{":
            stack.append(now) # ( or { 나오면 스택에 넣어줌

        elif now==")" or now=="}": # ) or } 나오면 스택에 안넣어도됨 
            if stack: # 스택에 무엇이있다면
                before=stack.pop()
            else: # 스택에 무엇이 없다면
                return 0

            if before=="(" and now=="}":
                return 0
            if before=="{" and now==")":
                return 0
        
    if len(stack)==0:
        return 1
    else:
        return 0

t=int(input())
for t in range(t):
    stack=[]
    before=""
    string=list(map(str,input()))
    print("#{} {}".format(t+1,a(string)))
