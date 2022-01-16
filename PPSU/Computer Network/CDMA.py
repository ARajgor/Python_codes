import numpy as np

d1 = -1
d2 = -1
d3 = 1
d4 = 1
print("sender d1: ", d1)
print("sender d2: ", d2)
print("sender d3: ", d3)
print("sender d4: ", d4)

c1 = [1, 1, 1, 1]
c2 = [1, -1, 1, -1]
c3 = [1, 1, -1, -1]
c4 = [1, -1, -1, 1]

d1c1 = np.multiply(d1, c1)
d2c2 = np.multiply(d2, c2)
d3c3 = np.multiply(d3, c3)
d4c4 = np.multiply(d4, c4)

data = d1c1 + d2c2 + d3c3 + d4c4
print("Sum: ", data)

r1 = np.sum(np.multiply(data, c1)) / 4
r2 = np.sum(np.multiply(data, c2)) / 4
r3 = np.sum(np.multiply(data, c3)) / 4
r4 = np.sum(np.multiply(data, c4)) / 4

print("receiver r1: ", r1)
print("receiver r2: ", r2)
print("receiver r3: ", r3)
print("receiver r4: ", r4)