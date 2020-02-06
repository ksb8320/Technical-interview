import sys
sys.stdin=open("sample_input_특별한 정렬.txt")

T=int(input())
for T in range(1,T+1):
    n1=int(input())
    n2=list(map(int,input().split( )))
    new_list=[]


    # 선택정렬 해주기
    for i in range(n1-1):
        for j in range(i+1,n1):
            if n2[i]>n2[j]:
                n2[i],n2[j]=n2[j],n2[i] # n2는 정렬 되었음

    # 새로운 리스트를 만들어서 홀수번째 인덱스에는 작은수부터
    # 짝수번째 인덱스에는 큰수부터 역순으로 넣어줌
    for i in range(10):
        if i%2==0:
            new_list.append(max(n2))
            n2.remove(max(n2))
        else:
            new_list.append(min(n2))
            n2.remove(min(n2))

    print("#{} {}".format(T," ".join(map(str,new_list))))