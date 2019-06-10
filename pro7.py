nt = int(input())
kt = 1000
for i in range(0,20):
    if pow(2,i)<=nt:
        a = abs(pow(2,i)-nt)
        if a<=kt:
            kt=a
print(kt)
