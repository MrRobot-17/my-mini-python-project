processes_data = []
op = int(input("""Which operation do you choose?
1. First Come First Serve (FCFS)
2. Shortest Job First (SJF)
3. PRIORITY
4. Round Robin (R.R)
Input only the number of the operation: """))

burst_input = input("Input the burst time of processes split by comma : ").split(",")
burst_times = [int(x) for x in burst_input] 

for i in range(len(burst_times)):
    processes_data.append([f"P{i+1}", burst_times[i]])

print("-" * 30)

if op == 1:
    print("You chose FCFS (First Come First Serve)")
    print(f"Execution Order: {processes_data}")

elif op == 2:
    print("You chose SJF (Shortest Job First)")
    processes_data.sort(key=lambda x: x[1])
    print(f"Execution Order (ID, Time): {processes_data}")

elif op == 3:
    print("You chose PRIORITY")
    p_input = input(f"Input priorities for {len(burst_times)} processes split by comma (lower number = higher priority): ").split(",")
    priorities = [int(x) for x in p_input]
    
    for i in range(len(processes_data)):
        processes_data[i].append(priorities[i])
    
    processes_data.sort(key=lambda x: x[2])
    
    print("Process Execution Order based on Priority:")
    print("Format: [ID, Burst Time, Priority]")
    for p in processes_data:
        print(f"Process {p[0]} (Priority: {p[2]})")

elif op == 4:
    print("You chose R.R (Round Robin)")
    quantum = int(input("Input the Time Quantum (Q): "))
    
    remaining_time = burst_times.copy() 
    t = 0 
    done = False
    
    print(f"\nExecution Log (Quantum = {quantum}):")
    while not done:
        done = True
        for i in range(len(burst_times)):
            if remaining_time[i] > 0:
                done = False 
                
                if remaining_time[i] > quantum:
                    t += quantum
                    remaining_time[i] -= quantum
                    print(f"Time {t}: Process P{i+1} runs for {quantum}s (Remaining: {remaining_time[i]})")
                else:
                    t = t + remaining_time[i]
                    print(f"Time {t}: Process P{i+1} runs for {remaining_time[i]}s and FINISHES.")
                    remaining_time[i] = 0
    
    print(f"\nAll processes finished at Time = {t}")

else:
    print("Invalid Selection")