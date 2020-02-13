test=int(input())
for test in range(test):
    string=list(input())
    i=0
    while i<len(string)-1:
        if string[i]==string[i+1]:
            del string[i:i+2]
            i=0
        i+=1
    print("#{} {}".format(test+1,len(string)))

            