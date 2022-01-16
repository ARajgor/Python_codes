# basic_salary=[]
# for i in range(3):
#     s=int(input(f"enter the basic salary of employee no {i+1} :"))
#     basic_salary.append(s)
#
# for i in basic_salary:
#     da=i*(20/100)
#     hra=i*0.5
#     ma=i*0.1
#     gross_salary=i+da+hra+ma
#     print(f"the gross salary of {i} employee is :",gross_salary)



# for i in range(99,0,-1):
#     if i==1:
#         print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
#         break
#     print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i-1} bottles of beer on the wall.")
#
#
# print("No bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")


# i=input("Enter a String : ")
# print("convert to lower : ",i.lower())
# print("convert to upper : ",i.upper())
# print("convert to title case : ",i.title())
# print("convert to capitalize : ",i.capitalize())
#
# i=input("enter a String to check alphanumeric characters:")
# if i.isalnum():
#     print("yes it is alphaumeric characters")
# else:
#     print("no it's not..!!!...try again")   #if its contain except a-z ,A-Z,0-9


string="restart"
#a=string.index('o') #when its not found then traceback
#f=string.find('o')  #when its not found then return -1
#print(a,f)
char=string[0]
string=string.replace('r','$')
s1=char+string[1:]
print(s1)





