str=input()
l=["GLGLGL","GRRG","GLLG","GRGRGR"]
count=0
for i in range(0,len(l)):
    if l[i] in str:
        count+=1
if count==1:
    print("yes")
else:
    print("no")
