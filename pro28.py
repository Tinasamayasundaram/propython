o=int(input())
t=list(map(int,input().split()))
t.sort()
s=0
c=0
for i in range(len(t)):
    if t[i]>=s:
        c=c+1
    s=s+t[i]
print(c)
