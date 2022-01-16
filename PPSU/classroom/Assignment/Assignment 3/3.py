# 1st method
l=input("enter numbers: ").split()
r=1
for i in l:
    r=r*int(i)
print("product of all numbers: ",r)

#2nd method
import math
L=[1,2,3]
product=math.prod(L)
print("Using math lib: ",product)