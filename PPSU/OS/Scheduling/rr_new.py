from pandas import *
#P=[]
#AT=[]
#BT=[]
GC=0
CT=[]
IT=0
TAT=[]
WT=[]
RT=[]
AvgTAT=0
AvgWT=0
AvgRT=0

n=6                                                            #########
TQ=4                                                           #########
P=['P1','P2','P3','P4','P5','P6']                              #########
AT=[0,1,3,5,7,9]                                               #########
BT=[5,6,3,1,5,4]                                               #########
# DF.sort_values("Arrival-Time", axis = 0, ascending = True, inplace = True)
# DF
for i in range(n):
    for j in range(n-1,i,-1):
        if AT[j]<AT[j-1]:
            P[j],P[j-1] =P[j-1],P[j]
            BT[j],BT[j-1]=BT[j-1],BT[j]
            AT[j],AT[j-1]=AT[j-1],AT[j]
print(P,AT,BT)                                                 #########

RQ = []
z = BT
flag = []
RQ.append(z[0])
for i1 in range(n):
    flag.append(0)

c = 0
while True:
    i2 = 0
#for i2 in range(n):
    if RQ[i2] > TQ:
        GC = GC + TQ
        z[i2 + c] = z[i2 + c] - TQ
        RQ.pop(0)
        flag[i2 + c] = 1
        for j1 in range(n):
            if AT[j1] <= GC and flag[j1] == 0:
                RQ.append(z[j1])
        for j2 in range(n):
            if AT[j2] <= GC and flag[j2] == 1:
                RQ.append(z[j2])

    else:
        GC = GC + z[i2]
        flag[i2] = -1
        RQ.pop(0)
        if GC < AT[i2] + BT[i2]:
            IT = AT[i2] + BT[i2] - GC
            GC = AT[i2] + BT[i2]
    CT.append(GC)
    if len(RQ) == 0:
        break
    c += 1