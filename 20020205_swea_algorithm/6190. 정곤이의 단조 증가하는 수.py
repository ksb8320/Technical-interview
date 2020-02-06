import sys
sys.stdin=open("s_input.txt")

test=int(input())
for test in range(test):
    n=int(input())
    danjo=list(map(int,input().split()))
    lst=[]
    new_lst=[]

    for i in range(n):
        for j in range(i+1,n): # 곱해서 새로운 리스트에 넣어줌
            lst.append(str(danjo[i]*danjo[j])) 

    for num in lst:
        for k in range(len(num)-1): # num을 비교
            if num[k] > num[k+1]:
                break
        else:
            new_lst.append(int(num))
    if new_lst:
        a=max(new_lst)
    else:
        a=-1
    print(new_lst)
    print("#{} {}".format(test+1,a))