input1,input2=input().split()
temp=abs(len(input1)-len(input2))
for i in range(len(input1)):
    if len(input2)==1 and input2[i] in input1:
        break
    if input1[i]!=input2[i]:
        temp+=1
print(temp)
