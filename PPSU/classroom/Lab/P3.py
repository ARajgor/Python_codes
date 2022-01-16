#1)
a=float(1/2.0)
print("int divide float: ",a)
#2)
b=int(1/2.0)
print("int divide float: ",b)
#3)
x,y=input("enter x and y").split()
print("x raise to power y",pow(x,y))
#4)
print(-(3+2))
print(-3+2)
print(3-2*8)
#5)
#----logical and relational-----
a,b,c,d=5,6,7,-8
if a>0 and b>0:
    print("both positive number")
if a<0 or b<0 or c<0 or d<0:
    print("there is negative number....!!!!")
#----bitwise----
a,b=10,20
print(a&b)  #Bitwise AND return 1 if both bits are 1
print(a|b)  #bitwise OR return 1 if one of them is 1
print(~a,~b) #bitwise NOT return one's compliement of number(- (binary +1))

#6)
f=float(input("enter temp in fahrenheit: "))
c=(f-32)*(5/9)
print("In celsius: ",c)
#7)
r=float(input("enter radius of circle :"))
print(f"Circumference of circle with radius {r} is: ",3.14*r*r)
#8)
a,b=input("enter two number a and b for swap :").split()
temp=a
a=b
b=temp
print(f"the value of a after swap: ",a)
print(f"the value of b after swap: ",b)
#9)
import math
x1,x2=input("enter x1 and x2 point: ").split()
y1,y2=input("enter y1 and y2 point: ").split()
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("distance is: ",distance)
#10)
m,c,p=input("enter marks of maths , chemistry and physics respectively :").split()
avg=(m+c+p)/3
print("average marks :",avg)
percentage=((m+c+p)/300)*100
print("percentage :",percentage)