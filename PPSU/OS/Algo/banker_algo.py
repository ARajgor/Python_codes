import numpy as np
from pandas import *
no_p = 5
#no_p = int(input("number of processes : "))

#print("--- Insert Values like: A B C ---")
total_resources = np.array([10, 5, 7])
#total_resources = np.array([int(i) for i in input("total resources:").split()])
#print("\n--- Enter Resource Allocation of Process ---")
allocation = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])
#allocation = np.array([[int(i) for i in input(f"allocation of process {j + 1} : ").split()] for j in range(no_p)])
#print("\n--- Enter Maximum need of Resource of Process ---")
maximum_need = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [4, 2, 2], [5, 3, 3]])
#maximum_need = np.array([[int(i) for i in input(f"maximum need of process {j + 1} : ").split()] for j in range(no_p)])

process = no_p

sqeuence = []
remaining_need = maximum_need - allocation
# print(remaining_need)
# remaining_need = [[7,4,3], [1,2,2], [6,0,0], [2,1,1], [5,3,1]]
total = allocation.sum(axis=0)
available = total_resources - total
pro = [int(i+1) for i in range(no_p)]
available2 = []
available2.append(available)
# available = [3, 3, 2]
# print("available",available)
flag = [0] * no_p
# print("flag:", all(flag))

while all(flag) is not True:
    for i in range(no_p):
        temp = np.greater_equal(available, remaining_need[i])
        temp2 = all(temp)
        if temp2 is True and flag[i] == 0:
            flag[i] += 1
            sqeuence.append(i+1)
            if process == 1:
                break
            available = available + allocation[i]
            available2.append(available)
            process = process - 1

data = zip(allocation,maximum_need,available2,remaining_need)
DF1 = DataFrame(data=data, index=pro, columns=["Allocation", "Maximum_need", "Available", "Remaining_need"])
DF1.index.name = "Processs"
print(DF1)

print("\n-- Order of Execution of process")
print("sqeuence: ", sqeuence)
# 2,4,5,1,3