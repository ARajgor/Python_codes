Q = [82, 170, 43, 140, 24, 16, 190]
n= len(Q)
clgt = []   # 82,140,170,190
cllv = []   # 16, 24, 43
cl = []
head_move = 0
initial_head = 53

for i in range(n):

    if initial_head < Q[i]:
        clgt.append(Q[i])
        clgt.sort()

    if initial_head > Q[i]:
        cllv.append(Q[i])
        cllv.sort()
cl = clgt + cllv

movements =(clgt[-1] - initial_head) + (clgt[-1] - cllv[0]) + (cllv[-1] - cllv[0])
print(cl)
print(movements)