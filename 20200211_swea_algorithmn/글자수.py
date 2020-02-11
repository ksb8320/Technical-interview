import sys
sys.stdin=open("in.txt")
test=int(input())
for test in range(test):
    str1=input()
    str2=input()
    str1_dic={}
    count=0
    result=0
    for i in str1:
        for j in str2:
            if i==j:
                count+=1

        if i in str1_dic:
            pass
        else:
            str1_dic[i]=count
        count=0
    for key in str1_dic.keys():
        if str1_dic[key]>result:
            result=str1_dic[key]
    print("#{} {}".format(test+1,result))
    

