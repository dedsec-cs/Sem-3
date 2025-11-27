## Unit 4 Questions 🧠

Here are the questions from Unit 4, which focuses on **Memory Management and Virtual Memory**:

1.  Compare **FIFO** with other page replacement algorithms (like **LRU, LFU, and Optimal**). Under what situations would FIFO be more efficient than other algorithms?
2.  Given a scenario where a system is experiencing **thrashing**, explain how the operating system can detect and address this problem. Discuss the strategies for reducing or eliminating thrashing, such as page swapping, **working set management**, and memory allocation tuning.
3.  Explain the concept of **non-contiguous memory allocation** and how it overcomes the limitations of contiguous allocation. Discuss the techniques involved in non-contiguous memory allocation, focusing on **Paging** and **Segmentation**. How do these techniques help in minimizing **fragmentation**?
4.  Define **segmented paging** and explain how it combines the features of both segmentation and paging to manage memory. What are the benefits of segmented paging over pure segmentation and paging, and in what scenarios is segmented paging particularly useful?
5.  Discuss the concept of **virtual memory** and explain how it allows the system to run processes that may not fit entirely into physical memory. What role does **demand paging** play in virtual memory management? How does demand paging optimize memory usage, and what factors contribute to its performance?
6.  Define **thrashing** in the context of virtual memory systems. What are the causes of thrashing, and how does it affect system performance? What strategies can be employed to reduce or prevent thrashing in an operating system?
7.  Discuss **address binding** in the context of loading and linking, explaining the different types of address binding (**compile-time, load-time, and execution-time**). How do these bindings affect the execution of a process?
8.  In memory management, allocation strategies play a crucial role in determining how memory is assigned to processes. Compare and contrast the **First Fit, Best Fit, and Worst Fit** strategies for memory allocation. How do these strategies impact the efficiency of memory usage and process execution?
9.  Explain the concept of **virtual memory** and how it allows processes to exceed physical memory limits. Discuss the concept of **demand paging** and its impact on system performance. How is **page fault handling** managed in demand paging, and what are the factors influencing its efficiency?
10. Describe the function of **memory management** in an operating system. Discuss the role of **loading and linking** in the memory management process. Also, explain **address binding** and how it occurs at different stages (compile-time, load-time, and execution-time), with examples of how it impacts process execution.
11. Explain the concept of **Belady's Anomaly** and discuss how it applies to page replacement algorithms. Which algorithms are susceptible to Belady's Anomaly?

---

### Page Replacement Algorithm Problems

12. Consider the following reference string: 4, 3, 2, 1, 4, 3, 5, 4, 3, 2, 1, 5, and a frame size of 3. Calculate the **page fault rate** using **FIFO**. Explain your solution step-by-step.
13. Given a reference string: 4, 7, 6, 1, 7, 6, 1, 2, 7, 2 and a frame size of 3, calculate the **number of page faults** using **FIFO**. Show your calculations and explain the results.
14. Given the following reference string: 3, 1, 2, 3, 4, 2, 3, 0, 3, 1, 3, and a frame size of 3, calculate the **number of page faults** using the **LRU**.
15. Consider the following reference string: 4, 3, 2, 1, 4, 3, 5, 4, 3, 2, 1, 5, and a frame size of 3. Calculate the **page fault rate** using **LRU**. Explain your solution step-by-step.
16. Given the following reference string: 1, 2, 3, 4, 2, 5, 3, 4, 2, 6, 3, 8, 4, and a frame size of 3, calculate the **number of page faults** using the **Optimal page replacement algorithm**.
17. Given the following reference string: 5, 3, 1, 5, 4, 1, 6, 3, 4, 5, 1, and a frame size of 3, calculate the **number of page faults** using the **Optimal page replacement algorithm**.
18. Consider the following reference string: 0, 1, 2, 3, 0, 1, 4, 0, 1, 2, 3, 4, and a frame size of 4. Calculate the **page fault rate** using **LRU**. Explain your solution step-by-step.
19. Consider six memory partitions of size 200 KB, 400 KB, 600 KB, 500 KB, 300 KB and 250 KB. These partitions need to be allocated to four processes of sizes 357 KB, 210 KB, 468 KB and 491 KB in that order. Perform the allocation of processes using- **First Fit Algorithm, Best Fit Algorithm, Worst Fit Algorithm**.
20. Consider the page references 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3 with 4-page frame. Find **number of page faults** using **Optimal Page Replacement Algorithm**.
21. Consider the following reference string: 1, 2, 3, 4, 5, 1, 2, 3, and a frame size of 3. Calculate the **page fault rate** using **FIFO, LRU, Optimal, and LFU**. Compare the results and explain the differences.
