from pandas import *

GC = 0

ideal_time = 0
turnaround_time = []
waiting_time = []
response_time = []
AvgTAT = 0
AvgWT = 0
AvgRT = 0

no_process = 5
process = ['P1', 'P2', 'P3', 'P4', 'P5']
priority = [3, 4, 5, 2, 1]
arrival_time = [0, 3, 4, 5, 10]
burst_time = [8, 4, 1, 6, 1]
completion_time = [0, 0, 0, 0, 0]
flag = [0, 0, 0, 0, 0]
flag1 = [-1, -1, -1, -1, -1]

for i in range(no_process):
    for j in range(no_process - 1, i, -1):
        if priority[j] < priority[j - 1]:
            process[j], process[j - 1] = process[j - 1], process[j]
            priority[j], priority[j - 1] = priority[j - 1], priority[j]
            burst_time[j], burst_time[j - 1] = burst_time[j - 1], burst_time[j]
            arrival_time[j], arrival_time[j - 1] = arrival_time[j - 1], arrival_time[j]

while True:
    for i in range(no_process):
        if GC >= arrival_time[i] and flag[i] != -1:
            GC = GC + burst_time[i]
            if GC < arrival_time[i] + burst_time[i]:
                ideal_time = arrival_time[i] + burst_time[i] - GC
                GC = arrival_time[i] + burst_time[i]
            completion_time[i] = GC
            flag[i] = -1
            break
    if flag == flag1:
        break

for i in range(no_process):
    turnaround_time.append(completion_time[i] - arrival_time[i])
    AvgTAT += turnaround_time[i]
    waiting_time.append(turnaround_time[i] - burst_time[i])
    AvgWT += waiting_time[i]
    response_time.append(completion_time[i] - burst_time[i] - arrival_time[i])
    AvgRT += response_time[i]

print("P: ", process)
print("Py: ", priority)
print("AT: ", arrival_time)
print("BT: ", burst_time)
print("CT: ", completion_time)
print("TAT: ", turnaround_time)
print("WT: ", waiting_time)
print("RT: ", response_time)

print("average turn around time:", AvgTAT / no_process)
print("average waiting time:", AvgWT / no_process)
print("average response time:", AvgRT / no_process)
print("ideal time:", ideal_time)

data = {'Process': process, 'Priority': priority, 'Arrival-Time': arrival_time, 'Brust-Time': burst_time, 'Complition-Time': completion_time,
        'TurnAround-Time': turnaround_time, 'Waiting-Time': waiting_time, 'Responce-Time': response_time}
DF1 = DataFrame(data)
DF = DF1.set_index("Process")
DF1 = DF.sort_index(ascending=True)
pandas.set_option('display.width', 300)
pandas.set_option('display.max_columns', 10)
print(DF1)
