string1=input("enter 1st string: ")
string2=input("enter 2nd string: ")
o=string2[:2]+string1[2:]+" "+string1[:2]+string2[2:]
print("output: ",o)