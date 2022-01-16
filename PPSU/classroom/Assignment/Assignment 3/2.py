L = ["Michael Jackson", 10.1, 1982]

# a) Print the elements on each index (positive as well as negative index)
print("Positive Index: ")
for i in L:
    print("\t\t\t\t",i)

print("Negative Index: ")
for i in L[::-1]:
    print("\t\t\t\t",i)

# b)to add elements to list using extend and append function.

new=["Dance","hip-hop"]
L.extend(new)
print("with extend: ",L)
L.append(50)
print("with append: ",L)

#c) Change the element based on the index
L[1]=0
print("change element: ",L)

#d)Delete the element based on the index
L.pop(3)
print("Delete element: ",L)

#e)Copy (copy by reference) the list
c=L.copy()
print("copy: ",c)