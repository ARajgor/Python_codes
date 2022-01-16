def dToB(a):
    if a>1:
        dToB(a//2)
    print(a%2,end="")

a="12C"
b=[]
hexa={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
for k in a:
    if k in hexa:
        b.append(hexa[k])
    else:
        b.append(int(k))
c=0
i=len(a)-1
for j in b:
    c=c+(16**i)*int(j)
    i=i-1

dToB(c)
