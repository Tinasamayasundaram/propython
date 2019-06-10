S2=int(input())
l1=list(map(int,input().split()))
count=0
for i in range(len(l1)-2):
    for j in range(i+1,len(l1)-1):
        for k in range(j+1,len(l1)):
            if l1[i]<l1[j]<l1[k] and i<j<k:
                count=count+1
print(count)
