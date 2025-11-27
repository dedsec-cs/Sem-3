## 🏃 Concurrent Processes

**Concurrency** is the fundamental concept in modern operating systems that allows multiple tasks (processes) to make progress seemingly at the same time.

### Process Model and Sections

A **process** is an **active entity**—a program in execution. When you launch a program, the OS creates a process, loading the program's instructions and data into memory.

A process is logically divided into four main sections, primarily residing in RAM:

* **1. Text Section:** Contains the **executable instructions** (the code) and any fixed macros. It is generally a **read-only** area and can often be **shared** by multiple processes running the same program (e.g., multiple instances of a calculator app).
* **2. Data Section:** Contains **global and static variables**. These are allocated memory once the program is loaded.
* **3. Heap Section:** Used for **dynamic memory allocation** (memory requested during run-time) using functions like `malloc()` or `new`. This section grows upwards toward the Stack.
* **4. Stack Section:** Contains temporary data, including **local variables**, **function parameters**, and **return addresses** for function calls. This section typically grows downwards toward the Heap.

---

### Difference between Process and Program

| Process (Active Entity) | Program (Passive Entity) |
| :--- | :--- |
| Is a **sequential program in execution** (a live instance). | Is a **set of instructions** stored on disk (a static file). |
| Includes resources like the **Program Counter**, registers, stack, and heap. | Is simply a **set of instructions**; it doesn't need resources to exist. |
| Is an **active entity** that executes concurrently. | Is a **passive entity** (like a blueprint). |
| **Dependent** on the program for its instructions. | **Independent** of any execution state. |

---

### Principle of Concurrency

**Concurrency** is the **interleaving of processes in time** on a single CPU core, giving the *appearance* of simultaneous execution.

* **Multitasking OS:** Any operating system described as multi-tasking supports concurrency.
* **Fundamental Problem:** When multiple processes are concurrent, they must often access and update a **shared global resource** (like a variable or a file), which leads to synchronization problems like the **Race Condition**.

| Concurrency | Parallelism |
| :--- | :--- |
| **Actions in progress** at the same time (time-slicing on one core). | **Actions executing simultaneously** (running on multiple cores/CPUs). |
| A property of the **program/system design**. | A property of the **machine/hardware**. |

---

### Synchronization Primitives and Problems

Synchronization is necessary to ensure that concurrent access to shared data is done correctly and consistently.

#### Difference between Busy Waiting and Blocking

| Busy Waiting (Spinlock) | Blocking (Sleep/Wakeup) |
| :--- | :--- |
| The process **continuously tests a condition** in a loop, wasting CPU cycles while waiting. | The process is **suspended** and put into a waiting queue until the required event occurs. |
| **Does not share sufficient time**—it monopolizes the CPU waiting. | **Yields the CPU** for other processes to run, improving utilization. |
| Used in **scheduled** contexts (e.g., in a kernel if the wait is expected to be very short). | Used when processes **wait indefinitely** for an event (I/O, resource release). |

#### Critical Section Problem

* A **Critical Section** is the code segment where a process accesses **shared variables** or resources.
* An **atomic action** is required here: only one process must execute its critical section at a time to ensure data consistency.
* The solution to the Critical Section Problem requires three conditions:

| Condition | Description |
| :--- | :--- |
| **1. Mutual Exclusion** | **At most one process** may be executing in its critical section at any given time. |
| **2. Progress** | If no process is in the critical section, and some processes want to enter, only those processes *not* in their remainder section can participate in the decision, and that decision **cannot be postponed indefinitely**. |
| **3. Bounded Waiting** | There must be a **limit** on the number of times other processes are allowed to enter their critical sections after a process has requested entry and before that request is granted. |

#### Mutual Exclusion Algorithms

1.  **Dekker's Algorithm (Two-Process Solution):** The first known correct software-based solution. It uses two shared variables:
    * **Flags** (to indicate desire to enter CS).
    * A **Turn** variable (token) to break ties when both processes want to enter simultaneously.
2.  **Bakery Algorithm (N-Process Solution):** Solves the problem for $N$ processes. It uses a metaphorical "take a number" system:
    * Processes receive a **ticket number** before entering.
    * The process with the **smallest ticket number** enters.
    * Ties (same number) are broken by **Process ID** (lower ID wins).

---

## 🚦 Semaphores

A **Semaphore** is a simple, non-negative integer **variable** used for process synchronization, serving as a powerful and flexible solution to the critical section problem.

* Semaphores are accessed only through two **atomic operations**: **wait** and **signal**.

| Operation | Action | Effect on Process |
| :---: | :---: | :--- |
| **wait(S)** (or P) | Decrements $S$. | If $S$ becomes negative, the process is **blocked** (put into a waiting queue). |
| **signal(S)** (or V) | Increments $S$. | If $S$ is $\leq 0$ (meaning processes are blocked), one of the blocked processes is **woken up**. |

* **Counting Semaphores:** Can take any non-negative integer value. Used to control access to a resource pool with multiple instances.
* **Binary Semaphores:** Can only take values of 0 or 1. Used to enforce **Mutual Exclusion** (acting as a mutex lock).

#### Disadvantages of Semaphores

1.  **Complexity/Error Prone:** If `wait()` and `signal()` operations are not implemented in the **correct order**, it can easily lead to **deadlocks** or violations of mutual exclusion.
2.  **Priority Inversion:** A low-priority process might hold a semaphore, forcing a higher-priority process that needs the semaphore to wait.

---

## 🧩 Classical Synchronization Problems

These problems illustrate common concurrency challenges and are used to test the effectiveness of synchronization tools (like Semaphores).

### Producer-Consumer Problem

* **Setup:** A **Producer** process creates data items and stores them in a **Buffer**. A **Consumer** process retrieves and uses these items.
* **Constraint:** The Producer **cannot deposit** data if the buffer is **full**. The Consumer **cannot retrieve** data if the buffer is **empty**.
* **Solution (Semaphores):** Typically uses three semaphores:
    1.  A **binary semaphore (mutex)** for mutual exclusion on the buffer.
    2.  A **counting semaphore (empty)** counting empty buffer slots.
    3.  A **counting semaphore (full)** counting full buffer slots.

### Reader-Writer Problem

* **Setup:** Multiple processes share an object (like a file). Some are **Readers** (only read data), and some are **Writers** (modify data).
* **Constraints:**
    1.  **Multiple Readers** can access the object simultaneously.
    2.  If a **Writer** is accessing the object, **no other process (reader or writer)** may access it (**exclusive access**).
* **Problem:** To manage synchronization to ensure data integrity while maximizing concurrency.

### The Dining Philosophers Problem

* **Setup:** Five philosophers alternate between **THINKING** and **EATING** around a circular table, each requiring **two adjacent chopsticks** (shared resources) to eat.
* **Challenge:** The classic solution where each philosopher tries to grab the left stick, then the right stick, can lead to a **deadlock** where everyone holds one stick and waits forever for the other.
* **Solution Approach:** Requires a mechanism (like semaphores or a monitor) to ensure that a philosopher only tries to pick up both sticks if both are available, preventing the circular wait condition necessary for deadlock.

### Sleeping Barber Problem

* **Analogy:** Models a barber shop with one barber, one chair, and $N$ waiting chairs.
* **Challenge:** Synchronizing the barber (server) and the customers (clients):
    * If no customers, barber sleeps.
    * Customer must wake barber if asleep.
    * Customers wait if chairs are full, or leave if no chairs are empty.
* **Solution Approach:** Uses semaphores to manage the states of the barber and the customers, along with a shared variable to track the number of waiting customers.