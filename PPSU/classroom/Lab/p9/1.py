def addition(f,s):
    sum=f+s
    print(f"Sum of {f} and {s} is {sum}")

a,b=input("Enter two number for addition: ").split()
addition(int(a),int(b))