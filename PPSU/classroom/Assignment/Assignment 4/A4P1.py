def prime(i,div=None):
    if div is None:
        div = i-1
    while div>=2:
        if i%div==0:
            print("Number is not prime")
            return False
        else:
            return prime(i,div-1)
    else:
        print("Number is prime")
        return True

i=int(input("Enter a number: "))
prime(i)