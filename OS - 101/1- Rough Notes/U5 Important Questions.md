## Unit 5 Questions 🌐

Here are the questions from Unit 5, which covers **Distributed Systems, Virtualization, and Disk Scheduling**:

1.  Describe the key differences between **parallel** and **distributed systems**.
2.  How do **virtual machines** help in resource management?
3.  Explain the importance of **hypervisors** in virtualization.
4.  What are **virtual machines**? Differentiate between **Type 1** and **Type 2 hypervisors**.
5.  How can **GPUs** improve the performance of AI and machine learning tasks? Develop a **GPU-based framework** for real-time image processing.
6.  Why does **C-LOOK** perform better than **LOOK** in some scenarios?
7.  Compare the architectures of **CPU** and **GPU** in terms of processing efficiency.
8.  How can **GPUs** improve the performance of AI and machine learning tasks?
9.  A company wants to implement virtualization for cost efficiency. Suggest a suitable **hypervisor** and justify your choice.
10. Which is better for handling large-scale computations: a **parallel system** or a **distributed system**? Justify your answer.
11. Design a basic **distributed system model** for a real-world application (e.g., online banking).

---

### Disk Scheduling Problems

12. Consider a disk queue with requests for I/O to blocks on cylinders 98, 183, 41, 122, 14, 124, 65, 67. The **FCFS scheduling algorithm** is used. The head is initially at cylinder number 53. The cylinders are numbered from 0 to 199. The total head movement (in number of cylinders) incurred while servicing these requests is?
13. Consider a disk with 200 tracks and the queue has random requests from different processes in the order: 55, 58, 39, 18, 90, 160, 150, 38, 184. Initially arm is at 100. Find the **Average Seek length** using **FIFO, SSTF, SCAN** and **C-SCAN** algorithm.
14. Disk requests come to a disk driver for cylinders in the order 10, 22, 20, 2, 40, 6 and 38 at a time when the disk drive is reading from cylinder 20. The seek time is $6 \text{ ms/cylinder}$. The total seek time, if the disk arm scheduling algorithms is **first-come-first-served** is...
15. Consider the disk system with 100 cylinders. The request to access the cylinders occur in the following sequence: 4, 37, 10, 7, 19, 73, 2, 15, 6, 20. Assuming the head is currently at cylinder 50 what is the time taken to satisfy all requests if it takes $1 \text{ ms}$ to move from one cylinder to adjacent one and **shortest seek time first algorithm (SSTF)** is used.

---

### Comprehensive Disk Scheduling Problem

Given: A disk queue with requests at the following track numbers: 98, 183, 37, 122, 14, 124, 65, 67. Initial head position: 53. Disk size: 200 tracks. Head movement direction: Right.

Solve the following:

16. Compute the total seek time using the **FCFS (First-Come, First-Served) algorithm**.
17. Solve using the **SSTF (Shortest Seek Time First) algorithm**.
18. Apply the **SCAN (Elevator) algorithm** and find the total head movement.
19. Solve using the **C-SCAN (Circular SCAN) algorithm**.

---

### Architecture and Performance

20. Explain the impact of **disk architecture** on system performance.
21. How does **disk cache** improve the performance of storage devices?
22. What is **disk scheduling**? Explain its need in operating systems.
23. Describe the **First-Come, First-Served (FCFS)** disk scheduling algorithm with an example.
24. Explain the **Shortest Seek Time First (SSTF)** scheduling algorithm with a diagram.
