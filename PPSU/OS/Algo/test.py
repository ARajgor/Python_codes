import numpy as np
from pandas import  *
# a=[int(i) for i in input("maximum resources : ").split()]
# print(a)
# currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(3)]
# print(currently_allocated)
#allocation = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])
#allocation = np.array([[int(i) for i in input(f"allocation of process {j + 1} : ").split()] for j in range(no_p)])
#maximum_need = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [4, 2, 2], [5, 3, 3]])
#a = zip(allocation,maximum_need)
#df = DataFrame(data=a,columns=['allocation','maximum_need'])
#print(df)

remaining_need = [[7,4,3], [1,2,2], [6,0,0], [2,1,1], [5,3,1]]
available = [3, 3, 2]

temp = np.greater_equal(available, remaining_need[0])
temp2 = all(temp)

print(temp)
print(temp2)