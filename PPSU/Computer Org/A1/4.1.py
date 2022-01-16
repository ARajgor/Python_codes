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
                    #Decimal to Binary function
A=7
B=25

a=dToB(A)
b=dToB(B)
a.reverse()
b.reverse()

while True:
    if len(a)<len(b):
        a.append(0)
    elif len(a)>len(b):
        b.append(0)
    else:
        break

a.reverse()
b.reverse()

for i,j in zip(a,b):
    q=i & j     #AND operation
    print(q,end="")