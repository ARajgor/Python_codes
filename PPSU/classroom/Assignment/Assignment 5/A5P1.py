import re

a=input("Enter the String: ")
c=re.findall('[a-zA-Z0-9]',a)
c1=re.findall("\w",a)  # shorter version
print("Output: ",c)