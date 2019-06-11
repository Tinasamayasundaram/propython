n=int(input())
l=list(map(int,input().split()))
m1=[]
a=1
for i in range(n-1):
    if l[i]<l[i+1]:
        a+=1
    else:
        m1.append(a)
        a=1
m1.append(a)
print(max(m1))
