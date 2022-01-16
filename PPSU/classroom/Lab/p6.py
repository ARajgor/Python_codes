# a=[2,5,1,8,3,4,6]
# c=0
# for i in a:
#     if i%2==0:
#         c=c+1
# print("sum of even numbers: ",c)


#a=[]
# print("enter a 10 positive values: ")
# for i in range(10):
#     a.append(int(input()))
# a.sort()
# print(a)


# a=[1,5,3,4,6,2]
# x=0
# for i in range(len(a)):
#     if i%2==0:
#         x=a[i]
#         a[i]=a[i+1]
#         a[i+1]=x
# print(a)


#
# a=[1,2,1,3,3,2,5,6]
# a=set(a)
# a=list(a)
# print(a)


#
# b=[]
# if len(b)==0:
#     print("this is empty list")
# else:
#     print("this is not empty list")



a=[1,2,3,4,5]
b=[1,6,7,8,9]
result=False
for i in a:
    for j in b:
        if i==j:
            result=True

print(result)