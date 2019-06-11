n,m=map(int,input().split())
t=list(map(int,input().split()))
u=0
y=sorted(t)
x=(y[::-1])
for i in range(0,len(x)):
    z = m //(x[i])
    u = u + z
    m = m - (z *x[i])
print(u)
