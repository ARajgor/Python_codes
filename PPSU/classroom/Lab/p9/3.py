def add(a,b):
    s=0
    for i in range(a,b+1):
        if(i%3==0):
            s=i+s
    print(f"sum between {a} and {b} is {s}")

add(1,10)