#----------------(1)
# string=input("Enter a string: ")
# pop=int(input("Enter index of character: "))
#
# first=string[:pop]
# right=string[pop+1:]
# print("results: ",first+right)


#2)
# s1=input("enter 1st string: ")
# s2=input("enter 2nd string: ")
# if(sorted(s1)==sorted(s2)):
#     print("The string are anagrams.")
# else:
#     print("The string aren't anagrams.")

# string=input("Enter a string: ")
# result=string[len(string)-1]+string[1:len(string)-1]+string[0]
# print("Output String: ",result)


#3)
# a=input("enter 1st string: ")
# b=input("enter 2nd string: ")
# c1=0
# c2=0
# for i in a:
#     c1=c1+1
# for i in b:
#     c2=c2+1
# if(c1>c2):
#     print("Larger string is: ",a)
# elif(c1<c2):
#     print("Larger string is: ",b)
# else:
#     print("string is same...!!")


#5)
# string=input("Enter a string: ")
# c1=0
# c2=0
# for i in string:
#     if(i.islower()):
#         c1=c1+1
#     elif(i.isupper()):
#         c2=c2+1
# print(f"Total {c1} character are in Uppercase")
# print(f"Total {c2} character are in Lowercase")


#6)
string=input("Enter a string: ")
c=0
vowels='aeiouAEIOU'
for i in string:
    if i in vowels:
        c=c+1
print(f"Total {c} number of vowels are present..")


#7)
# string=input("Enter a string: ")
# c=0
# for i in string:
#     c=c+1
# print("length of string is :",c)


#8)
# string=input("Enter a string: ")
# new=string.split()
# word=len(new)
# char=0
# for i in string:
#     char=char+1
# print("Number of characters are: ",char-word+1)
# print("Number of words are: " ,word)


#9)
# string=input("Enter a string: ").split()
# di= {}
# for i in string:
#     di[i]=string.count(i)
# print(di)


# 10)
# a=input("enter a string: ")
# b=input("enter a substring: ")
# if b in a:
#     print(f"{b} is substring of {a}")
# else:
#     print(print(f"{b} is not substring of {a}"))