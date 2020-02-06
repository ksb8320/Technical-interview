import sys
sys.stdin=open("sample_input_세로로말해요.txt")

test=int(input())
for test in range(test):
    arr=[" " for x in range(5)] # 배열생성
    for i in range(5):
        arr[i]= list(input()) # 문자열을 리스트로 넣어줌 ( 다 나뉘어져서  나옴 ex. "A","a","b")
    a=0
    for i in range(5): 
        if len(arr[i])>a: # 가장 긴 길이가 무엇인지 알아야하니 0을 만들고 a보다 긴 길이 찾아줌
            a= len(arr[i])
    
    for i in range(5): 
        while len(arr[i])!=a: # 최대의 길이와 다른 길이가 있으면 
            arr[i].append("") # 배열의 뒤에 공백을 붙여줌
    new=""
    for j in range(a):
        for i in range(5):
            new+=arr[i][j]
    print(new)

