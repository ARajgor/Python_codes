def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


i =int(input("Enter number of elements: "))
l=[]
for j in range(0,i):
    e=int(input("Enter element: "))
    l.append(e)
total = sumOfList(l, len(l))

print("Sum of all elements in given list: ", total)