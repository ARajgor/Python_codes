from pandas import  *
import numpy as np
# P=[]
# AT=[]
# BT=[]
GC = 0
completion_time = []
ideal_time = 0
turnaround_time = []
waiting_time = []
response_time = []
AvgTAT = 0
AvgWT = 0
AvgRT = 0

no_process = 6
time_quantum = 4
Process =['P1','P2','P3','P4','P5','P6']
arrival_time =[0,1,3,5,7,9]                                               #########
burst_time = [5,6,3,1,5,4]

AT_z= not np.any(np.array(arrival_time))
print(AT_z)
# Sorting according by Arrival Time
for i in range(no_process):
    for j in range(no_process - 1, i, -1):
        if arrival_time[j] < arrival_time[j - 1]:
            Process[j], Process[j - 1] = Process[j - 1], Process[j]
            burst_time[j], burst_time[j - 1] = burst_time[j - 1], burst_time[j]
            arrival_time[j], arrival_time[j - 1] = arrival_time[j - 1], arrival_time[j]

#print(Process, arrival_time, burst_time)

pn = []
ready_queue = []
remaining_time = burst_time.copy()
fullRQ = []
flag = []
RTmate = []
ATcpu = []
ready_queue.append(remaining_time[0])
pn.append(0)
fullRQ.append(remaining_time[0])
for i1 in range(no_process):
    flag.append(0)
    RTmate.append(0)
    ATcpu.append(0)
    completion_time.append(0)

c1 = 0
while True:
    i2 = 0
    if RTmate[pn[0]] == 0:
        ATcpu[pn[0]] = GC
        RTmate[pn[0]] = 1
    if ready_queue[i2] > time_quantum:
        GC = GC + time_quantum
        remaining_time[pn[0]] = remaining_time[pn[0]] - time_quantum
        c3 = pn[0]
        ready_queue.pop(0)
        pn.pop(0)
        flag[c3] = 1
        for j1 in range(no_process):
            if arrival_time[j1] <= GC and flag[j1] == 0 and c1 <= arrival_time[j1] and AT_z: #when arrival time is zero
                ready_queue.append(remaining_time[j1])
                fullRQ.append(remaining_time[j1])
                pn.append(j1)
            elif arrival_time[j1] <= GC and flag[j1] == 0 and c1 < arrival_time[j1]: #arrival time is diffrent
                ready_queue.append(remaining_time[j1])
                fullRQ.append(remaining_time[j1])
                pn.append(j1)
        for j2 in range(no_process):
            if arrival_time[j2] <= GC and flag[j2] == 1:
                ready_queue.append(remaining_time[j2])
                fullRQ.append(remaining_time[j2])
                pn.append(j2)
        flag[c3] = 2

    else:
        GC = GC + ready_queue[i2]
        # z[i2] = 0
        remaining_time[pn[i2]] = 0
        flag[i2] = -1
        ready_queue.pop(0)
        cfor = pn[0]
        pn.pop(0)
        for j11 in range(no_process):
            if GC >= arrival_time[j11] > c1 and flag[j11] == 0:
                ready_queue.append(remaining_time[j11])
                fullRQ.append(remaining_time[j11])
                pn.append(j11)
        for j22 in range(no_process):
            if arrival_time[j22] <= GC and flag[j22] == 1:
                ready_queue.append(remaining_time[j22])
                fullRQ.append(remaining_time[j22])
                pn.append(j22)
        # if GC < arrival_time[i2] + burst_time[i2]:
        #     ideal_time = arrival_time[i2] + burst_time[i2] - GC
        #     GC = arrival_time[i2] + burst_time[i2]
        completion_time[cfor] = GC
    if len(ready_queue) == 0:
        break
    c1 = GC
#print("Burst_time:  ", burst_time)
print("P: ", Process)
print("AT: ", arrival_time)
print("BT: ", burst_time)
print("CT: ", completion_time)
print("ATc: ", ATcpu)
print("fullRQ: ", fullRQ)

for i in range(no_process):
    turnaround_time.append(completion_time[i] - arrival_time[i])
    AvgTAT += turnaround_time[i]
    waiting_time.append(turnaround_time[i] - burst_time[i])
    AvgWT += waiting_time[i]
    response_time.append(ATcpu[i] - arrival_time[i])
    AvgRT += response_time[i]

print("average turn around time:", AvgTAT / no_process)
print("average waiting time:", AvgWT / no_process)
print("average response time:", AvgRT / no_process)
print("ideal time:", ideal_time)

pandas.set_option('display.width', 320)
pandas.set_option('display.max_columns', 10)

data = {'Process': Process, 'Arrival-Time': arrival_time, 'Burst-Time': burst_time, 'Completion-Time': completion_time,
        'TurnAround-Time': turnaround_time, 'Waiting-Time': waiting_time, 'Response-Time': response_time}
DF1 = DataFrame(data)
DF = DF1.set_index("Process")
DF1 = DF.sort_index(ascending=True)

print(DF1)