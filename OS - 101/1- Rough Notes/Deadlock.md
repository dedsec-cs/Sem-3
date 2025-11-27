These notes cover **Threads**, a lightweight approach to concurrency, and the crucial topic of **Deadlocks** in Operating Systems. I'll provide detailed explanations for a complete understanding.

---

## 🧵 Threads

A **Thread** is a basic unit of CPU utilization. It represents a **flow of execution within a process**.

* **Lightweight Process (LWP):** A thread is often called a lightweight process because it maintains its own context (like a Program Counter and Stack) but **shares** the vast majority of resources with its parent process.
* **Shared Resources:** All threads within the same process share the process's **Text Section** (code), **Data Section** (global variables), **Heap** (dynamic memory), and OS resources (like open files, child processes, and signal handling).
* **Private Resources:** Each thread maintains its own:
    * **Program Counter (PC):** Points to the next instruction to execute.
    * **Registers:** CPU state information.
    * **Stack:** Used for local variables, function parameters, and return addresses.

### Advantages of Threads

Using threads (multithreading) over multiple heavy processes offers significant benefits:

1.  **Concurrency within a Process:** Allows different parts of the same application to execute seemingly simultaneously.
2.  **Minimized Context Switching Time:** Thread context switching involves saving and loading fewer components (mainly registers and the stack pointer) compared to a process switch, which must save the entire address space.
3.  **Economical:** Threads are **faster to create and terminate** than processes because they don't require new memory structures (like the Page Table) to be set up by the OS.
4.  **Efficient Communication:** Communication between threads is easy and fast because they share the same address space (memory), avoiding the need for complex Inter-Process Communication (IPC) mechanisms.

### Process vs. Thread

| Feature | Process (Heavyweight) | Thread (Lightweight) |
| :--- | :--- | :--- |
| **Creation/Switching** | **Heavyweight**; slow to create/switch. | **Lightweight**; fast to create/switch. |
| **OS Interaction** | Switching **requires interaction** with the OS kernel. | Switching can often happen **without kernel intervention** (in User-level threads). |
| **Resource Sharing** | Each process has its **own separate memory** and file resources. | All threads **share** the same memory, open files, and data sections. |
| **Isolation** | High. If one process is blocked, others can run. | Low. If one thread makes a **blocking system call** (in User-Level threading), the **entire process is blocked**. |

### Types of Threads 

Threads are classified based on where the management (creation, scheduling, switching) takes place.

#### 1. User-Level Threads (ULT)

* **Management:** Handled entirely by a **user-level thread library** (e.g., POSIX Pthreads) in the application space, **without the kernel's knowledge**.
* **Advantages:**
    * **Fast:** Thread switching does not require a mode switch to the kernel (no kernel privileges needed).
    * **Flexible:** Scheduling can be application-specific.
    * **Portable:** Can run on any OS.
* **Disadvantages:**
    * **Blocking Problem:** If one thread makes a **blocking system call** (like reading from disk), the kernel blocks the **entire process**, stopping all other threads in that process.
    * **No Multi-Processing:** The OS only sees one process, so the application cannot utilize multiple CPU cores/processors simultaneously.

#### 2. Kernel-Level Threads (KLT)

* **Management:** Handled directly by the **Operating System Kernel**. The kernel maintains context information for both the process and each individual thread.
* **Advantages:**
    * **No Blocking Problem:** If one thread is blocked (e.g., waiting for I/O), the kernel can schedule another thread of the **same process** to run.
    * **True Concurrency:** The kernel can simultaneously schedule multiple threads from the same process on **multiple processors/cores**.
* **Disadvantages:**
    * **Slow:** Transfer of control requires a **mode switch** to the kernel, making creation and context switching slower than ULTs.

### Thread Cancellation

**Thread Cancellation** is the task of terminating a target thread before it has completed its work.

* **Example:** In a search operation, once one thread finds the answer, the other search threads are cancelled.
* **Modes:** Cancellation can be **asynchronous** (terminating the thread immediately, which can leave shared resources in an inconsistent state) or **deferred** (the target thread periodically checks a flag and terminates itself safely at a convenient point).

---

## 🔒 Deadlock

A **deadlock** is a state in which two or more processes are permanently blocking each other because they are each waiting for a resource held by another process in the set.

* **Deadlock State:** A system is in a deadlock state if a **circular-wait condition** exists for some set of processes and resources.

### Four Necessary Conditions for Deadlock

A deadlock can only occur if the following four conditions hold simultaneously (known as the Coffman Conditions):

1.  **Mutual Exclusion:** At least one resource must be held in a non-sharable mode (only one process can use it at a time).
2.  **Hold and Wait:** A process must be holding at least one resource and waiting to acquire additional resources currently held by other processes.
3.  **No Preemption:** A resource cannot be forcibly taken away from a process; it must be voluntarily released by the process holding it.
4.  **Circular Wait:** A set of processes $\{P_0, P_1, \dots, P_n\}$ exists such that $P_0$ is waiting for a resource held by $P_1$, $P_1$ is waiting for a resource held by $P_2$, ..., and $P_n$ is waiting for a resource held by $P_0$. 

### Methods for Handling Deadlock

There are three general strategies for handling deadlocks:

1.  **Deadlock Prevention or Avoidance:** Ensure the system never enters a deadlock state.
2.  **Deadlock Detection and Recovery:** Allow deadlocks to occur, detect them, and then recover by breaking the circular wait.
3.  **Ignore the Problem:** Assume deadlocks will rarely occur and restart the system if one happens (used by most general-purpose OSs like Windows/Linux).

### Deadlock Prevention

This strategy works by ensuring that at least one of the four necessary conditions for deadlock **can never hold**.

1.  **Avoid Mutual Exclusion:** Make all resources sharable. (*Impractical* for non-sharable resources like printers or write access to files.)
2.  **Avoid Hold and Wait:**
    * **Strategy 1:** A process must request and be allocated **all its necessary resources** before execution starts.
    * **Strategy 2:** A process must release all its currently held resources before requesting any new ones.
    * *Drawback:* Low resource utilization and potential starvation.
3.  **Avoid No Preemption:** If a process holding resources requests another resource that cannot be immediately allocated, the OS **takes away (preempts)** all resources currently held by the waiting process.
    * *Drawback:* Practical only for resources whose state can be easily saved and restored (e.g., CPU registers, memory).
4.  **Avoid Circular Wait:** Assign a unique **priority number** (ordering) to each resource type. A process can only request resources in **increasing order** of enumeration.
    * *Benefit:* This ensures that no cycle can be formed.

### Deadlock Avoidance

**Deadlock Avoidance** is a strategy that requires the OS to have **a priori knowledge** of each process's maximum resource needs. It allows the first three conditions (Mutual Exclusion, Hold and Wait, No Preemption) to exist but checks every resource allocation request to ensure the system remains in a **safe state**.

#### System States

1.  **Safe State:** When the system can allocate resources to each process in some sequence (a **safe sequence**) and still **avoid a deadlock**. In a safe sequence, a process $P_i$ can request its maximum resources and terminate. A system in a safe state is guaranteed to have no deadlocks.
2.  **Unsafe State:** A state that **may** lead to a deadlock. The system cannot find a safe sequence for the current state.
3.  **Deadlock State:** The system has entered a state where a circular wait exists, and processes are permanently blocked.

#### Avoidance Algorithms

* **Single Instance of a Resource Type:** The **Resource-Allocation Graph** algorithm is used. The OS maintains a claim edge ($P \to R$) for maximum claims. When a request is made, the OS checks if granting the request would complete a cycle.
* **Multiple Instances of a Resource Type:** The **Banker's Algorithm** is used. This algorithm simulates the allocation of maximum possible resources and makes an allocation only if the simulated state is found to be safe.