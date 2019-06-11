nn=int(input())
l=list(map(int,input().split()))
mm=[]
c=1
for i in l:
    if i not in mm:
        mm.append(i)
        

for i in range(len(mm)-1):
    if mm[i]<mm[i+1]:
        c=c+1
print(c) 
 
