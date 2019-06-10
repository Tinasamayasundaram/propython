mt,jt=map(str,input().split())
s=0
if len(mt)>len(jt):
  mt,jt=jt,mt
i=0
while i<len(mt):
  s+=(ord(jt[i])-ord(mt[i]))
  i+=1
for i in range(i,len(jt)):
  s+=ord(jt[i])-ord('a')+1
print(s)
