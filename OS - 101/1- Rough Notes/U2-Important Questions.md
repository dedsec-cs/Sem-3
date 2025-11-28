# ⚙️ Operating Systems: Unit 2 Questions Arrangement

## 1. 📂 Core Process Concepts & Structure

This section covers the fundamental components and lifecycle of a process within the Operating System.

* **Question 4:** Describe the various states in a **Process Control Block (PCB)**.
* **Question 7:** Explain the structure of a **Linux process management system**.
* **Question 22:** Describe the **Process Transition Diagram** with a labeled diagram. 


---

## 2. ⏱️ CPU Scheduling: Theory & Comparison

This section addresses the theoretical foundation of scheduling, different queue types, and conceptual comparisons between algorithms.

* **Question 8:** Discuss the different types of **process scheduling queues**.
* **Question 2:** Difference between **Multilevel Queue** and **Multilevel Feedback Queue Scheduling**.
* **Question 3:** Explain **Round Robin Scheduling** with an example.
* **Question 5:** Explain the concept of **starvation** in scheduling and methods to handle it.
* **Question 6:** Compare and contrast **SJF** and **Round Robin scheduling** with examples.

---

## 3. 📈 CPU Scheduling: Calculation Problems

This large section focuses on calculating performance metrics (CT, TAT, WT, AWT, ATAT) for specific algorithms.

### 3.1. First-Come, First-Served (FCFS)

* **Question 9:** Consider the following set of processes with their respective arrival times (AT) and burst times (BT), scheduled using the **First-Come, First-Served (FCFS) algorithm**... Calculate: The completion time (CT) for each process, the average waiting time (AWT), and the average turnaround time (TAT). Show your calculations.
* **Question 10:** Consider the following set of processes... The scheduling follows the **First-Come, First-Served (FCFS) algorithm**. Tasks: Construct a **Gantt Chart**, Calculate the Completion Time (CT), Determine the Turnaround Time (TAT) and Waiting Time (WT), Compute the Average Waiting Time (AWT) and Average Turnaround Time (ATAT), and Interpret the results.
* **Question 11:** Using **FCFS**, calculate for each process: Completion Time (CT), Turnaround Time $(\text{TAT} = \text{CT} - \text{AT})$, and Waiting Time $(\text{WT} = \text{TAT} - \text{BT})$. Also calculate: ATAT, AWT, ACT.
* **Question 18:** Solve for the average waiting time and turnaround time using the **First Come First Serve (FCFS) algorithm** for the following processes:

### 3.2. Shortest Job First (SJF) & Shortest Remaining Time First (SRTF)

* **Question 12:** Use **SJF (non-preemptive)** to calculate for each process: CT, TAT, WT. Also calculate: ATAT, AWT, ACT.
* **Question 19:** Compute the average turnaround time using the **Shortest Job First (SJF) non-preemptive algorithm** for these processes:
* **Question 14:** Use **Preemptive SJF (SRTF)** to calculate CT, TAT, WT, ATAT, AWT, ACT.
* **Question 20:** Analyze the response time and waiting time using **Shortest Remaining Time First (SRTF)** for the given dataset:

### 3.3. Round Robin (RR)

* **Question 1:** Use the **Round Robin scheduling algorithm** to schedule five processes and compute the turnaround time.
* **Question 13:** Time Quantum: 3 milliseconds. Draw the **Gantt Chart**, then compute: CT, TAT, WT, Averages (ATAT, AWT, ACT).
* **Question 16:** Time Quantum: 2 milliseconds. Task: Draw the **Gantt Chart** and compute CT, TAT, WT, ATAT, AWT, ACT.

### 3.4. Priority Scheduling

* **Question 15:** **Note: Lower number = higher priority**. Task: Schedule the processes using **non-preemptive priority scheduling**. Calculate CT, TAT, WT, ATAT, AWT, ACT.
* **Question 17:** Consider the set of 5 processes... If the CPU scheduling policy is **priority non-preemptive** (Higher number represents higher priority), calculate the average waiting time and average turnaround time.
* **Question 21:** Derive the execution order and CPU utilization using **preemptive priority scheduling** where lower numbers indicate higher priority:

