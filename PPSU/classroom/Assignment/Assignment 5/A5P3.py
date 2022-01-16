import re

s=input("Enter a String: ")
t=re.findall('^the',s)
if t:
    print("yes, it contain")
else:
    print("Sorry,No match")