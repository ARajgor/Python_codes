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
    for i in b:
        print(i, end="")
dToB(45)
