process_no = [1,2,3,4,5]            #Round Robin CPU Scheduling algorithm
arrival_time = [0,1,2,3,4]
burst_time = [5,2,3,1,6]

count = 0
remain_process = 5

ready_queue = []
running_queue = []

remaining_time = [5,2,3,1,6]
completion_time = 0
total_waiting_time = 0
turnaround_time = 0
time_q = 2
i = 0
wt = 0

while remain_process != 0 :

    if burst_time[i] > time_q:

        for j in range(time_q):
            ready_queue.append(process_no[i + 1])
    ready_queue.append(process_no[0])
    running_queue.append(process_no[0])



    running_queue.append(process_no[1])





    if time_q >= remaining_time[i] > 0:
        completion_time = completion_time + remaining_time[i]
        remaining_time[i] = 0
        count = 1

    elif remaining_time[i] > 0:
        remaining_time[i] = remaining_time[i] - time_q
        completion_time = completion_time + time_q

    if count == 1 and remaining_time[i] == 0:
        remain_process -= 1
        print(f"P[{i+1}] | BT : {burst_time[i]} | TAT : {completion_time - arrival_time[i]} | WT : {completion_time - arrival_time[i] - burst_time[i]}")
        total_waiting_time = total_waiting_time + completion_time - arrival_time[i] - burst_time[i]
        turnaround_time = turnaround_time + completion_time - arrival_time[i]
        count = 0

    if i == 4:
        i = 0

    elif arrival_time[i+1] <= completion_time:
        i += 1

    else:
        i = 0

total_waiting_time = total_waiting_time / 5
avg_turnaround_time = turnaround_time * 1.0 / 5
print(f"\n The Average waiting Time: {total_waiting_time} ")
print(f"\n The Average turnaround Time: {avg_turnaround_time} ")