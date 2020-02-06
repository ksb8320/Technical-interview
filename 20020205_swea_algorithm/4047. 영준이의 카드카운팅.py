import sys
sys.stdin=open("sample_input_card.txt")

test=int(input())
for t in range(test):
    lst=[]
    s_cnt=13
    d_cnt=13
    h_cnt=13
    c_cnt=13
    s=str(input()) #  영준이가 가지고 있는 카드정보
    
    for i in range(0,len(s),3):
        lst.append(s[i:i+3]) # 카드정보를 카드별로 나눠줌

    for i in range(len(lst)):
        if "S" in lst[i]:
            s_cnt-=1
        elif "D" in lst[i]:
            d_cnt-=1
        elif "H" in lst[i]:
            h_cnt-=1
        elif "C" in lst[i]:
            c_cnt-=1
        
    flag=0
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                flag=1
        if flag==1:
            print("#{} {}".format(t+1,"ERROR"))
            break
    # for i in range(len(lst)):
    #     if lst[i]==lst[i-1]:
    #         flag=1
    #         print("#{} {}".format(t+1,"ERROR"))
    #         break
    if flag==0:
        print("#{} {} {} {} {}".format(t+1,s_cnt,d_cnt,h_cnt,c_cnt))
    
