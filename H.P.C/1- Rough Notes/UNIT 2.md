# **Computer Architecture**

## **🧠What is Computer Architecture**

Computer architecture defines the structure and behavior of a computer system—how it processes data, executes instructions, and manages memory.  
It acts as a blueprint connecting hardware and software for efficient performance.  

### The main types are:  
**SISD (Single Instruction, Single Data)** – one instruction on one data stream.  
**SIMD (Single Instruction, Multiple Data)** – same instruction on multiple data.  
**MISD (Multiple Instruction, Single Data)** – multiple instructions on one data stream.  
**MIMD (Multiple Instruction, Multiple Data)** – multiple instructions on multiple data streams.

![[Pasted image 20251108204604.png]]

---
## **SISD(Single Instruction, Single Data)**
SISD stands for **Single Instruction, Single Data**.  
It means one processor executes **a single instruction** on **a single data stream** at a time.  
It’s the simplest computer architecture — the kind most old, sequential computers use.

**Working:**
- Only **one control unit** and **one processing unit (ALU)**.
- Instructions are executed **one after another (sequentially)**.
- Both **instructions and data** are stored in **primary memory**.

**Characteristics:**
- Sequential execution (no parallelism).
- One instruction operates on one data at a time.
- Used in **uniprocessor systems**.
- Based on the **Von Neumann model**.

**Advantages:**
- Simple design and control.
- Easy to program and debug.
- Works well for small, general-purpose tasks.

**Limitations:**
- **Slow** for large or complex computations.
- No support for parallel processing.

**Examples:**
- **IBM PC**, **Macintosh**, **early Intel processors**, **ARM scalar instructions**.
---
## **SIMD(Single Instruction, Multiple Data)**

SIMD stands for **Single Instruction, Multiple Data**.  
It means a **single control unit** sends the **same instruction** to **multiple processors**, and each processor works on **different pieces of data** at the same time.  
It’s mainly used for tasks that handle large data sets — like graphics, images, or scientific computations.

**Working:**
- One instruction is **broadcast** to all processors (called **Processing Elements – PEs**).
- Each PE performs the **same operation** but on **different data**.
- Data is divided into chunks (like parts of a matrix or image).
- Great for **vector or array operations**.

**Characteristics:**
- **Parallel execution** of the same task on multiple data items.
- High performance for repetitive mathematical operations.
- Works best when the same computation repeats on large datasets.

**Advantages:**
- **Faster execution** for data-heavy tasks.
- Saves time by reducing the number of instructions.
- Good **hardware utilization**.

**Limitations:**
- Not suitable for tasks where operations are different on each data.
- Complex to program for non-uniform data.

**Examples:**
- **Vector processors**, **GPUs**, **Cray supercomputers**, **Intel SSE/AVX instructions**.
---
## **MISD(Multiple Instruction, Single Data)**

MISD stands for _Multiple Instruction, Single Data_.  
It’s a computer architecture where **multiple processors execute different instructions on the same data stream** at the same time.  
This type of system is mostly _theoretical_ and rarely used in practical computing.

**Working:**
- Each processor has its own **instruction stream** but works on the **same input data**.
- All processors perform **different operations** on that data simultaneously.
- Used mainly in systems that focus on **reliability or real-time control**, not speed.

**Characteristics:**
- Many instructions, one data stream.
- Focuses on **fault tolerance** and **data reliability**.
- Rare in commercial use because of its complexity.

**Advantages:**
- Good for **real-time systems** like control systems or defense applications.
- Useful for **error detection** and **fault-tolerant computing**.

**Limitations:**
- **Difficult to design** and synchronize.
- **Inefficient** for general or parallel computing.
- Very **limited scalability** and performance gain.

**Examples:**
- Used conceptually in **Space Shuttle flight control systems**, **redundant pipelines**, and **fault-tolerant processors**.
---
## **MIMD(Multiple Instruction, Multiple Data)**

MIMD stands for _Multiple Instruction, Multiple Data_.  
It’s a computer architecture where **multiple processors execute different instructions on different data sets** at the same time.  
This model allows **true parallel processing** and is the most commonly used architecture in modern systems.

**Working:**
- Each processor (called a **Processing Element**, PE) has its **own control unit**, **instruction stream**, and **data memory**.
- Processors work **asynchronously**, meaning each can perform a separate task independently. 
- It’s perfect for **multi-core CPUs**, **clusters**, and **distributed systems**.

**Characteristics:**
- Supports both **task-level** and **data-level** parallelism.
- Provides **high flexibility** and **scalability**.
- Processors can cooperate or work on **completely different problems**.

**Advantages:**
- **High performance** and **true parallel execution**.
- Works well for **complex, real-world applications**.
- Easy to scale by adding more processors.

**Limitations:**
- **Harder to program and synchronize** compared to SIMD.
- May face **communication delays** in distributed systems.
- Requires **advanced coordination mechanisms**.

**Types of MIMD Systems:**
1. **Shared Memory MIMD** – All processors share a common memory (used in multiprocessor systems).
2. **Distributed Memory MIMD** – Each processor has its own local memory; processors communicate via messages.

**Examples:**
- **Multicore processors (Intel, AMD CPUs)**
- **Supercomputers**
- **Cluster systems (Beowulf, IBM SP2)**
- **Cloud and distributed computing environments**
---
## **Memory Hierarchy**

In computer system design, **memory hierarchy** organizes different types of memory so that access time is minimized.  
It’s based on the concept of **locality of reference** — data or instructions recently used are likely to be used again.  
The hierarchy balances **speed, cost, and capacity** to optimize performance.

### **Types of Memory Hierarchy**
#### **1. Registers**
- Small, high-speed memory units located inside the **CPU**.
- Store the **most frequently used data and instructions**.
- Fastest access time but very small storage (usually 16–64 bits).
#### **2. Cache Memory**
- A small, fast memory placed close to the CPU.
- Temporarily stores **recently accessed data** from main memory to reduce CPU waiting time.
- Designed to **minimize access delay** by keeping the most used data ready for immediate use.
#### **3. Main Memory (RAM)**
- The **primary memory** of the system used to hold currently executing programs and data.
- Larger than cache but slower.
- Two main types:
    - **Static RAM (SRAM):** Uses flip-flops, faster, used for cache.
    - **Dynamic RAM (DRAM):** Uses capacitors, slower, needs refreshing, used as main RAM.
#### **4. Secondary Storage**
- **Non-volatile** memory for permanent data storage.
- Much larger in capacity but slower than main memory.
- Examples include **Hard Disk Drives (HDDs)** and **Solid-State Drives (SSDs)**.
#### **5. Magnetic Disk**
- Circular metal or plastic plates coated with magnetic material.
- Commonly used in computers as hard disks for frequent data storage.
- Operates at high speed and can store large volumes of information.
#### **6. Magnetic Tape**
- Plastic tape coated with magnetic material, used for **data backup**.
- Access time is slower because data is read sequentially.
- Ideal for archiving and long-term storage.
### **Memory Hierarchy Design**

The design arranges memory levels so that faster, smaller, and costlier memory is on top, while larger, cheaper, and slower memory is at the bottom.  
Frequently accessed data is stored in higher levels to improve performance.

|Level|Memory Type|Speed|Size|Cost per Bit|Example|
|---|---|---|---|---|---|
|1|Registers|Fastest|Smallest|Highest|CPU internal registers|
|2|Cache|Very Fast|Small|High|L1, L2 cache|
|3|Main Memory|Moderate|Medium|Moderate|RAM|
|4|Secondary|Slow|Large|Low|HDD, SSD|
|5|Tertiary|Slowest|Very Large|Lowest|Magnetic Tape|
![[Pasted image 20251109131457.png]]
### **Characteristics of Memory Hierarchy**
- **Capacity:** Increases from top to bottom.
- **Access Time:** Increases from top to bottom.
- **Speed:** Decreases down the hierarchy.
- **Cost per Bit:** Decreases from top to bottom.
- **Performance:** Improved when frequently used data stays in faster memory.
### **In Short**
> **Registers → Cache → Main Memory → Secondary → Magnetic Tape**  
> As we move downward: **Speed ↓ | Capacity ↑ | Cost ↓**

### **Example**
When the CPU needs data, it first checks the **registers**, then **cache**, then **main memory**, and finally **secondary storage** if not found — ensuring efficient and fast access.

---
## **Parallelism(Parallel Computing)

Parallel computing is a type of computation in which **many processors work together simultaneously** to solve a problem.  
Instead of performing one task at a time, the problem is divided into **smaller sub-tasks**, and each processor executes a part of it **at the same time**.  
The goal is to **increase processing speed and efficiency**.
### **Need for Parallel Computing:**
- To handle **large and complex problems** faster.
- To make better use of **multi-core processors** and system resources.
- To **reduce execution time** and improve performance.
- Used in areas like **scientific simulations, AI, image processing, and HPC**.
### **Working Principle:**
The main task is divided into smaller tasks (sub-problems).  
These tasks are executed **concurrently** on multiple processors.  
After completion, the results of all sub-tasks are combined to form the final output.

---
## **Types of Parallel Computing**

Parallel computing allows multiple processors or cores to **work together at the same time** to solve a problem faster.  
It mainly includes **Data Parallelism**, **Task Parallelism**, **Bit-Level Parallelism**, and **Instruction-Level Parallelism (ILP).**

---

### **1. Data Parallelism**

**Definition:**  
The same operation is performed on **different parts of data** simultaneously using multiple processors.

**Example:**  
Performing addition on all array elements at once using GPU cores.

**Key Points:**
1. Same instruction executes on different data items.
2. Used in **SIMD** and **GPU** architectures.
3. Ideal for **matrix operations** or image processing.
4. All processors work **synchronously** (in step).
5. Best for **large, uniform data sets**.

### **2. Task Parallelism**
Different processors execute **different tasks or functions** on the same or different data at the same time.
**Example:**  
In a server — one thread handles user requests, another processes data, another writes to a database.
**Key Points:**
1. Different instructions operate on the same or different data.
2. Based on **MIMD** architecture.
3. Each processor runs **independently (asynchronously)**.
4. Suited for **multi-threading and distributed computing**.
5. Good for problems divided into distinct functions.
## **Compare between Data and Task Parallelism

| **Aspect**            | **Data Parallelism**                    | **Task Parallelism**                         |
| --------------------- | --------------------------------------- | -------------------------------------------- |
| **Basic Idea**        | Same task on different data             | Different tasks on same/different data       |
| **Architecture Type** | SIMD                                    | MIMD                                         |
| **Data Division**     | Large dataset divided among processors  | Tasks or functions divided among processors  |
| **Execution**         | All processors execute same code        | Each processor executes different code       |
| **Execution Type**    | Synchronous (processors work in step)   | Asynchronous (processors work independently) |
| **Communication**     | Less communication required             | More communication and synchronization       |
| **Use Cases**         | Image processing, numerical computation | Web servers, distributed systems             |
| **Efficiency**        | High for uniform data                   | High for independent tasks                   |
### **3. Bit-Level Parallelism**

**Definition:**  
Improves processor performance by allowing **multiple bits to be processed simultaneously** in a single instruction.

**Example:**  
A 64-bit CPU adds two 64-bit numbers at once instead of bit by bit.

**Key Points:**
1. Works at the **hardware level**.
2. Reduces total instruction count.
3. Speeds up arithmetic and logical operations.
4. Common in **modern 32-bit and 64-bit CPUs**.
5. Used in **cryptography, graphics, and compression**.
**Applications:**
- **Cryptography:** Parallel bitwise operations for encryption/decryption.
- **Digital Signal Processing (DSP):** Fast arithmetic operations.
- **Graphics and Multimedia Processing:** Pixel-level computations.
- **Compression Algorithms:** Bit manipulation for encoding/decoding.
- **Low-level system programming** and **hardware optimization**.
### **4. Instruction-Level Parallelism (ILP)**

**Definition:**  
Executes **multiple independent instructions** within a single CPU cycle by overlapping their stages.

**Example:**  
In pipelining  one instruction is fetched while another is decoded and another executed.

**Key Points:**
1. Works within a **single CPU**.
2. Achieved using **pipelining** and **superscalar design**.
3. Increases **instruction throughput**.
4. Avoids idle CPU stages through overlapping.
5. Improves performance without raising clock speed.

**Classification of ILP:**

- **Static ILP:**  
    In this approach, parallelism is identified by the **compiler before execution**. The compiler schedules instructions to avoid conflicts, and the CPU executes them as arranged.  
    Example: **VLIW (Very Long Instruction Word)** processors, where multiple operations are packed into a single instruction.
- **Dynamic ILP:**  
    Here, the **hardware automatically detects** which instructions can run in parallel at runtime. The processor dynamically reorders instructions to keep execution units busy.  
    Example: **Superscalar processors** like Intel Core or AMD Ryzen.
- **Pipelined ILP:**  
    The most common form, where instruction execution is **divided into stages** (Fetch, Decode, Execute, Memory, Write Back), and multiple instructions are processed simultaneously in different stages.  
    Example: Classic **5-stage RISC pipeline**.
---
## Concurrency
Concurrency is the ability of a system to **perform multiple tasks or processes during the same time period**, where tasks **overlap in execution**.  
It doesn’t mean all tasks run exactly at once (that’s parallelism) — instead, the CPU switches between them efficiently.

**Example:**  
Downloading a file, typing in a document, and listening to music at the same time.
**Characteristics:**
1. **Overlapping Execution:** Multiple tasks make progress together.
2. **Resource Sharing:** Tasks share CPU, memory, or I/O devices.
3. **Independent Execution:** Each task runs separately but may coordinate with others.
4. **Time Sharing:** The CPU switches rapidly between tasks.
5. **Synchronization Required:** Shared data must be accessed safely.
---
## Decomposition
Decomposition means **dividing a problem into smaller, manageable subtasks** that can be executed **concurrently or in parallel**.  
It’s the first step in designing any parallel program.

**Purpose:**
- To improve **performance** by dividing work.
- To ensure **load balance** among processors.
- To simplify complex problems into smaller, independent tasks.
###### **Types of Decomposition**

**a) Data Decomposition**
- The data is divided into smaller chunks.
- Each processor performs the **same operation** on a different part of data.
- Example: Dividing an image into blocks for parallel filtering.
- Used in **SIMD systems** and **GPU computing**.

**b) Functional (Task) Decomposition**
- The problem is divided into **independent functions or modules**.
- Each processor performs a **different operation**.
- Example: One task reads data, another processes it, another saves results.
- Used in **MIMD systems** and **pipelines**.
---
## Mapping
Mapping is the process of **assigning decomposed tasks to processors or cores** for execution.  
Good mapping ensures efficient use of resources and faster results.

**Goals of Mapping:**
1. **Load Balancing:** Distribute work evenly among processors.
2. **Reduced Communication:** Minimize data transfer between processors.
3. **Efficient Execution:** Prevent processor idle time.
4. **Scalability:** Maintain performance as processor count grows.
##### **Types of Mapping

 **a) Static Mapping**
- Tasks are assigned to processors **before execution**.
- Fixed assignment, simple to implement.
- Example: Each processor handles a fixed portion of data.
- **Limitation:** May cause imbalance if workloads vary.
 **b) Dynamic Mapping**
- Tasks are assigned **during execution**, based on availability or load.
- More flexible and adaptive.
- Example: Load balancing in cloud servers.
- **Used in:** Systems where task execution time is unpredictable.
---
## PRAM: 
PRAM stands for **Parallel Random Access Machine** — it’s a **theoretical model** used to design and analyze **parallel algorithms**.  
It assumes **multiple processors** working simultaneously and **sharing a single global memory** with equal access time.

#### **Key Characteristics:**
1. Consists of **multiple processors**, each with its own local registers.
2. All processors **share a common global memory**.
3. **Uniform memory access time** for all processors.
4. All processors execute instructions in **synchronous steps**.
5. Used as a **simplified model** for studying parallel algorithm performance.
### **Types of PRAM Models:**

|**Model Type**|**Description**|
|---|---|
|**EREW (Exclusive Read Exclusive Write)**|No two processors can read or write the same memory location simultaneously.|
|**CREW (Concurrent Read Exclusive Write)**|Many processors can read the same location, but only one can write at a time.|
|**ERCW (Exclusive Read Concurrent Write)**|Only one can read at a time, but multiple can write (rarely used).|
|**CRCW (Concurrent Read Concurrent Write)**|Multiple processors can both read and write the same memory location at once.|

##### **Advantages of PRAM:**
- Simple model to analyze parallel algorithms.
- Helps in **theoretical performance measurement**.
- Easy to understand synchronization and communication patterns.
##### **Limitations:**
- Not realistic — assumes **zero memory access delay** and **perfect synchronization**.
- Doesn’t model hardware limitations like **bus contention** or **cache latency**.

### **2. Difference Between UMA and NUMA**
Both UMA and NUMA are **shared-memory architectures** used in multiprocessor systems.  
They differ in how **memory is accessed and shared** among processors.
##### **UMA (Uniform Memory Access)**
- All processors share a **common physical memory** with **equal access time**.
- The system bus or interconnect provides **uniform access** to memory.
- Example: **SMP (Symmetric Multiprocessing)** systems.
##### **NUMA (Non-Uniform Memory Access)**
- Each processor has its **own local memory**, but can access others’ memory too.
- **Access time varies** — faster for local memory, slower for remote.
- Example: **Modern multi-socket servers**, high-end multicore processors.
##### **Difference Table**

| **Aspect**             | **UMA (Uniform Memory Access)**              | **NUMA (Non-Uniform Memory Access)**      |
| ---------------------- | -------------------------------------------- | ----------------------------------------- |
| **Memory Access Time** | Same for all processors                      | Depends on memory location (local/remote) |
| **Memory Sharing**     | Single shared memory module                  | Each processor has local + shared memory  |
| **Performance**        | Constant access time but limited scalability | Scalable with variable access time        |
| **Communication**      | Through common bus or interconnect           | Through high-speed interconnect links     |
| **Scalability**        | Less scalable (bus contention)               | More scalable for large systems           |
| **Cost**               | Cheaper and simpler to design                | Expensive, complex interconnect           |
| **Example**            | Dual-core CPUs, small SMPs                   | Multi-socket Xeon or AMD EPYC systems     |

---
### **Multithreading**

**Definition:**  
Multithreading means running **multiple threads** (smaller units of a process) **within a single process**
All threads share the **same memory space** but execute **independent tasks** concurrently
**Example:**  
A web browser one thread handles user input, another loads web pages, another plays videos.

**Key Points:**
1. Multiple threads share the same process memory.
2. Threads run **concurrently** within one process.
3. Lightweight and faster to create or switch.
4. Easier for tasks that need to share data.
5. If one thread crashes, it can affect the entire process.
### **Multiprocessing**

**Definition:**  
Multiprocessing means using **multiple processors or cores** to execute **different processes** at the same time.  
Each process runs independently with its **own memory space**.

**Example:**  
Running multiple applications simultaneously — like editing a document while rendering a video.

**Key Points:**
1. Each process has its own memory and resources.
2. Processes run **in parallel** on different CPUs or cores.
3. More reliable — one process crash doesn’t affect others.
4. Better for heavy, CPU-bound tasks.
5. Requires more system resources and overhead.
### **Difference Between Multithreading and Multiprocessing**

|**Aspect**|**Multithreading**|**Multiprocessing**|
|---|---|---|
|**Basic Unit**|Multiple threads in a single process|Multiple independent processes|
|**Memory Space**|Shared among threads|Separate for each process|
|**Execution Type**|Concurrent (time-shared)|Parallel (truly simultaneous)|
|**Communication**|Easier (shared memory)|Harder (inter-process communication needed)|
|**Speed**|Faster context switching|Slower due to process isolation|
|**Reliability**|One thread crash may affect others|One process crash doesn’t affect others|
|**Use Case**|Lightweight, I/O-bound tasks|Heavy, CPU-bound computations|
|**Example**|Web browsers, servers|Video editing, scientific computing|

---
## **Shared Memory
The Shared Memory Model** is a **parallel programming model** in which **multiple processors or threads share a common physical memory space**.  
They communicate and coordinate by **reading and writing shared variables** in that memory rather than passing messages.

### **Working Principle:**
- A **single global memory** is accessible by all processors.
- Each processor can read and write to this memory.
- To prevent conflicts, **synchronization mechanisms** (like semaphores, mutexes, and locks) are used.
- The system ensures **cache coherence** so that all processors see consistent data.
### **Characteristics:**

1. **Common address space** shared among all processors.
2. **Fast communication** since no message passing is needed.
3. **Synchronization required** to manage simultaneous access.
4. Works best on **closely coupled systems** (like multicore CPUs).
5. Based on architectures such as **UMA (Uniform Memory Access)** and **NUMA (Non-Uniform Memory Access)**.
### **Use Cases:**

1. **Inter-Process Communication (IPC):**
    - Two or more processes use shared memory to **exchange data directly** without the need for message passing.
    - Example: Communication between system daemons or background services.
2. **Parallel Processing:**
    - Multiple processors or threads **share and modify data** simultaneously in the same memory space.
    - Improves computation speed in **scientific or engineering simulations**.
3. **Databases:**
    - Shared memory acts as a **common cache**, allowing faster read/write operations for concurrent users.
    - Example: PostgreSQL and Oracle use shared memory for caching and buffer management.
4. **Graphics and Multimedia Applications:**
    - Enables **CPU and GPU** to access data concurrently for tasks like video rendering or image processing.
    - Reduces data transfer time between components.
5. **Distributed Systems:**
    - Multiple machines share access to a **common memory region** or virtual shared space.
---
## Distributed Memory Model

The **Distributed Memory Model** is a **parallel programming model** where each processor has its **own private local memory**.  
Processors do **not share memory directly** — instead, they communicate by **sending and receiving messages** over a network.
#### **Working Principle:**
- Each processor has its **own local memory** that only it can access.
- To share data, processors use **message passing** (like MPI — Message Passing Interface).
- The program is divided into tasks, each with its own data, and processors **exchange messages** to coordinate work.
- Commonly used in **clusters, grids, and supercomputers**.
### **Characteristics:**
1. **Private memory space** for each processor.
2. **Communication via message passing**, not shared memory.
3. **No cache coherence issues**, since memory is local to each processor.
4. **Scalable**, as adding more processors increases total memory.
5. Ideal for **loosely coupled systems** (like cluster computing).
---
## **Varieties of Distributed Memory Model**

Distributed memory systems can vary based on how the processors are connected and how communication is managed:

---

#### **A) On-Chip Memory**
- The **CPU’s chip** itself contains all of the required data and memory.
- **Memory and address lines** have a **direct link**, ensuring very fast access.
- Provides **high speed and low latency**, but is **extremely expensive and complex** to design.
- Common in **advanced multi-core processors** and **SoCs (System on Chip)**.
#### **B) Microprocessor Based on Buses**
- Memory and CPU are connected via a **bus — a network of parallel wires**.
- Processors follow a **standardized access protocol** to manage memory usage.
- **Algorithms control memory access**, preventing multiple systems from using the same memory simultaneously.
- **Cache memory** is used to reduce **bus traffic** and improve performance.
- Common in **bus-based multiprocessor systems**.
#### **C) Microprocessor with Rings**
- There is **no centralized memory** — each node has its **own local memory**.
- All nodes are connected in a **ring topology**, and **token passing** is used to control memory access.
- Only one node at a time can access the shared address line.
- Reduces contention but increases **latency** for distant nodes.
- Common in **ring-based distributed systems** and some **networked architectures**.
---
## **Performance Measures in Parallel Computing**

### **1. Speedup (S)**

- Shows how much **faster** a parallel program runs compared to a sequential one.

- **Formula:**
    S(p)=T(1)/T(p)
    where **T(1)** = time on 1 processor, **T(p)** = time on p processors.
- **Ideal case:** S(p) = p (perfect speedup).
- **Example:** 100s (1 CPU) → 25s (4 CPUs), S = 4.
### **2. Efficiency (E)**
- Measures **how well processors are utilized**.
- **Formula:**
    E(p)=S(p)/p
- High efficiency means processors are doing useful work.
- **Ideal value:** E = 1 (100%).
### **3. Scalability**

- Tells how well a system **maintains performance** as processors or problem size increase.
- **Types:**
    - **Strong scalability:** Fixed problem size, more processors → faster.
    - **Weak scalability:** Problem size grows with processors → stable performance.
- A **highly scalable system** keeps efficiency and speedup high when expanded.
- --
## **Message Passing Interface (MPI)**
**MPI** is a **standard specification** for message-passing used to write **parallel programs** for **distributed memory systems**.
### **Important Points
- Provides a **library of routines** for **process communication**.
- Used where each processor has its **own local memory**.
- Processes **exchange data** by explicitly **sending and receiving messages**.
- Supports both **point-to-point** and **collective communication**.
- Ensures **portability and scalability** across platforms.
- Commonly used in **scientific and engineering applications**.
---
## **Methods of MPI**
**1. Point-to-Point Communication:**
- Data is exchanged **between two specific processes** (one sender, one receiver).
- Requires explicit **send** and **receive** calls.
- Example functions:
    - `MPI_Send()` – Sends a message.
    - `MPI_Recv()` – Receives a message.
- Used for **direct communication** between processors.
**2. Collective Communication:*
- Involves **a group of processes** working together to exchange data.
- Data can be **broadcast, gathered, or scattered** among processes.
- Example functions:
    - `MPI_Bcast()` – Broadcasts data from one process to all.
    - `MPI_Scatter()` – Distributes different pieces of data to multiple processes.        
    - `MPI_Gather()` – Collects data from multiple processes to one.
- Used for **synchronization** and **data sharing** in parallel tasks.