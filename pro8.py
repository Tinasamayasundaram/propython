import math
import functools
n,k=map(int,input().split())
l1=[int(i) for i in input().split()]
for i in range(k):
    c,d=map(int,input().split())
    t=functools.reduce(math.gcd,l1[c-1:d])
    print(t)
