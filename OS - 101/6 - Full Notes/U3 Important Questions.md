## Unit 3 Questions 🛡️

1.  Discuss **RAG** and give example of **wait-for graph (WFG)**.
2.  Explain any two **deadlock handling methods** in detail.
3.  Discuss the **classical problems of synchronization** in detail.
4.  Discuss the **atomic operations of semaphore** and show how **mutual exclusion** can be implemented.
5.  Discuss the process of **deadlock detection** and also explain various approach we follow to **avoid deadlock detection** in detail.
6.  Discuss about **Peterson solution** for the critical section problem in detail.
7.  Describe **Lamport Bakery Solution** to the critical section problem.
8.  Discuss **Sleeping Barber problem** in detail.
9.  Elaborate the **reader-writer problem** in detail.
10. Elaborate **Race Condition** and how synchronization helps in concurrent programming.
11. Write a short note on **Interprocess communication** with its advantages and disadvantages.
12. Show how **mutual exclusion** can be implemented and give example of **synchronization hardware** using **Test and Set** operation.
13. Describe the **Bounded - buffer problem** and give a solution for the same using **semaphores**.
14. Write code for **Dining Philosopher problem** and discuss the approaches for reducing deadlock condition.
15. Discuss in detail the **critical section problem** and also write the algorithm for **Readers/Writers Problem** with semaphores.
16. Mention five real life examples of **deadlock situation** and also suggest the solution of mentioned problems.
17. Describe **Banker's algorithm** with an example.

---

### Numerical/Advanced Problems

18. Assume a system with four resource types R1, R2, R3 and R4 with these many units (6,4,4,2), respectively, and the maximum claim on resources and the current allocation given below. Is this state safe? Explain.
* **Maximum Request**

| Process | R1  | R2  | R3  | R4  |
| :-----: | :-: | :-: | :-: | :-: |
|   P1    |  3  |  2  |  1  |  1  |
|   P2    |  1  |  2  |  0  |  2  |
|   P3    |  1  |  1  |  2  |  0  |
|   P4    |  3  |  2  |  1  |  0  |
|   P5    |  2  |  1  |  0  |  1  |

* **Current Allocation**

| Process | R1  | R2  | R3  | R4  |
| :-----: | :-: | :-: | :-: | :-: |
|   P1    |  2  |  0  |  1  |  1  |
|   P2    |  1  |  1  |  0  |  0  |
|   P3    |  1  |  1  |  0  |  0  |
|   P4    |  1  |  0  |  1  |  0  |
|   P5    |  0  |  1  |  0  |  1  |
19. If we ran processes sequentially, would we ever have deadlocks in the system? Justify your answer.
20. In a **uniprocessor system**, can the system ever enter into a **deadlock**? Justify your answer.
21. A club has a lounge where the members can sit and chat. Members include both smokers and non-smokers. Smokers can smoke in the lounge when non-smokers are absent. Devise a protocol for the lounge.
    * A smoker calls $\text{enterLounge(true)}$ to enter the lounge (the flag true indicates that she is a smoker), then calls $\text{smoke()}$, and finally calls $\text{leaveLounge(true)}$ to leave.
    * A non-smoker calls $\text{enterLounge(false)}$ to enter, then sits in the lounge, and finally calls $\text{leaveLounge(false)}$ to leave the lounge.
    * Using **semaphores**, write a code for the functions noted above so that smoking rules are obeyed.
    * Name and describe three desirable properties that any synchronization algorithm should possess. Explain briefly whether your solution satisfies each property.
22. Consider a traffic crossing between two roads, one in the east-west direction and the other in the north-south direction.
    * Suppose the crossing is modelled as a shared data structure, and cars are modelled as processes that access the crossing in order to pass through it.
    * Assume that cars only travel straight, without turning left or right.
    * Two or more cars that are allowed to simultaneously pass through the crossing only if they are headed in the same or opposite directions (e.g., a north-bound and south-bound car), but east-west traffic and north-south traffic can never access the crossings simultaneously.
    * Devise a **synchronization solution** for the cars using **semaphores**. You should write two procedures $\text{east\_west()}$ and $\text{north\_south()}$ to show how cars travelling in the respective direction should behave.
23. Write a **monitor** that implements an **alarm clock** that enables a calling program to delay itself for a specified number of time units (ticks). You may assume the existence of a real hardware clock that invokes a procedure $\text{tick}$ in your monitor at regular intervals.
24. Consider a system consisting of processes $P_1, P_2, \ldots, P_n$, each of which has a unique priority number. Write a **monitor** that allocates three identical **line printers** to these processes, using the priority numbers for deciding the order of allocation.
25. Show that the **two-phase locking protocol** ensures conflict serializability.
