a=int(input())
i=0
x=0
z=[]
while i<90 and i<a:
  r=0
  for j in str(a-i):
    r+=int(j)
  if r+(a-i)==a:
    x+=1
    z.append(a-i)
  i+=1
print(x)
for i in z:
  print(i)
