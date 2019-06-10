from itertools import combinations
str1,numbr1=map(int,input().split())
numbr2=len(str(str1))
x=list(combinations(str(str1),numbr2-numbr1))
x=(sorted(x))
y="".join(x[0])
print(y)
