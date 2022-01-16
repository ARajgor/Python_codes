n=int(input("enter total number of process:"))
process=[]                       
at=[]                            #arrival time
bt=[]                            #brust time

for i in range(n):
    print("process:",i+1)
    process.append(i + 1)
    y=int(input("arrival time:"))
    at.append(y)
    z=int(input("brust time:"))
    bt.append(z)

for i in range(n):
    for j in range(n-1,i,-1):
        if at[j]<at[j-1]:
            process[j], process[j - 1] = process[j - 1], process[j]
            bt[j],bt[j-1]=bt[j-1],bt[j]
            at[j],at[j-1]=at[j-1],at[j]
        if at[j]==at[j-1] and bt[j]<bt[j-1]:
            process[j], process[j - 1] = process[j - 1], process[j]
            bt[j], bt[j - 1] = bt[j - 1], bt[j]
            at[j], at[j - 1] = at[j - 1], at[j]

gt=0
ct=[]                            #complition time
it=0                             #ideal time

for i in range(n):
    gt+=bt[i]
    if at[i] <= gt:
        for j in range(n - 1, i+1, -1):
            if at[j]<=gt and bt[j]<bt[j-1]:
                process[j], process[j - 1] = process[j - 1], process[j]
                bt[j], bt[j - 1] = bt[j - 1], bt[j]
                at[j], at[j - 1] = at[j - 1], at[j]
    if gt<at[i]+bt[i]:
        it=at[i]+bt[i]-gt
        gt=at[i]+bt[i]
    ct.append(gt)

tat=[]                           #turn around time
wt=[]                            #waiting time
rt=[]                            #responce time
avgtat=0
avgwt=0
avgrt=0

for i in range(n):
    tat.append(ct[i]-at[i])
    avgtat+=tat[i]
    wt.append(tat[i]-bt[i])
    avgwt+=wt[i]
    rt.append(ct[i]-bt[i]-at[i])
    avgrt+=rt[i]

for i in range(n):
    for j in range(n-1,i,-1):
        if process[j]<process[j - 1]:
            process[j], process[j - 1]= process[j - 1], process[j]
            bt[j],bt[j-1]=bt[j-1],bt[j]
            at[j],at[j-1]=at[j-1],at[j]
            ct[j],ct[j-1]=ct[j-1],ct[j]
            tat[j],tat[j-1]=tat[j-1],tat[j]
            wt[j],wt[j-1]=wt[j-1],wt[j]
            rt[j],rt[j-1]=rt[j-1],rt[j]

avgtat /= n
avgwt /= n
avgrt /= n

print("process at bt  ct  tat  wt  rt")
for i in range(n):
    print(process[i], "     ", at[i], " ", bt[i], " ", ct[i], " ", tat[i], " ", wt[i], " ", rt[i])
print("average turn around time:",avgtat)
print("average waiting time:",avgwt)
print("average response time:",avgrt)
print("ideal time:",it)
