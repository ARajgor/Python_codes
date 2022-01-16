import re

s=input("Enter a String: ")
f=re.findall('^[a-zA-Z0-9_]*$',s)
if f:
    print("yes we find")
else:
    print("sorry,no match")