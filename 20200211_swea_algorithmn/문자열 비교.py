import sys
sys.stdin=open("in.txt")
test=int(input())
for test in range(test):
    string_a=input()
    string_b=input()
    def bruteforce(a,b):
        i=j=0
        while i<len(string_a) and j<len(string_b):#j의 길이와 i의 길이만큼 반복
            if b[i]!=a[j]:
                i=i-j+1 #원상복귀 시킨 뒤 하나씩 증가
                j=0
            else:
                i=i+1
                j=j+1
        if string_a in string_b:
            return 1
        else:
            return 0
    print("#{} {}".format(test+1,bruteforce(string_a,string_b)))
