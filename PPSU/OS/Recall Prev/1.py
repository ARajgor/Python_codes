a=int(input("Enter a number: "))
def nextprime(a):
    while True:
        c=0
        for i in range(1,a):
            if(a+1)%i==0:
                c=c+1
        if c==1:
            print(a+1)
            break
        else:
            a=a+1
nextprime(a)