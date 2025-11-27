## Why Do We Need CPU Scheduling?
The CPU is like the brain of your computer, but it can only do one thing at a time in most cases. When you’re running multiple programs—like a music player, a game, and a web browser—they all need the CPU to work. CPU scheduling is how the computer decides which program gets to use the CPU and when.

- **Think of it like**: A single chef in a kitchen with many orders. The chef needs a plan to decide which dish to cook first so everyone gets their food without too much waiting.
- **Why it’s important**: Scheduling keeps your computer running smoothly, makes sure programs don’t wait forever, and helps use the CPU efficiently.

## What’s Non-Preemptive vs. Preemptive?
When we talk about scheduling, we split algorithms into two types based on how they handle programs (called processes):

- **Non-Preemptive**: Once a process starts using the CPU, it keeps going until it’s done or pauses on its own (like waiting for you to type something).
  - **Example**: A customer at a store counter finishes their entire purchase before the next person steps up, even if it takes a while.
  - **Good**: Simple to manage.
  - **Bad**: Can make others wait a long time.
- **Preemptive**: The computer can pause a process to let another one use the CPU, then come back to the first one later.
  - **Example**: The store clerk helps one customer but pauses to quickly help someone with a small purchase, then returns.
  - **Good**: Fairer for urgent tasks.
  - **Bad**: Trickier to manage because of all the pausing and switching.

## FCFS Scheduling Algorithm
**First Come First Serve (FCFS)** is a simple scheduling method. It’s like a line at a ticket counter: the first process to show up gets the CPU, and it runs until it’s finished.

- **Goal**: Run processes in the order they arrive.
- **How it decides**:
  - **Arrival Time (AT)**: When a process shows up and is ready to run.
  - **Tie Breaker**: If two processes arrive at the same time, the one with the lower Process ID (like P1 before P2) goes first.
- **Type**: Non-preemptive (no interrupting a process once it starts).
- **Key terms**:
  - **Burst Time (BT)**: How long a process needs the CPU to finish.
  - **Completion Time (CT)**: When a process is done (when it finishes running).
  - **Turnaround Time (TAT)**: Time from when a process arrives to when it’s done (CT - AT).
  - **Waiting Time (WT)**: Time a process waits before running (TAT - BT).
  - **Response Time**: In FCFS, this is the same as Waiting Time (time until the process first gets the CPU).
  - **Scheduling Length**: Time from when the first process arrives to when the last one finishes.
  - **Throughput**: How many processes finish per unit of time.

### Example 1: FCFS Scheduling
Let’s walk through the first example to see how FCFS works.

#### Given Data
| Process | Arrival Time (AT) | Burst Time (BT) |
|---------|-------------------|-----------------|
| P1      | 0                 | 30              |
| P2      | 0                 | 5               |
| P3      | 0                 | 5               |

- **Ready Queue at Time = 0**: P1, P2, P3 (all arrive at time 0; P1 goes first because it has the lowest ID).
- **Order**: P1 runs first, then P2, then P3 (no interruptions since it’s non-preemptive).

#### Gantt Chart
This shows when each process runs:
```
| P1      | P2  | P3  |
0        30    35   40
```

#### Calculations
1. **Completion Time (CT)**:
   - P1: Starts at 0, runs for 30 → CT = 0 + 30 = 30.
   - P2: Starts at 30, runs for 5 → CT = 30 + 5 = 35.
   - P3: Starts at 35, runs for 5 → CT = 35 + 5 = 40.

2. **Turnaround Time (TAT)** = CT - AT:
   - P1: 30 - 0 = 30.
   - P2: 35 - 0 = 35.
   - P3: 40 - 0 = 40.

3. **Waiting Time (WT)** = TAT - BT:
   - P1: 30 - 30 = 0.
   - P2: 35 - 5 = 30.
   - P3: 40 - 5 = 35.

4. **Average TAT** = (30 + 35 + 40) / 3 = 105 / 3 = 35.
5. **Average WT** = (0 + 30 + 35) / 3 = 65 / 3 ≈ 21.67.
6. **Response Time** (same as WT in FCFS):
   - P1 = 0.
   - P2 = 30.
   - P3 = 35.
   - P4, P5, P6: Not in this example.
7. **Scheduling Length** = max(CT) - max(AT) = 40 - 0 = 40.
8. **Throughput** = 3 processes / 40 time units = 0.075 processes per unit time.

#### Solution Table
| Process | AT | BT | CT | TAT | WT | Response Time |
|---------|----|----|----|-----|----|---------------|
| P1      | 0  | 30 | 30 | 30  | 0  | 0             |
| P2      | 0  | 5  | 35 | 35  | 30 | 30            |
| P3      | 0  | 5  | 40 | 40  | 35 | 35            |

### Example 2: FCFS Scheduling
Now let’s do the second example, where processes arrive at different times.

#### Given Data
| Process | Arrival Time (AT) | Burst Time (BT) |
|---------|-------------------|-----------------|
| P1      | 0                 | 4               |
| P2      | 1                 | 2               |
| P3      | 2                 | 3               |
| P4      | 3                 | 5               |
| P5      | 4                 | 6               |
| P6      | 5                 | 1               |

- **Ready Queue**:
  - At Time = 0: P1.
  - At Time = 1: P2 (P1 is running).
  - At Time = 2: P2, P3.
  - At Time = 3: P2, P3, P4.
  - At Time = 4: P2, P3, P4, P5.
  - At Time = 5: P2, P3, P4, P5, P6.
  - But FCFS runs them in arrival order: P1, P2, P3, P4, P5, P6.

#### Gantt Chart
```
| P1  | P2 | P3 | P4 | P5  | P6 |
0     4    6   9   14   20   21
```

#### Calculations
1. **Completion Time (CT)**:
   - P1: Starts at 0, BT = 4 → CT = 0 + 4 = 4.
   - P2: Starts at 4, BT = 2 → CT = 4 + 2 = 6.
   - P3: Starts at 6, BT = 3 → CT = 6 + 3 = 9.
   - P4: Starts at 9, BT = 5 → CT = 9 + 5 = 14.
   - P5: Starts at 14, BT = 6 → CT = 14 + 6 = 20.
   - P6: Starts at 20, BT = 1 → CT = 20 + 1 = 21.

2. **Turnaround Time (TAT)** = CT - AT:
   - P1: 4 - 0 = 4.
   - P2: 6 - 1 = 5.
   - P3: 9 - 2 = 7.
   - P4: 14 - 3 = 11.
   - P5: 20 - 4 = 16.
   - P6: 21 - 5 = 16.

3. **Waiting Time (WT)** = TAT - BT:
   - P1: 4 - 4 = 0.
   - P2: 5 - 2 = 3.
   - P3: 7 - 3 = 4.
   - P4: 11 - 5 = 6.
   - P5: 16 - 6 = 10.
   - P6: 16 - 1 = 15.

4. **Average TAT** = (4 + 5 + 7 + 11 + 16 + 16) / 6 = 59 / 6 ≈ 9.83.
5. **Average WT** = (0 + 3 + 4 + 6 + 10 + 15) / 6 = 38 / 6 ≈ 6.33.
6. **Response Time** (same as WT in FCFS):
   - P1 = 0.
   - P2 = 3.
   - P3 = 4.
   - P4 = 6.
   - P5 = 10.
   - P6 = 15.
7. **Scheduling Length** = max(CT) - max(AT) = 21 - 5 = 16.
8. **Throughput** = 6 / 16 = 0.375 processes per unit time.

#### Solution Table
| Process | AT | BT | CT | TAT | WT | Response Time |
|---------|----|----|----|-----|----|---------------|
| P1      | 0  | 4  | 4  | 4   | 0  | 0             |
| P2      | 1  | 2  | 6  | 5   | 3  | 3             |
| P3      | 2  | 3  | 9  | 7   | 4  | 4             |
| P4      | 3  | 5  | 14 | 11  | 6  | 6             |
| P5      | 4  | 6  | 20 | 16  | 10 | 10            |
| P6      | 5  | 1  | 21 | 16  | 15 | 15            |

### Example 3: FCFS Scheduling
Here’s the third example for more practice.

#### Given Data
| Process | Arrival Time (AT) | Burst Time (BT) |
|---------|-------------------|-----------------|
| P1      | 4                 | 4               |
| P2      | 8                 | 2               |
| P3      | 6                 | 3               |
| P4      | 5                 | 3               |
| P5      | 2                 | 1               |
| P6      | 7                 | 7               |

- **Ready Queue**:
  - At Time = 0: Empty (no processes yet).
  - At Time = 2: P5.
  - At Time = 4: P5, P1.
  - At Time = 5: P5, P1, P4.
  - At Time = 6: P5, P1, P4, P3.
  - At Time = 7: P5, P1, P4, P3, P6.
  - At Time = 8: P5, P1, P4, P3, P6, P2.
  - Order: P5 (AT=2), P1 (AT=4), P4 (AT=5), P3 (AT=6), P6 (AT=7), P2 (AT=8).

#### Gantt Chart
```
| Idle | P5 | P1 | P4 | P3 | P6 | P2 |
0      2    3    7   10   13   20   22
```

#### Calculations
1. **Completion Time (CT)**:
   - P5: Starts at 2, BT = 1 → CT = 2 + 1 = 3.
   - P1: Starts at 3, BT = 4 → CT = 3 + 4 = 7.
   - P4: Starts at 7, BT = 3 → CT = 7 + 3 = 10.
   - P3: Starts at 10, BT = 3 → CT = 10 + 3 = 13.
   - P6: Starts at 13, BT = 7 → CT = 13 + 7 = 20.
   - P2: Starts at 20, BT = 2 → CT = 20 + 2 = 22.

2. **Turnaround Time (TAT)** = CT - AT:
   - P1: 7 - 4 = 3.
   - P2: 22 - 8 = 14.
   - P3: 13 - 6 = 7.
   - P4: 10 - 5 = 5.
   - P5: 3 - 2 = 1.
   - P6: 20 - 7 = 13.

3. **Waiting Time (WT)** = TAT - BT:
   - P1: 3 - 4 = -1 (but WT can’t be negative, so WT = 0; P1 starts right after P5).
   - P2: 14 - 2 = 12.
   - P3: 7 - 3 = 4.
   - P4: 5 - 3 = 2.
   - P5: 1 - 1 = 0.
   - P6: 13 - 7 = 6.

4. **Average TAT** = (3 + 14 + 7 + 5 + 1 + 13) / 6 = 43 / 6 ≈ 7.17.
5. **Average WT** = (0 + 12 + 4 + 2 + 0 + 6) / 6 = 24 / 6 = 4.
6. **Response Time** (same as WT in FCFS):
   - P1 = 0.
   - P2 = 12.
   - P3 = 4.
   - P4 = 2.
   - P5 = 0.
   - P6 = 6.
7. **Scheduling Length** = max(CT) - max(AT) = 22 - 8 = 14.
8. **Throughput** = 6 / 14 ≈ 0.429 processes per unit time.

#### Solution Table
| Process | AT  | BT  | CT  | TAT | WT  | Response Time |
| ------- | --- | --- | --- | --- | --- | ------------- |
| P1      | 4   | 4   | 7   | 3   | 0   | 0             |
| P2      | 8   | 2   | 22  | 14  | 12  | 12            |
| P3      | 6   | 3   | 13  | 7   | 4   | 4             |
| P4      | 5   | 3   | 10  | 5   | 2   | 2             |
| P5      | 2   | 1   | 3   | 1   | 0   | 0             |
| P6      | 7   | 7   | 20  | 13  | 6   | 6             |

## Try It Yourself
To get better at FCFS:
- Draw a Gantt chart for a new set of processes with different arrival and burst times.
- Write down the steps to calculate CT, TAT, and WT for practice.
- If you want to experiment, try this simple Python code to check your work:
```python
processes = [(1, 0, 30), (2, 0, 5), (3, 0, 5)]  # (PID, AT, BT)
queue = sorted(processes, key=lambda x: (x[1], x[0]))  # Sort by arrival time, then PID
current_time = 0
for pid, at, bt in queue:
    start = max(current_time, at)
    ct = start + bt
    print(f"P{pid}: CT={ct}, TAT={ct-at}, WT={ct-at-bt}")
    current_time = ct
```

![[Pasted image 20250725130937.png]]

---

## Additions/Removals
- **Added**: Explained CPU scheduling, non-preemptive vs. preemptive, and FCFS in simple terms with examples like a chef or ticket counter. Solved all three examples with clear steps, Gantt charts, and tables. Included a Python code snippet for practice. Kept the image placeholder as requested.
- **Removed**: Avoided technical terms like “context switching” or other algorithms to keep it beginner-friendly. Didn’t add extra examples beyond the three you provided, but I can if you ask!
- **Approach**: Used plain language, step-by-step calculations, and analogies to make FCFS easy to understand for someone new to Operating Systems.