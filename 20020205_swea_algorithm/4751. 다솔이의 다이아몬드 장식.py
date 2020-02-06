import sys
sys.stdin=open("sample_input_diamond.txt")

T=int(input())
for T in range(T):
    STR=input()
    arr=[["." for x in range((len(STR)*4)+1)] for y in range(5)]
    for i in range(5):
        if i==0 or i==4:
            for k in range(2,(len(STR)*4)+1,4):
                arr[i][k]="#"
        if i==1 or i==3:
            for l in range(1,(len(STR)*4)+1,2):
                arr[i][l]="#"
        if i==2:
            for m in range(0,(len(STR)*4)+1,4):
                arr[i][m]="#"
            for n in range(2,(len(STR)*4)+1,4):
                arr[i][n]=STR[n//4]

        print("".join(arr[i]))