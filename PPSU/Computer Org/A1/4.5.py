def dToB(a):
    b=[]
    while True:
        c=a%2
        if c==0:
            b.append(0)
            a=a//2
        else:
            if a==1:
                b.append(a)
                break
            else:
                b.append(1)
                a=(a-1)//2
    b.reverse()
    return b
            # Decimal to Binary function

A=7
B=16
comA=[]
comB=[]
a=dToB(A)
b=dToB(B)

for i in a:
    comA.append(~i + 2)
for j in b:
    comB.append(~j + 2)

print(a,b)
print(comA,comB)