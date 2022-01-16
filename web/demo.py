#1)
string = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high," \
         "\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are"
print(string)
print('\n')
#2)
num = int(input("enter any number :"))
print('binary : ', bin(num))
print('hexadecimal : ', hex(num))
print('octal : ', oct(num))
bi = input('enter a binary number :')
print('output: ',int(bi , 2))
print('\n')
#3)
c1 = 1 + 2j
c2 = 2 + 3j
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)

print((c1+c2).imag)
print((c1*c2).real)
print('\n')
#4)
import math
r = float(input("Enter a radius circle: "))
print('Area of circle' , math.pi*r*r)



