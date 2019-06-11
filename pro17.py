import sys
n1,k1 = input().split()
n1,k1 = int(n1), int(k1)
L1 = [ int(x) for x in input().split()]
for i in range(0,n1-1) :
    for j in range(i+1,n1) :
        if L1[i] + L1[j] == k1 :
            print('yes')
            sys.exit()
print('no')
