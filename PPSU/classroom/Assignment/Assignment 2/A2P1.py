string=input("Enter a string: ")
if len(string)>=2:
    s=string[:2]+string[len(string)-2:]
    print("output: ",s)
else:
    print("not vaild (length>2)")