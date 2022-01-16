# 1. Write a code to create tuple1 with following values "disco",10,1.2.
# a=("disco",10,1.2)
# print(a)

# 2. Write a code to perform following operations
# from numpy import sort
# print("[a.]")
# tuple1=("disco",10,1.2)
# for i in tuple1:
#     print(i)
# print("\n")
#
# print("[b.]")
# for i in tuple1:
#     print(type(i))
# print("\n")
#
# print("[c.]")
# for i in range(-1,-1*(len(tuple1)+1),-1):
#     print(tuple1[i])
# print("\n")
#
# print("[d.]")
# tuple2=("hard rock", 10)
# tuple3=tuple1+tuple2
# print(tuple3 ,"\n")
#
# print("[e.]")
# print(tuple3[:2],"\n")
#
# print("[f.]")
# print(len(tuple3),"\n")
#
# print("[g.]")
# print(sort(tuple3))

# 3. Write a program to find the first occurrence of an element in a tuple.
# a=input("enter elements: ").split()
# a=tuple(a)
# input=(input("Enter the character: "))
# print(f"first occurrence of {input} is :",a.index(input))


# 4. Write a program to insert new element into a tuple of elements at a
# specified position and delete element from a tuple.
a = (1,2,3,4,5,6,7,8,9)
print(a)
# add a num
a = a + (43 , 'red')
print(a)
# delete element
n = 2
a = a[:n] + a[n+1:]
print(a)
# add at spacific index
n=1
a = a[:n] + (3,) + a[n:]
print(a)