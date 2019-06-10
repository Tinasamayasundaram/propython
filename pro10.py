v=int(input())
k=list(map(int,input().split()))
t=0
for f in range(0,v):
    for u in range(0,f):
        if k[u]<k[f]:
            t=t+k[u]
print(t) 
