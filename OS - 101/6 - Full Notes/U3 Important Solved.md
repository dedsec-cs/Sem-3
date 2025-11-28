### **Q1. Discuss RAG and give example of wait-for graph (WFG).**

**Answer:**

- **Resource Allocation Graph (RAG):** A directed graph used to characterize deadlocks. It consists of a set of vertices V and edges E.
    
    - **Vertices (V):** Partitioned into two types:
        
        - P={P1​,P2​,…,Pn​}: The set of all active processes.
            
        - R={R1​,R2​,…,Rm​}: The set of all resource types in the system .
            
    - **Edges (E):**
        
        - **Request Edge (Pi​→Rj​):** Process Pi​ has requested an instance of resource Rj​ and is waiting for it.
            
        - **Assignment Edge (Rj​→Pi​):** An instance of resource Rj​ has been allocated to process Pi​.
            
- **Wait-for Graph (WFG):** This is used for deadlock detection in systems with **single instances** of each resource type. It is obtained by removing the resource nodes from the RAG and collapsing the edges.
    
    - An edge Pi​→Pj​ exists in the WFG if and only if the corresponding RAG contains a path Pi​→Rq​→Pj​. This implies Pi​ is waiting for a resource held by Pj​.
        



---

### **Q2. Explain any two deadlock handling methods in detail.**

**Answer:** Two common methods for handling deadlocks are:

1. **Deadlock Prevention:**
    
    - This ensures that at least one of the four necessary conditions for deadlock (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait) cannot hold .
        
    - _Example Strategy:_ To prevent **Hold and Wait**, the system can require a process to request and be allocated all its resources before it begins execution. To prevent **Circular Wait**, the system can impose a total ordering of resource types and require processes to request resources in increasing order.
        
2. **Deadlock Avoidance:**
    
    - This requires the system to have a priori information about the maximum resources a process will request.
        
    - The system dynamically examines the resource-allocation state to ensure it never enters an **Unsafe State** (a state where a deadlock _could_ occur).
        
    - _Algorithm:_ The **Banker's Algorithm** is the standard method used for deadlock avoidance in systems with multiple instances of resources.
        

---

### **Q3. Discuss the classical problems of synchronization in detail.**

**Answer:** The classical problems used to test synchronization schemes include:

1. **Bounded-Buffer Problem (Producer-Consumer):**
    
    - A producer creates data and places it in a buffer; a consumer removes it.
        
    - **Challenge:** The producer must wait if the buffer is full, and the consumer must wait if the buffer is empty .
        
2. **Readers-Writers Problem:**
    
    - A data set is shared among multiple processes. Readers only read; Writers can read and write.
        
    - **Challenge:** Multiple readers can read simultaneously, but if a writer is writing, no other process (reader or writer) can access the shared data .
        
3. **Dining-Philosophers Problem:**
    
    - Five philosophers sit at a table with five single chopsticks. A philosopher needs two chopsticks to eat.
        
    - **Challenge:** Avoiding deadlock (everyone picking up the left chopstick at once) and starvation .
        
4. **Sleeping Barber Problem:**
    
    - A barber sleeps if there are no customers. A customer wakes the barber if he is sleeping. If the barber is busy, the customer waits in a chair unless all chairs are full .
        

---

### **Q4. Discuss the atomic operations of semaphore and show how mutual exclusion can be implemented.**

**Answer:** A **Semaphore (S)** is an integer variable accessed only through two atomic (indivisible) operations: `wait()` and `signal()` .

**Atomic Operations:**

1. **wait(S):** Checks if S≤0. If true, the process waits (busy wait or blocks). If S>0, it decrements S .
    
    C
    
    ```
    wait(S) {
       while (S <= 0); // busy wait
       S--;
    }
    ```
    
2. **signal(S):** Increments the value of S .
    
    C
    
    ```
    signal(S) {
       S++;
    }
    ```
    

**Mutual Exclusion Implementation:** To ensure only one process executes in a Critical Section (CS) at a time, initialize a semaphore named `mutex` to **1**.

C

```
do {
    wait(mutex);       // Decrement mutex (1 -> 0). Process enters.
                       // Other processes wait because mutex is now 0.
        /* critical section */
    signal(mutex);     // Increment mutex (0 -> 1). Allows next process in.
        /* remainder section */
} while (true);
```

---

### **Q5. Discuss the process of deadlock detection and also explain various approaches we follow to avoid deadlock detection in detail.**

**Answer:** _Note: The question likely asks to explain "Deadlock Detection" and approaches to "Avoid Deadlock" (Prevention/Avoidance)._

**Deadlock Detection:**

- Used when the system does not employ prevention or avoidance. The system periodically invokes an algorithm to examine the resource-allocation state.
    
- **Single Instance Resources:** Uses a **Wait-for Graph**. If the graph contains a cycle, a deadlock exists.
    
- **Multiple Instance Resources:** Uses an algorithm similar to Banker's (using Available, Allocation, and Request matrices) to see if the current processes can finish. If all processes cannot finish, the system is deadlocked.
    

**Approaches to Avoid Deadlock (Avoidance):**

- **Safe State:** The system allows a resource request only if the allocation leaves the system in a Safe State.
    
- **Banker’s Algorithm:** Used for multiple resource instances. It simulates resource allocation and checks if a "safe sequence" exists where all processes can complete.
    

---

### **Q6. Discuss about Peterson solution for the critical section problem in detail.**

**Answer:** Peterson’s Solution is a software-based algorithm for two processes (P0​ and P1​) that solves the Critical Section problem. It guarantees Mutual Exclusion, Progress, and Bounded Waiting .

**Shared Data:**

- `int turn`: Indicates whose turn it is to enter.
    
- `boolean flag[2]`: Indicates if a process is ready to enter (`flag[i] = true` means Pi​ wants to enter) .
    

**Algorithm for Process Pi​:**

C

```
while (true) {
    flag[i] = true;        // I want to enter
    turn = j;              // I assume it is your turn
    while (flag[j] && turn == j); // Wait if you want to enter AND it is your turn

        /* Critical Section */

    flag[i] = false;       // I am leaving
        /* Remainder Section */
}
```

.

---

### **Q7. Describe Lamport Bakery Solution to the critical section problem.**

**Answer:**

(Note: While listed in the syllabus, the detailed slides focus on Peterson's. The Bakery algorithm is a generalization of Peterson's solution for N processes.)

- **Concept:** Based on a bakery numbering system. A process entering the ready queue receives a number. The process with the lowest number is served next.
    
- **Key Behavior:**
    
    - If two processes receive the same number, the one with the lower Process ID (PID) gets priority.
        
    - Processes choose a number `max(all_current_numbers) + 1`.
        
    - Before entering the critical section, a process checks if any other process has a smaller number.
        

---

### **Q8. Discuss Sleeping Barber problem in detail.**

**Answer:** This is a classic IPC synchronization problem.

- **Scenario:** A shop has 1 barber, 1 barber chair, and N waiting chairs.
    
- **Behavior:**
    
    - If no customers are present, the barber sleeps in his chair.
        
    - If a customer enters and the barber is asleep, the customer wakes him.
        
    - If the barber is busy, the customer sits in a waiting chair. If all chairs are occupied, the customer leaves .
        
- **Implementation:** Requires three semaphores:
    
    1. `customers`: Counts waiting customers.
        
    2. `barber`: Binary semaphore (0 = busy, 1 = idle/waiting).
        
    3. `mutex`: Mutual exclusion for accessing the number of free chairs.
        

---

### **Q9. Elaborate the reader-writer problem in detail.**

**Answer:**

- **Problem:** A shared data set (file or database) is accessed by "Readers" (read-only) and "Writers" (read-write).
    
- **Constraint:** Multiple readers can read simultaneously. However, if a writer is accessing the data, it must have exclusive access (no other writers or readers allowed) .
    
- **Synchronization Primitives:**
    
    - `rw_mutex`: A semaphore that functions as a mutual exclusion lock for the writers. The first reader to enter locks it, and the last reader to leave unlocks it.
        
    - `mutex`: A semaphore to protect the `read_count` variable.
        
    - `read_count`: Tracks the number of active readers .
        

---

### **Q10. Elaborate Race Condition and how synchronization helps in concurrent programming.**

**Answer:**

- **Race Condition:** A situation where multiple processes access and manipulate shared data concurrently. The final value of the data depends on the specific order in which the instructions are executed (interleaving).
    
    - _Example:_ If two processes try to increment a variable `count` (read -> add -> write) at the same time, one increment might be overwritten .
        
- **Role of Synchronization:** Synchronization mechanisms (like semaphores or monitors) ensure **Mutual Exclusion**. This guarantees that only one process can access the critical section (shared data) at a time, preventing race conditions and ensuring data consistency.
    

---

### **Q11. Write a short note on Interprocess communication (IPC) with its advantages and disadvantages.**

**Answer:** IPC is a mechanism allowing cooperating processes to exchange data. **Two Models:**

1. **Shared Memory:**
    
    - A shared region of memory is established. Processes read/write data here .
        
    - _Advantage:_ Maximum speed/convenience for large data; processed at memory speeds.
        
    - _Disadvantage:_ Synchronization is difficult; programmer must manage conflicts.
        
2. **Message Passing:**
    
    - Communication via exchanging messages (send/receive).
        
    - _Advantage:_ Easier to implement for distributed systems; prevents conflicts automatically via kernel handling.
        
    - _Disadvantage:_ Slower due to system call overhead (kernel intervention required).
        

---

### **Q12. Show how mutual exclusion can be implemented and give example of synchronization hardware using Test and Set operation.**

**Answer:** Hardware synchronization uses special atomic instructions.

- **Test-and-Set:** An atomic instruction that reads a variable and sets it to TRUE in one uninterruptible step.
    
- **Implementation:** Shared boolean variable `lock` initialized to `FALSE`.
    
    C
    
    ```
    do {
       while (test_and_set(&lock)); // Busy wait loop.
                                    // Returns old value (FALSE) and sets to TRUE.
                                    // If locked (TRUE), loop continues.
    
           /* Critical Section */
    
       lock = false;                // Release lock
           /* Remainder Section */
    } while (true);
    ```
    
    (Referenced as "Test and set lock" in syllabus topics).
    

---

### **Q13. Describe the Bounded-buffer problem and give a solution for the same using semaphores.**

**Answer:**

- **Problem:** A producer creates items for a fixed-size buffer; a consumer removes them. Synchronization is needed to prevent producing into a full buffer or consuming from an empty one .
    
- **Semaphore Solution:**
    
    - `mutex` (init 1): Protects the buffer pool.
        
    - `full` (init 0): Counts filled slots.
        
    - `empty` (init N): Counts empty slots .
        
- **Producer:** `wait(empty); wait(mutex); // add item; signal(mutex); signal(full);`
    
- **Consumer:** `wait(full); wait(mutex); // remove item; signal(mutex); signal(empty);` .
    

---

### **Q14. Write code for Dining Philosopher problem and discuss the approaches for reducing deadlock condition.**

**Answer:**

- **Standard Code (Deadlock Prone):**
    
    C
    
    ```
    wait(chopstick[i]);          // Take left
    wait(chopstick[(i+1) % 5]);  // Take right
    // EAT
    signal(chopstick[i]);
    signal(chopstick[(i+1) % 5]);
    ```
    
    .
    
- **Approaches to Reduce Deadlock:**
    
    1. Allow at most 4 philosophers to sit at the table of 5 seats.
        
    2. Allow picking up chopsticks only if **both** are available (requires a critical section).
        
    3. **Asymmetric Solution:** Odd philosophers pick left chopstick first; Even philosophers pick right chopstick first .
        

---

### **Q15. Discuss in detail the critical section problem and also write the algorithm for Readers/Writers Problem with semaphores.**

**Answer:**

- **Critical Section Problem:** The challenge of designing a protocol where processes can access shared data (critical section) without race conditions. It must satisfy Mutual Exclusion, Progress, and Bounded Waiting .
    
- **Readers/Writers Algorithm (Writer Process):**
    
    C
    
    ```
    wait(rw_mutex);      // Lock access for writers/readers
    /* writing is performed */
    signal(rw_mutex);    // Release access
    ```
    
    . _(Note: Readers utilize a `read_count` protected by a separate `mutex` to ensure `rw_mutex` is only locked by the first reader and released by the last reader)._
    

---

### **Q16. Mention five real life examples of deadlock situation.**

**Answer:**

1. **Traffic Jam:** Four cars at a 4-way stop, each waiting for the one on the right to move.
    
2. **Narrow Bridge:** Two cars meeting on a single-lane bridge; neither can back up due to traffic behind them (implied by "traffic signals" application).
    
3. **Printer/Scanner:** Process A holds the Printer and waits for the Scanner; Process B holds the Scanner and waits for the Printer.
    
4. **Bank Accounts:** Two transactions trying to transfer money to each other's locked accounts simultaneously (A locks Acc1, wants Acc2; B locks Acc2, wants Acc1).
    
5. **Client-Server:** Client waits for Server response; Server waits for Client request (Communication Deadlock).
    

---

### **Q17. Describe Banker's algorithm with an example.**

**Answer:** The Banker's Algorithm prevents deadlock by checking if granting a resource request leaves the system in a **Safe State**.

- **Data Structures:** `Available`, `Max`, `Allocation`, `Need` .
    
- **Logic:**
    
    1. Calculate `Need = Max - Allocation`.
        
    2. Find a process Pi​ where `Need` ≤ `Available`.
        
    3. If found, pretend to allocate, let Pi​ finish, and reclaim its resources (`Available += Allocation`).
        
    4. Repeat. If all processes finish, the state is safe.
        
    
    - _Example:_ See Q18 below for a specific numerical walkthrough .
        

---

### **Q18. [Numerical] Check if the state is safe using Banker's Algorithm.**

**Given:** 4 Resources (R1, R2, R3, R4) with total units (6, 4, 4, 2). **Allocated Matrix:** P1(2,0,1,1), P2(1,1,0,0), P3(1,1,0,0), P4(1,0,1,0), P5(0,1,0,1). **Max Matrix:** P1(3,2,1,1), P2(1,2,0,2), P3(1,1,2,0), P4(3,2,1,0), P5(2,1,0,1).

**Solution:**

1. **Total Allocated:** Sum columns of Allocation. R1: 2+1+1+1+0 = 5. R2: 3. R3: 2. R4: 2. Total Alloc = (5, 3, 2, 2).
    
2. **Available:** Total Units (6,4,4,2) - Alloc (5,3,2,2) = **(1, 1, 2, 0)**.
    
3. **Need Matrix (Max - Allocation):**
    
    - P1: (1, 2, 0, 0)
        
    - P2: (0, 1, 0, 2)
        
    - P3: (0, 0, 2, 0)
        
    - P4: (2, 2, 0, 0)
        
    - P5: (2, 0, 0, 0)
        
4. **Safety Sequence Check:**
    
    - **P3:** Need (0,0,2,0) <= Avail (1,1,2,0). **True.**
        
        - New Avail = (1,1,2,0) + P3_Alloc (1,1,0,0) = **(2, 2, 2, 0)**.
            
    - **P1:** Need (1,2,0,0) <= Avail (2,2,2,0). **True.**
        
        - New Avail = (2,2,2,0) + P1_Alloc (2,0,1,1) = **(4, 2, 3, 1)**.
            
    - **P4:** Need (2,2,0,0) <= Avail (4,2,3,1). **True.**
        
        - New Avail = (4,2,3,1) + P4_Alloc (1,0,1,0) = **(5, 2, 4, 1)**.
            
    - **P5:** Need (2,0,0,0) <= Avail (5,2,4,1). **True.**
        
        - New Avail = (5,2,4,1) + P5_Alloc (0,1,0,1) = **(5, 3, 4, 2)**.
            
    - **P2:** Need (0,1,0,2) <= Avail (5,3,4,2). **True.**
        
        - New Avail = (5,3,4,2) + P2_Alloc (1,1,0,0) = **(6, 4, 4, 2)**. **Result:** The system is in a **Safe State**. Sequence: **<P3, P1, P4, P5, P2>**.
            

---

### **Q19. In a uniprocessor system, can the system ever enter into a deadlock? Justify your answer.**

**Answer:** Yes, a uniprocessor system can enter a deadlock.

- **Justification:** Deadlock depends on the logical contention for resources (like printers, files, or semaphores), not on the number of processors. Even with a single CPU, if Process A holds Resource X and waits for Y (via context switch), and Process B holds Y and waits for X, a circular wait is established, causing deadlock .
    

---

### **Q20. [Coding] A club has a lounge where members (smokers/non-smokers) sit. Smokers can smoke only if non-smokers are absent.**

**Answer (Using Semaphores):** This is equivalent to a Readers-Writers problem where Smokers are "Writers" (require exclusive access regarding Non-smokers) and Non-smokers are "Readers".

**Variables:** `mutex=1`, `lounge=1`, `smokerCount=0`.

C

```
// Code for Smoker (Requires Non-smokers to be absent)
enterLounge(true) {
    wait(mutex);
    if (smokerCount == 0) {
        wait(lounge); // Lock lounge from non-smokers
    }
    smokerCount++;
    signal(mutex);
}

smoke() { ... }

leaveLounge(true) {
    wait(mutex);
    smokerCount--;
    if (smokerCount == 0) {
        signal(lounge); // Unlock lounge
    }
    signal(mutex);
}
```

_Note: A complete solution would also require `nonSmokerCount` logic for the other group._.

---

### **Q21. Traffic crossing synchronization (East-West vs North-South).**

**Answer:** This is another variation of the Readers-Writers problem. "North-South" cars can share the crossing (Readers), but "East-West" cars (Writers) need exclusive access relative to NS (and vice versa).

- Use a semaphore `crossing_mutex` to ensure only one _direction_ owns the crossing.
    
- Use `NS_count` and `EW_count` protected by their own mutexes.
    
- The first car of a direction locks `crossing_mutex`; the last car releases it.
    

---

### **Q24. Show that the two-phase locking protocol ensures conflict serializability.**

**Answer:**

(Note: This topic relates to Database Transactions mentioned in "Case Study", though 2PL details are not in the provided PPT slides. Standard OS/DB answer follows).

- **Two-Phase Locking (2PL):** A transaction has a **Growing Phase** (acquiring locks, no releasing) and a **Shrinking Phase** (releasing locks, no acquiring).
    
- **Reasoning:** By holding all necessary locks until the "lock point" (end of growing phase), 2PL ensures that the order of conflicting operations is consistent with the order of lock points, guaranteeing a serializable schedule.