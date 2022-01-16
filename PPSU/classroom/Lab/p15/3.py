import numpy as np
user = open("user.txt" , 'w')
user.write("7 4 6 9 lets dance")
user.close()
user = open("user.txt" , "r")
word = ((user.read()).split())
print(np.sort(word))
user.close()