n,k=map(int,input().split())
m=list(map(int,input().split()))
tq=[]
for i in range(0,k):
    d = []
    d=list(map(int,input().split()))
    s = m[d[0]-1]
    for j in range(min(d),max(d)):
        s=s^m[j]
    tq.append(s)
for i in range(0,len(tq)):
    print(tq[i])
