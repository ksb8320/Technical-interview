import sys
sys.stdin=open("input.txt")

def check(start,end,card_num): 
    if start==end:
        return start # 빠져나오는 조건
    else:
        v1=check(start,(start+end)//2,card_num) # 절반 나눈 첫번째 그룹, 재귀
        v2=check(((start+end)//2)+1,end,card_num) # 절반 나눈 두번재 그룹, 재귀

        if card_num[v1]=="1" and card_num[v2]=="2":
            return v2
        elif card_num[v1]=="1" and card_num[v2]=="3":
            return v1
        elif card_num[v1]=="2" and card_num[v2]=="1":
            return v1
        elif card_num[v1]=="2" and card_num[v2]=="3":
            return v2
        elif card_num[v1]=="3" and card_num[v2]=="1":
            return v2
        elif card_num[v1]=="3" and card_num[v2]=="2":
            return v1
        elif card_num[v1]==card_num[v2]: # 무승부
            return v1 # 누가 이겼는지를 알기위해 인덱스 출력

test=int(input())
for test in range(test):
    n=int(input())
    card_num=input().split()

    print("#{} {}".format(test+1,check(0,n-1,card_num)+1))