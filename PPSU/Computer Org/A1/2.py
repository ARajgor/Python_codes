a=1010
c=0
i=len(str(a))-1
for j in str(a):
    c=c+(2**i)*int(j)
    i=i-1
print(c)