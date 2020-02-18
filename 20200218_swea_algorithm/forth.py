import sys
sys.stdin=open("input.txt")

def forth(string):
    stack=[]
    for i in range(len(string)):
        if string[i].isdecimal():
            stack.append(int(string[i]))
        elif string[i]=="+":
            if len(stack)<2:
                return "error"
            a=stack.pop()
            b=stack.pop()
            stack.append(a+b)
        elif string[i]=="-":
            if len(stack)<2:
                return "error"
            a=stack.pop()
            b=stack.pop()
            stack.append(b-a)
        elif string[i]=="*":
            if len(stack)<2:
                return "error"
            a=stack.pop()
            b=stack.pop()
            stack.append(a*b)
        elif string[i]=="/":
            if len(stack)<2:
                return "error"
            a=stack.pop()
            b=stack.pop()
            stack.append(b//a)
        elif string[i]==".":
            if len(stack)>=2:
                return "error"
            result=stack.pop()
            return result

test=int(input())
for test in range(test):
    string=list(map(str,input().split()))
    print("#{} {}".format(test+1,forth(string)))