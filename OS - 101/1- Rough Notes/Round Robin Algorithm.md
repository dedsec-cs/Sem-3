## Reason Behind Using This Scheduling Algorithm

The primary motivation for using the Round Robin (RR) algorithm is to achieve **responsiveness** and **fairness** in a multi-tasking environment.

- **Responsiveness (Interactiveness):** In modern computing, users interact with many programs at once (e.g., browsing the web, typing a document, listening to music). If one program were allowed to run for a long time, the others would freeze, and the system would feel sluggish. RR rapidly switches the CPU between these processes, ensuring that every program receives processing time quickly. This makes the system seem instantly responsive to user inputs, which is crucial for **interactive** applications.
    
- **Fairness:** RR ensures that no single process can hog the CPU. Every process is guaranteed to get a slice of the CPU's time within a specific, short interval. This prevents **starvation**, a condition where a low-priority or long process might never get to run.
    

---

## Scheduling Algorithm: Round Robin (RR)

Round Robin is one of the oldest, simplest, and most commonly used CPU scheduling algorithms, specifically designed for **time-sharing systems**.

### Objective: Provides Interactiveness, Fairness

|**Objective**|**Detailed Explanation**|
|---|---|
|**Interactiveness**|The main goal is to minimize the **response time** for all processes. By rapidly cycling the CPU, the time from when a user performs an action (like a mouse click) to when the computer responds is kept very short.|
|**Fairness**|Every process, regardless of its size or priority, is treated equally and given an equivalent opportunity to run on the CPU. This is guaranteed by the fixed time slice mechanism.|

### $Q = \text{Time Quantum}$

The **Time Quantum ($Q$)** is the central concept of the RR algorithm.

- **Definition:** It is a **small, fixed unit of time** (typically $10$ to $100$ milliseconds) that represents the maximum amount of time a process can continuously run on the CPU before being interrupted.
    
- **Role:** When a process starts executing, a timer is set to $Q$.
    
    - If the process finishes its work **before** the timer expires, it voluntarily gives up the CPU.
        
    - If the timer expires **before** the process finishes, the process is forcefully interrupted (preempted) and moved to the back of the queue, allowing the next process to run.
        
- **Impact of $Q$ Selection:**
    
    - **Large $Q$:** If $Q$ is very large (approaches infinity), RR degenerates into the **First-Come, First-Served (FCFS)** algorithm. Fairness and responsiveness suffer.
        
    - **Small $Q$:** If $Q$ is extremely small, the system spends too much time performing **context switches** (the overhead of saving one process's state and loading another's), which wastes CPU time and reduces overall efficiency.
        
    - **Optimal $Q$:** The Time Quantum must be selected as a reasonable compromise to minimize context switching overhead while still ensuring good system responsiveness.
        

### Type: Preemptive

RR is a **preemptive** scheduling algorithm.

- **Preemption:** The ability of the operating system to forcefully stop a currently running process and switch the CPU to another process, even if the running process has not finished its task.
    
- **Mechanism:** In RR, preemption occurs specifically when the **Time Quantum ($Q$) expires**. This ensures that even a very long process cannot indefinitely occupy the CPU, forcing it to relinquish control after its allotted time slice.
    

### Criteria: Arrival Time + Time Quantum

The Round Robin algorithm uses a combination of these two criteria for its operation:

1. **Arrival Time (For Initial Ordering):** Processes are initially placed in the **Ready Queue** in the order they arrive in the system (**First-Come, First-Served**).
    
    - _Analogy:_ Imagine people waiting in line for a ride. The people who got in line first are at the front.
        
2. **Time Quantum (For Reordering):** Once a process is selected from the front of the queue, it runs for exactly $Q$ time units.
    
    - After the time quantum expires, the process (if not finished) is **preempted** and sent to the **end** of the Ready Queue.
        
    - _Analogy:_ The person at the front gets on the ride for a short, set time. When their time is up, they have to get off and go to the very back of the line to wait their turn again.
        

### Tie Breaker: Process ID

A **tie breaker** is necessary when multiple processes meet the primary criteria (arrival time) at the exact same moment.

- **Scenario:** If Process A and Process B both arrive at time $t=0$ (simultaneous arrival), a tie-breaker is needed to decide which one is placed at the very front of the Ready Queue.
    
- **Tie Breaker Mechanism:** The **Process ID (PID)** is a unique, typically numerical identifier assigned to every process. The scheduler will choose the process with the **lowest** (or sometimes highest, depending on the system design) Process ID to go first. This ensures a deterministic and consistent ordering when a tie occurs.

---
## Example 1: Simultaneous Arrival

**Time Quantum ($Q$) = $2$**

|**Process**|**Arrival Time (AT)**|**Burst Time (BT)**|
|---|---|---|
|P1|0|3|
|P2|0|6|
|P3|0|4|
|P4|0|5|

Since all processes arrive at $t=0$, the initial Ready Queue (RQ) is determined by the **Process ID (PID) Tie Breaker**: $\text{RQ} = [\text{P1}, \text{P2}, \text{P3}, \text{P4}]$.

### Execution Trace (Remaining Burst Time)

|**Process**|**BT**|**Cycle 1 (Run 2)**|**Cycle 2**|**Cycle 3**|**Status**|
|---|---|---|---|---|---|
|P1|3|$3-2=1$|$1-1=\mathbf{0}$|N/A|Completed at $\mathbf{9}$|
|P2|6|$6-2=4$|$4-2=2$|$2-2=\mathbf{0}$|Completed at $\mathbf{17}$|
|P3|4|$4-2=2$|$2-2=\mathbf{0}$|N/A|Completed at $\mathbf{13}$|
|P4|5|$5-2=3$|$3-2=1$|$1-1=\mathbf{0}$|Completed at $\mathbf{18}$|

### Gantt Chart (Total Time: 18)

| **P1**       | **P2** | **P3** | **P4** | **P1** | **P2** | **P3** | **P4** | **P2** | **P4** |
| ------------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| $\mathbf{0}$ | $2$    | $4$    | $6$    | $8$    | $9$    | $11$   | $13$   | $15$   | $17$   |

How Many Context Switches Happened In This?

A context switch occurs whenever the CPU switches processes. This happens at every time point except the start (0) and end (18).

Answer: 9 Context Switches

### Performance Metrics

|**Process**|**Arrival Time (AT)**|**Burst Time (BT)**|**Completion Time (CT)**|**Turn Around Time (TAT) (CT - AT)**|**Waiting Time (WT) (TAT - BT)**|
|---|---|---|---|---|---|
|**P1**|0|3|$\mathbf{9}$|$9 - 0 = \mathbf{9}$|$9 - 3 = \mathbf{6}$|
|**P2**|0|6|$\mathbf{17}$|$17 - 0 = \mathbf{17}$|$17 - 6 = \mathbf{11}$|
|**P3**|0|4|$\mathbf{13}$|$13 - 0 = \mathbf{13}$|$13 - 4 = \mathbf{9}$|
|**P4**|0|5|$\mathbf{18}$|$18 - 0 = \mathbf{18}$|$18 - 5 = \mathbf{13}$|
|**Total**||**18**||$\mathbf{57}$|$\mathbf{39}$|

- **Calculations For**
    
    - **Average TAT** ($\frac{\text{Total TAT}}{\text{No. of Processes}}$): $\frac{57}{4} = \mathbf{14.25}$ units
        
    - **Average WT** ($\frac{\text{Total WT}}{\text{No. of Processes}}$): $\frac{39}{4} = \mathbf{9.75}$ units
        
    - **Response Time** ($\text{First Start Time} - \text{AT}$):
        
        - P1 = $0 - 0 = \mathbf{0}$
            
        - P2 = $2 - 0 = \mathbf{2}$
            
        - P3 = $4 - 0 = \mathbf{4}$
            
        - P4 = $6 - 0 = \mathbf{6}$
            
    - **Calculating Scheduling Length** ($\max(\text{CT}) - \min(\text{AT})$): $18 - 0 = \mathbf{18}$ units
        
    - **Throughput** ($\frac{\text{No. of Process}}{\text{Unit Time}}$): $\frac{4}{18} \approx \mathbf{0.222}$ processes/unit time
        

---

## Solved Example 2: Non-Simultaneous Arrival

**Time Quantum ($Q$) = $2$**

|**Process**|**Arrival Time (AT)**|**Burst Time (BT)**|
|---|---|---|
|P1|0|4|
|P2|1|5|
|P3|2|6|
|P4|3|3|
|P5|4|2|
|P6|5|4|

### Execution Trace: Ready Queue Flow

1. **t=0:** P1 runs ($0 \to 2$). P2 arrives at $t=1$. $\text{RQ}=[\text{P2}]$. P1 is preempted (remaining $BT=2$), moves to the end. $\text{RQ}=[\text{P2}, \text{P1}]$.
    
2. **t=2:** P2 runs ($2 \to 4$). P3 arrives at $t=2$. $\text{RQ}=[\text{P1}, \text{P3}]$. P2 is preempted (remaining $BT=3$), moves to the end. $\text{RQ}=[\text{P1}, \text{P3}, \text{P2}]$.
    
3. **t=4:** P3 runs ($4 \to 6$). P4 arrives at $t=3$, P5 arrives at $t=4$. $\text{RQ}=[\text{P3}, \text{P4}, \text{P2}, \text{P1}]$. P3 is preempted (remaining $BT=4$), moves to the end. $\text{RQ}=[\text{P1}, \text{P4}, \text{P5}, \text{P2}, \text{P3}]$.
    
4. **t=6:** P1 runs ($6 \to 8$). P6 arrives at $t=5$. $\text{RQ}=[\text{P4}, \text{P5}, \text{P2}, \text{P3}, \text{P6}]$. P1 finishes (remaining $BT=0$). $\text{RQ}=[\text{P4}, \text{P5}, \text{P2}, \text{P3}, \text{P6}]$.
    
5. ...and so on, until all processes are complete.
    

### Gantt Chart (Total Time: 24)

|**P1**|**P2**|**P3**|**P1**|**P4**|**P5**|**P2**|**P6**|**P3**|**P4**|**P2**|**P6**|**P3**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|$\mathbf{0}$|$2$|$4$|$6$|$8$|$10$|$12$|$14$|$16$|$18$|$19$|$20$|$22$|

### Performance Metrics

|**Process**|**AT**|**BT**|**Completion Time (CT)**|**Turn Around Time (TAT)**|**Waiting Time (WT)**|**Response Time (RT)**|
|---|---|---|---|---|---|---|
|**P1**|0|4|$\mathbf{8}$|$8 - 0 = \mathbf{8}$|$8 - 4 = \mathbf{4}$|$0 - 0 = \mathbf{0}$|
|**P2**|1|5|$\mathbf{20}$|$20 - 1 = \mathbf{19}$|$19 - 5 = \mathbf{14}$|$2 - 1 = \mathbf{1}$|
|**P3**|2|6|$\mathbf{24}$|$24 - 2 = \mathbf{22}$|$22 - 6 = \mathbf{16}$|$4 - 2 = \mathbf{2}$|
|**P4**|3|3|$\mathbf{19}$|$19 - 3 = \mathbf{16}$|$16 - 3 = \mathbf{13}$|$8 - 3 = \mathbf{5}$|
|**P5**|4|2|$\mathbf{12}$|$12 - 4 = \mathbf{8}$|$8 - 2 = \mathbf{6}$|$10 - 4 = \mathbf{6}$|
|**P6**|5|4|$\mathbf{22}$|$22 - 5 = \mathbf{17}$|$17 - 4 = \mathbf{13}$|$14 - 5 = \mathbf{9}$|
|**Total**||**24**||$\mathbf{90}$|$\mathbf{66}$|$\mathbf{23}$|

|**Calculation**|**Result**|
|---|---|
|**Average TAT**|$\frac{90}{6} = \mathbf{15.0}$ units|
|**Average WT**|$\frac{66}{6} = \mathbf{11.0}$ units|
|**Response Times**|P1: 0, P2: 1, P3: 2, P4: 5, P5: 6, P6: 9|
|**Calculating Scheduling Length**|$24 - 0 = \mathbf{24}$ units|
|**Throughput**|$\frac{6}{24} = \mathbf{0.25}$ processes/unit time|

## What Should Be The Quantum Value ($Q$)?

The ideal value for the Time Quantum ($Q$) is a **small but not too small** number, typically chosen to be slightly larger than the average context switch time. This choice is a crucial trade-off between **CPU Efficiency (throughput)** and **System Responsiveness (interactiveness)**.

### Analysis of $Q$ Value

| **Quantum Value (Q)**     | **Effect on CPU Time**            | **Effect on Scheduling Algorithm**  | **Resulting System Characteristic**                                                                            |
| ------------------------- | --------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Very Very Small**       | **CPU Efficiency Is Very Low** 📉 | High **Context Switching Overhead** | CPU spends more time switching between processes than executing them. **Very poor throughput.**                |
| **Small** (Optimal Range) | CPU Efficiency is good            | Balanced Preemption and Execution   | **Highly Interactive.** Provides excellent response time while maintaining reasonable CPU utilization.         |
| **Large**                 | CPU Efficiency is High            | Less Frequent Preemption            | **Less Interactive.** Users might experience noticeable delays as a single process runs for a longer duration. |
| **Very Very Large**       | CPU Efficiency is High            | Preemption is almost non-existent   | **Round Robin Will Become FCFS** (First-Come, First-Served). Fairness and interactiveness are lost.            |

### The Optimal $Q$

The goal is to select $Q$ such that:

$$\text{Context Switch Time} \ll Q \ll \text{Average Burst Time}$$

This ensures that:

1. **$Q$ is much greater than the context switch time** (to keep efficiency high).
    
2. **$Q$ is much smaller than the average process run time** (to keep the system interactive).
    

If most processes can finish within $Q$ (i.e., $Q$ is greater than $80\%$ of all burst times), the system essentially becomes FCFS with unnecessary context switches for the long-running processes. Therefore, $Q$ must be small enough to force preemption on large tasks, guaranteeing fairness.

---

## Advantages Of Round Robin

Round Robin is the most suitable algorithm for modern time-sharing operating systems due to the following key advantages:

1. **Fairness (Starvation-Free) ⚖️:**
    
    - Every process in the Ready Queue is **guaranteed** to receive a turn on the CPU within a predictable, bounded time.
        
    - This prevents **starvation**, where a process might wait indefinitely for CPU time, regardless of its priority or length.
        
2. **Interactiveness for Time-Sharing Systems :**
    
    - Its primary benefit is minimizing the **response time** for all running applications.
        
    - By frequently rotating the CPU, the system gives the _illusion_ that all programs are running simultaneously, which is essential for user experience in interactive systems (e.g., desktops, web servers).
        
3. **No Prior Knowledge of Burst Time Required:**
    
    - Unlike algorithms like Shortest Job First (SJF) or Shortest Remaining Time First (SRTF), RR does **not** need to know the **Burst Time (BT)** of a process in advance.
        
    - It treats every process equally, only requiring the simple $Q$ parameter, making it easy to implement and robust in diverse computing environments.