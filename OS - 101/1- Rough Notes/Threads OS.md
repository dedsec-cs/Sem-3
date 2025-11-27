# Thread

- **Component of Process or Lightweight Process**: A thread is the smallest unit of execution within a process, often called a "lightweight process" because it shares the process’s resources but executes independently. Think of a process as a house and threads as workers inside, each doing a specific task.
- **Provides a Way to Improve Application Performance Through Parallelism**: Threads allow multiple tasks to run concurrently within a process, speeding up applications. For example, a web browser can load a webpage, play a video, and handle user clicks simultaneously using threads.
- **Project Group System for College Students**: Imagine a college project group (PG) system where students (threads) work on a group project (process). Each student handles a specific task (e.g., coding, designing), but they share common resources like the project’s data and tools.

|**Shared Among Threads**|**Unique for Each Thread**|
|---|---|
|**Code Section**: The program code (instructions) shared by all threads. E.g., a browser’s rendering code is used by all its threads.|**Thread ID**: A unique identifier for each thread. E.g., Thread-1 for loading a webpage, Thread-2 for playing audio.|
|**Data Section**: The process’s data (e.g., variables, memory) shared by threads. E.g., a browser’s cache shared by all threads.|**Register Set**: Each thread has its own CPU registers (e.g., to store temporary data during execution).|
|**OS Resources**: Resources like memory or CPU allocated to the process, shared by threads. E.g., browser’s allocated RAM.|**Stack**: Each thread has its own stack for function calls and local variables. E.g., one thread’s stack tracks webpage loading, another tracks video playback.|
|**Open Files and Signals**: Files or signals (e.g., network connections) shared by threads. E.g., all browser threads share the same internet connection.|**Program Counter**: Tracks the current instruction each thread is executing. E.g., one thread is at "load image," another at "play sound."|

## Single Threaded Process

A single-threaded process has only one thread of execution, performing tasks sequentially. Think of a simple calculator app that processes one operation at a time (e.g., adding numbers).

![[Pasted image 20250910072856.png]]

- **Example**: A basic text editor where one thread handles all tasks (typing, saving, formatting). If saving a file takes time, the app freezes until it’s done.
- **Limitation**: No parallelism, so tasks can’t run concurrently, leading to slower performance for complex applications.

## Multithreaded Process

A multithreaded process has multiple threads, each performing a task concurrently within the same process. Think of a web browser where one thread loads a webpage, another plays a video, and another handles user input.

![[Pasted image 20250910072902.png]]

- **Example**: In Chrome, one thread renders a webpage, another downloads a file, and another responds to mouse clicks, all sharing the browser’s memory.
- **Advantage**: Improves performance by allowing parallel task execution and better resource use.

## Advantages of Multithreading

- **Responsiveness**: Threads keep applications responsive. E.g., in a word processor, one thread saves a file while another lets you keep typing.
- **Faster Context Switch**: Switching between threads is faster than switching between processes because threads share memory, reducing overhead. E.g., switching between browser threads is quicker than switching between Chrome and Spotify.
- **Resource Sharing**: Threads share the process’s memory and resources, saving space and enabling efficient communication. E.g., browser threads share the same cache for faster data access.
- **Economy**: Creating and managing threads is less resource-intensive than processes. E.g., creating a new thread in a browser uses less memory than launching a new app.
- **Communication**: Threads communicate easily since they share memory. E.g., one thread updates a webpage’s data, and another immediately uses it to display content.
- **Utilization of Multiprocessor Architecture**: Threads can run on multiple CPU cores simultaneously, boosting performance. E.g., a game uses one thread for graphics and another for physics, each on a different core.

## Types of Threads

**Who Manages Threads in the End? Process or OS?**

- Threads are ultimately managed by either the **process** (for user-level threads) or the **OS** (for kernel-level threads), depending on the thread type.

### User-Level Threads (ULT)

- **Definition**: Threads managed by a user-level thread library within the process, without direct OS involvement.
- **OS Doesn’t Know About These**: The OS sees the process as a single unit, unaware of its threads.
- **Characteristics**:
    - **Multithreading in User Process**: The process’s thread library handles thread creation, scheduling, and management. E.g., a Java app using a thread library.
    - **Created Without Kernel Intervention**: No OS calls, so creation is fast.
    - **Context Switch is Very Fast**: Switching threads within the process avoids kernel overhead.
    - **If One Thread is Blocked, OS Blocks Entire Process**: E.g., if a thread waits for I/O, the whole process may freeze.
    - **Generic and Can Run on Any OS**: Thread libraries are portable across systems.
    - **Faster to Create and Manage**: Less overhead since no kernel involvement.
- **Example**: A game app using a user-level thread library to manage threads for rendering and sound, running on any OS.

### Kernel-Level Threads (KLT)

- **Definition**: Threads managed directly by the OS kernel.
- **OS Knows About These**: The kernel schedules and tracks each thread individually.
- **Characteristics**:
    - **Multithreading in Kernel Process**: The OS itself can be multithreaded, managing threads for apps.
    - **Kernel Itself is Multithreaded**: The OS assigns threads to CPU cores.
    - **Context Switch is Slow**: Involves kernel intervention, adding overhead.
    - **Individual Thread Can Be Blocked**: If one thread blocks (e.g., for I/O), others in the process can still run.
    - **Specific to OS**: Thread behavior depends on the OS (e.g., Windows vs. Linux).
    - **Slower to Create and Manage**: Kernel involvement increases resource use.
- **Example**: A web server on Linux where the kernel manages threads for handling client requests.

|**User Threads**|**Kernel Threads**|
|---|---|
|Multithreading in user process|Multithreading in kernel process|
|Created without kernel intervention|Kernel itself is multithreaded|
|Context switch is very fast|Context switch is slow|
|If one thread is blocked, OS blocks entire process|Individual thread can be blocked|
|Generic and can run on any OS|Specific to OS|
|Faster to create and manage|Slower to create and manage|

## Multithreading Models

Multithreading models define how user-level threads (ULT) map to kernel-level threads (KLT) for scheduling and execution.

### Many-to-One Model

- **Description**: Multiple user-level threads map to a single kernel-level thread. The process’s thread library manages all threads, and the OS sees the process as one thread.
- **Characteristics**:
    - No true parallelism since only one kernel thread runs at a time.
    - If one user thread blocks (e.g., for I/O), the entire process blocks.
    - Fast thread creation and switching due to no kernel involvement.
- **Example**: Early Java Green Threads, where a Java app manages multiple threads internally.
- **Pros**: Low overhead, portable across OS.
- **Cons**: No parallelism, poor handling of blocking operations.
- **Diagram**:
![[Pasted image 20250910073633.png]]

### One-to-One Model

- **Description**: Each user-level thread maps to one kernel-level thread, allowing the OS to schedule each thread independently.
- **Characteristics**:
    - True parallelism on multi-core CPUs since each thread can run on a separate core.
    - If one thread blocks, others can continue.
    - Higher overhead due to kernel involvement for creation and switching.
- **Example**: Modern Windows or Linux apps, where each thread in a browser is managed by the OS.
- **Pros**: Supports parallelism, handles blocking well.
- **Cons**: Resource-intensive due to kernel overhead.
- **Diagram**:
![[Pasted image 20250910073721.png]]

### Many-to-Many Model

- **Description**: Multiple user-level threads map to multiple kernel-level threads, allowing flexibility in thread management. A thread library maps user threads to a smaller or equal number of kernel threads.
- **Characteristics**:
    - Balances parallelism and efficiency.
    - Allows some threads to block without stopping others.
    - Complex to implement but scalable for large applications.
- **Example**: Advanced OS like Solaris, where a web server maps many user threads to a few kernel threads for efficiency.
- **Pros**: Combines benefits of both models—parallelism and low overhead.
- **Cons**: Complex to manage and implement.
- **Diagram**: 
![[Pasted image 20250910073811.png]]