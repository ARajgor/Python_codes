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

n=6                                                           #########
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

pn=[]
RQ = []
z = BT
BT1=tuple(BT)
flag = []
RTmate=[]
ATc=[]
RQ.append(z[0])
pn.append(0)
for i1 in range(n):
    flag.append(0)
    RTmate.append(0)
    ATc.append(0)
    CT.append(0)
c = 0
c1=0
BT=list(BT1)
while True:
    i2 = 0
    if (RTmate[pn[0]] == 0):
        ATc[pn[0]] = GC
        RTmate[pn[0]] = 1
    if RQ[i2] > TQ:        ###########
        GC = GC + TQ
        z[pn[0]] = z[pn[0]] - TQ
        c3=pn[0]
        RQ.pop(0)
        pn.pop(0)
        flag[c3] = 1
        for j1 in range(n):         #############
            if AT[j1] <= GC and flag[j1] == 0 and c1<AT[j1]:
                RQ.append(z[j1])
                pn.append(j1)
        for j2 in range(n):          #########
            if AT[j2] <= GC and flag[j2] == 1:
                RQ.append(z[j2])
                pn.append(j2)
        flag[c3] = 2

    else:
        GC = GC + RQ[i2]
        # z[i2] = 0
        z[pn[i2]]=0
        flag[i2] = -1
        RQ.pop(0)
        cfor=pn[0]
        pn.pop(0)
        for j11 in range(n):         #############
            if AT[j11] <= GC and flag[j11] == 0 and c1<AT[j11]:
                RQ.append(z[j11])
                pn.append(j11)
        for j22 in range(n):          #########
            if AT[j22] <= GC and flag[j22] == 1:
                RQ.append(z[j22])
                pn.append(j22)
        if GC < AT[i2] + BT[i2]:
            IT = AT[i2] + BT[i2] - GC
            GC = AT[i2] + BT[i2]
        CT[cfor]=GC
    if len(RQ) == 0:
        break
    c += 1
    c1= GC
BT=list(BT1)
print("P: ",P)
print("AT: ",AT)
print("BT: ",BT)
print("CT: ",CT)
print("ATc: ",ATc)

BT=list(BT1)
for i in range(n):
    TAT.append(CT[i]-AT[i])
    AvgTAT+=TAT[i]
    WT.append(TAT[i]-BT[i])
    AvgWT+=WT[i]
    RT.append(ATc[i]-AT[i])
    AvgRT+=RT[i]

print("average turn around time:",AvgTAT/n)
print("average waiting time:",AvgWT/n)
print("average response time:",AvgRT/n)
print("ideal time:",IT)

pandas.set_option('display.max_columns',10)


data={'Process':P,'Arrival-Time':AT,'Brust-Time':BT,'Complition-Time':CT,'TurnAround-Time':TAT,'Waiting-Time':WT,'Responce-Time':RT}
DF1=DataFrame(data)
DF=DF1.set_index("Process")
DF1=DF.sort_index(ascending=True)
print(DF1)