l=input("enter numbers: ").split()
even=[]
for i in l:
    if int(i)%2==0:
        even.append(int(i))
print("Even numbers: ",even)
