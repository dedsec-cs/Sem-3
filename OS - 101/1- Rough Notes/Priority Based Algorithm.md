# Priority Based Scheduling

## Why HRRN Loses the Burst Time Problem

- HRRN needs burst times to calculate response ratios, but burst times are often unknown in real systems (e.g., user-dependent programs).
- Priority-based scheduling uses a priority value instead, avoiding the need for burst time predictions.

## Priority Based Scheduling

- **Objective**: Run the most important processes first based on assigned priority.
- **Criteria**: Highest priority (higher number = higher priority, unless specified).
- **Tie Breaker**: FCFS (earliest arrival time).
- **Types**:
    - **Non-Preemptive**: Process runs to completion once started.
    - **Preemptive**: Process can be paused for a higher-priority process.
- **Analogy**: A hospital treats the most urgent patients first, pausing less urgent ones in preemptive mode.

## Types of Priority

1. **Static Priority**:
    - Fixed priority, doesn’t change.
    - Example: System update (priority 5) always beats file backup (priority 2).
    - Use: Systems with clear, constant priorities (e.g., car’s braking system).
2. **Dynamic Priority**:
    - Priority changes based on waiting time or system needs.
    - Example: Priority increases the longer a process waits.
    - Use: Systems needing fairness, like user apps.

## Advantages Over HRRN

- No need for burst times, more practical.
- Flexible for critical tasks or fairness.
- **Downside**: Low-priority processes may starve without dynamic adjustments.

**Note**: Priorities will be provided in questions, not assumed.

---
# Priority Based Scheduling Examples

## Review of Priority Based Scheduling
Priority-based scheduling runs the process with the **highest priority** (higher number = higher priority, as given). It’s like a hospital triage where the most urgent patient (highest priority) is treated first. 
- **Criteria**: Highest priority.
- **Tie Breaker**: FCFS (earliest arrival time).
- **Types**:
  - **Non-Preemptive**: Once a process starts, it finishes (like treating a patient fully before moving to the next).
  - **Preemptive**: A higher-priority process can interrupt the current one (like pausing a checkup for an emergency).
- **Note**: Priorities are provided (e.g., P4: 10, highest). Response time = waiting time in non-preemptive; can be less in preemptive.

## Example 1: Non-Preemptive Priority Scheduling
#### Given Data
| Process | Arrival Time (AT) | Burst Time (BT) | Priority |
|---------|-------------------|-----------------|----------|
| P1      | 0                 | 4               | 4        |
| P2      | 1                 | 2               | 5        |
| P3      | 2                 | 3               | 6        |
| P4      | 3                 | 1               | 10       |
| P5      | 4                 | 2               | 9        |
| P6      | 5                 | 6               | 7        |

### Step-by-Step Non-Preemptive Scheduling
- **Ready Queue**:
  - Time = 0: P1 (Priority=4). Run P1 (only process).
  - Time = 4: P1 finishes. P2 (P=5, AT=1), P3 (P=6, AT=2), P4 (P=10, AT=3), P5 (P=9, AT=4). Run P4 (highest priority, 10).
  - Time = 5: P4 finishes. P2 (P=5), P3 (P=6), P5 (P=9), P6 (P=7, AT=5). Run P5 (priority 9).
  - Time = 7: P5 finishes. P2 (P=5), P3 (P=6), P6 (P=7). Run P6 (priority 7).
  - Time = 13: P6 finishes. P2 (P=5), P3 (P=6). Run P3 (priority 6).
  - Time = 16: P3 finishes. P2 (P=5). Run P2.

- **Order**: P1 (0-4), P4 (4-5), P5 (5-7), P6 (7-13), P3 (13-16), P2 (16-18).

#### Gantt Chart
```
| P1 | P4 | P5 | P6  | P3 | P2 |
0    4    5    7    13   16   18
```

#### Calculations
1. **Completion Time (CT)**:
   - P1: Finishes at 4 → CT = 4.
   - P2: Finishes at 18 → CT = 18.
   - P3: Finishes at 16 → CT = 16.
   - P4: Finishes at 5 → CT = 5.
   - P5: Finishes at 7 → CT = 7.
   - P6: Finishes at 13 → CT = 13.

2. **Turnaround Time (TAT)** = CT - AT:
   - P1: 4 - 0 = 4.
   - P2: 18 - 1 = 17.
   - P3: 16 - 2 = 14.
   - P4: 5 - 3 = 2.
   - P5: 7 - 4 = 3.
   - P6: 13 - 5 = 8.

3. **Waiting Time (WT)** = TAT - BT:
   - P1: 4 - 4 = 0.
   - P2: 17 - 2 = 15.
   - P3: 14 - 3 = 11.
   - P4: 2 - 1 = 1.
   - P5: 3 - 2 = 1.
   - P6: 8 - 6 = 2.

4. **Average TAT** = (4 + 17 + 14 + 2 + 3 + 8) / 6 = 48 / 6 = 8.
5. **Average WT** = (0 + 15 + 11 + 1 + 1 + 2) / 6 = 30 / 6 = 5.
6. **Response Time** (same as WT in non-preemptive):
   - P1: 0.
   - P2: 15.
   - P3: 11.
   - P4: 1.
   - P5: 1.
   - P6: 2.
7. **Scheduling Length** = max(CT) - max(AT) = 18 - 5 = 13.
8. **Throughput** = 6 / 13 ≈ 0.462 processes per unit time.

#### Solution Table
| Process | AT  | BT  | Priority | CT  | TAT | WT  | Response Time |
| ------- | --- | --- | -------- | --- | --- | --- | ------------- |
| P1      | 0   | 4   | 4        | 4   | 4   | 0   | 0             |
| P2      | 1   | 2   | 5        | 18  | 17  | 15  | 15            |
| P3      | 2   | 3   | 6        | 16  | 14  | 11  | 11            |
| P4      | 3   | 1   | 10       | 5   | 2   | 1   | 1             |
| P5      | 4   | 2   | 9        | 7   | 3   | 1   | 1             |
| P6      | 5   | 6   | 7        | 13  | 8   | 2   | 2             |

## Example 2: Preemptive Priority Scheduling
#### Given Data
(Same as Example 1, but preemptive: higher-priority processes can interrupt.)

| Process | Arrival Time (AT) | Burst Time (BT) | Priority |
|---------|-------------------|-----------------|----------|
| P1      | 0                 | 4               | 4        |
| P2      | 1                 | 2               | 5        |
| P3      | 2                 | 3               | 6        |
| P4      | 3                 | 1               | 10       |
| P5      | 4                 | 2               | 9        |
| P6      | 5                 | 6               | 7        |

### Step-by-Step Preemptive Scheduling
- **Ready Queue**:
  - Time = 0: P1 (P=4). Run P1.
  - Time = 1: P1 (P=4, remaining=3), P2 (P=5). Pause P1, run P2.
  - Time = 2: P1 (P=4, remaining=3), P2 (P=5, remaining=1), P3 (P=6). Pause P2, run P3.
  - Time = 3: P1 (P=4, remaining=3), P2 (P=5, remaining=1), P3 (P=6, remaining=2), P4 (P=10). Pause P3, run P4.
  - Time = 4: P1 (P=4, remaining=3), P2 (P=5, remaining=1), P3 (P=6, remaining=2), P5 (P=9). Run P5 (highest priority).
  - Time = 5: P1 (P=4, remaining=3), P2 (P=5, remaining=1), P3 (P=6, remaining=2), P5 (P=9, remaining=1), P6 (P=7). Run P6 (priority 7).
  - Time = 6: P1 (P=4, remaining=3), P2 (P=5, remaining=1), P3 (P=6, remaining=2), P5 (P=9, remaining=1). Run P5.
  - Time = 7: P1 (P=4, remaining=3), P2 (P=5, remaining=1), P3 (P=6, remaining=2). Run P3.
  - Time = 9: P1 (P=4, remaining=3), P2 (P=5, remaining=1). Run P2.
  - Time = 10: P1 (P=4, remaining=3). Run P1.

- **Order**: P1 (0-1), P2 (1-2), P3 (2-3), P4 (3-4), P5 (4-5), P6 (5-6), P5 (6-7), P3 (7-9), P2 (9-10), P1 (10-13).

#### Gantt Chart
```
| P1 | P2 | P3 | P4 | P5 | P6 | P5 | P3 | P2 | P1 |
0    1    2    3    4    5    6    7    9    10   13
```

#### Calculations
1. **Completion Time (CT)**:
   - P1: Finishes at 13 (1 unit at 0-1, 3 units at 10-13) → CT = 13.
   - P2: Finishes at 10 (1 unit at 1-2, 1 unit at 9-10) → CT = 10.
   - P3: Finishes at 9 (1 unit at 2-3, 2 units at 7-9) → CT = 9.
   - P4: Finishes at 4 → CT = 4.
   - P5: Finishes at 7 (1 unit at 4-5, 1 unit at 6-7) → CT = 7.
   - P6: Finishes at 6 → CT = 6.

2. **Turnaround Time (TAT)** = CT - AT:
   - P1: 13 - 0 = 13.
   - P2: 10 - 1 = 9.
   - P3: 9 - 2 = 7.
   - P4: 4 - 3 = 1.
   - P5: 7 - 4 = 3.
   - P6: 6 - 5 = 1.

3. **Waiting Time (WT)** = TAT - BT:
   - P1: 13 - 4 = 9.
   - P2: 9 - 2 = 7.
   - P3: 7 - 3 = 4.
   - P4: 1 - 1 = 0.
   - P5: 3 - 2 = 1.
   - P6: 1 - 6 = -5 (WT = 0, no negative).

4. **Average TAT** = (13 + 9 + 7 + 1 + 3 + 1) / 6 = 34 / 6 ≈ 5.67.
5. **Average WT** = (9 + 7 + 4 + 0 + 1 + 0) / 6 = 21 / 6 = 3.5.
6. **Response Time** (time to first CPU use):
   - P1: Runs at 0 → 0 - 0 = 0.
   - P2: Runs at 1 → 1 - 1 = 0.
   - P3: Runs at 2 → 2 - 2 = 0.
   - P4: Runs at 3 → 3 - 3 = 0.
   - P5: Runs at 4 → 4 - 4 = 0.
   - P6: Runs at 5 → 5 - 5 = 0.
7. **Scheduling Length** = max(CT) - max(AT) = 13 - 5 = 8.
8. **Throughput** = 6 / 8 = 0.75 processes per unit time.

#### Solution Table
| Process | AT | BT | Priority | CT | TAT | WT | Response Time |
|---------|----|----|----------|----|-----|----|---------------|
| P1      | 0  | 4  | 4        | 13 | 13  | 9  | 0             |
| P2      | 1  | 2  | 5        | 10 | 9   | 7  | 0             |
| P3      | 2  | 3  | 6        | 9  | 7   | 4  | 0             |
| P4      | 3  | 1  | 10       | 4  | 1   | 0  | 0             |
| P5      | 4  | 2  | 9        | 7  | 3   | 1  | 0             |
| P6      | 5  | 6  | 7        | 6  | 1   | 0  | 0             |

**Comparison**:
- **Non-Preemptive**: Average WT = 5, longer waits for low-priority processes (e.g., P2: 15).
- **Preemptive**: Average WT = 3.5, shorter waits due to interruptions for high-priority processes (e.g., P4, P5 run early).

## Try It Yourself
- Create new processes with priorities and track the ready queue.
- For preemptive, check for higher-priority arrivals at each time unit.
- Use this Python code to verify:
```python
# Non-Preemptive
processes = [(1, 0, 4, 4), (2, 1, 2, 5), (3, 2, 3, 6), (4, 3, 1, 10), (5, 4, 2, 9), (6, 5, 6, 7)]
ready = []
current_time = 0
completed = {}
while processes or ready:
    ready.extend([p for p in processes if p[1] <= current_time])
    processes = [p for p in processes if p[1] > current_time]
    if ready:
        ready.sort(key=lambda x: (-x[3], x[1]))  # Highest priority, then FCFS
        current = ready.pop(0)
        pid, at, bt, _ = current
        current_time += bt
        completed[pid] = current_time
    else:
        current_time += 1
for pid in completed:
    ct = completed[pid]
    at, bt = next(p[1:3] for p in processes if p[0] == pid)
    print(f"P{pid}: CT={ct}, TAT={ct-at}, WT={ct-at-bt}")
```

![[Pasted image 20250725130937.png]]

# Priority Based Scheduling Examples

## Example 1: Non-Preemptive

|Process|AT|BT|Priority|CT|TAT|WT|Response Time|
|---|---|---|---|---|---|---|---|
|P1|0|4|4|4|4|0|0|
|P2|1|2|5|18|17|15|15|
|P3|2|3|6|16|14|11|11|
|P4|3|1|10|5|2|1|1|
|P5|4|2|9|7|3|1|1|
|P6|5|6|7|13|8|2|2|

- **Gantt Chart**: `| P1 | P4 | P5 | P6 | P3 | P2 | 0 4 5 7 13 16 18`
- **Average TAT**: 8, **Average WT**: 5, **Scheduling Length**: 18 - 5 = 13, **Throughput**: 6/13 ≈ 0.462.

## Example 2: Preemptive

|Process|AT|BT|Priority|CT|TAT|WT|Response Time|
|---|---|---|---|---|---|---|---|
|P1|0|4|4|13|13|9|0|
|P2|1|2|5|10|9|7|0|
|P3|2|3|6|9|7|4|0|
|P4|3|1|10|4|1|0|0|
|P5|4|2|9|7|3|1|0|
|P6|5|6|7|6|1|0|0|

- **Gantt Chart**: `| P1 | P2 | P3 | P4 | P5 | P6 | P5 | P3 | P2 | P1 | 0 1 2 3 4 5 6 7 9 10 13`
- **Average TAT**: 5.67, **Average WT**: 3.5, **Scheduling Length**: 13 - 5 = 8, **Throughput**: 6/8 = 0.75.



---
# Starvation

If Higher Priority Processes Keep Arriving Then Low Priority Processes May Wait Till Indefinite Time.

Solution Of Starvation:-
- Aging 
	After A Predefined Time Period Increase Priority Of All Waiting Processes By 1.
	This Is Only Applicable For Dynamic Priority System

