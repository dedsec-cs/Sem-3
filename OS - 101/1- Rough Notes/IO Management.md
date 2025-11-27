These notes provide a comprehensive overview of **I/O Management and Disk Scheduling**, which are essential for the Operating System (OS) to efficiently handle data transfer between the CPU and the external world.

---

## ⚙️ I/O Management

**I/O (Input/Output) devices** are the interfaces that allow the computer's functional units (like the CPU and Memory) to communicate with the external environment or other electronic equipment. **Inputs** are signals received, and **Outputs** are signals sent.

### Categories of I/O Devices

I/O devices are typically categorized based on their communication partner:

1.  **Human-Readable:** Designed for direct interaction with a user.
    * *Examples:* **Printers** (output), **Keyboard** (input), Mouse, Display screens.
2.  **Machine-Readable:** Designed for communication with electronic equipment or storage media.
    * *Examples:* **Disk and tape drives**, Sensors, Controllers.
3.  **Communication:** Designed for interaction with remote devices or networks.
    * *Examples:* **Digital drivers**, Modems, Network Interface Cards (NICs).

---

### Techniques / Organization of I/O Function

These techniques dictate how the CPU coordinates data transfer with the I/O module (the hardware interface for the device). The efficiency of I/O depends heavily on which technique is used, particularly regarding how much the CPU is involved.

1.  **Programmed I/O (Polling):**
    * **Control:** Takes place under the **direct, continuous control of the CPU**.
    * **Process:** The CPU issues a command and then **waits (polls)** for the I/O module to complete the operation. The CPU is essentially idle during this wait time.
    * **Drawback:** Very **inefficient** as it ties up the CPU resources for slow I/O operations.

2.  **Interrupt-Driven I/O:**
    * **Control:** The I/O module manages the I/O operation independently.
    * **Process:** The CPU issues a command and then **continues to execute** instructions from the same (or another) process (**non-blocking**). When the I/O operation is complete, the I/O module generates an **interrupt** to signal the CPU.
    * **Benefit:** Much more efficient than Programmed I/O because the CPU is freed to do other work during the I/O time.

3.  **Direct Memory Access (DMA):**
    * **Control:** A specialized module, the **DMA controller**, handles the data exchange.
    * **Process:** The CPU only sends the DMA module a request to transfer a **block of data**. The DMA module performs the entire transfer between the I/O device and memory **without involving the CPU**. The CPU is interrupted **only after the entire block has been transferred**. 
    * **Benefit:** This is the most efficient method for large data transfers (like disk reads), as it minimizes CPU intervention, only requiring the CPU's attention at the start and end of the transfer.

---

## 🗄️ Buffer and I/O Buffering Techniques

A **buffer** is a reserved region of memory used to **temporarily hold data** while it is being transferred between two different systems (e.g., a disk device and an application program).

* **Primary Purpose:** To cope with the **speed mismatch** between the data producer (often a slow I/O device) and the data consumer (often a fast CPU/application).
* **Secondary Purpose:** To provide **adaptations for different data transfer sizes** (e.g., reading data in 512-byte chunks from a disk and providing it to an application that processes 1024-byte records).

### I/O Buffering Techniques

1.  **Single Buffering:**
    * The OS assigns a **single system buffer** for the I/O operation.
    * The OS can perform **"reading ahead"** (input transfer) into the system buffer while the user process is processing the *previous* block, reducing waiting time.
2.  **Double Buffering (Buffer Swapping):**
    * Uses **two system buffers** that work in tandem.
    * Data in **one buffer are being processed** by the CPU while the **next set of data is read into the other buffer** by the I/O module.
    * This technique allows **I/O and processing to overlap**, significantly speeding up streaming data applications.
3.  **Circular Buffering:**
    * Used when **more than two buffers** are needed (e.g., for very fast devices or complex concurrent applications).
    * The collection of buffers is managed in a **circular queue**, allowing the producer (I/O) and consumer (CPU) to work asynchronously without waiting for each other, as long as the circle isn't completely full or empty.

---

### Services Provided in Kernel I/O

The OS **Kernel** manages the core I/O functionality, providing a uniform interface for applications and managing hardware complexities. Key services include:

1.  **I/O Scheduling:** Deciding the order in which requests from multiple processes are serviced (e.g., disk scheduling).
2.  **Buffering:** Managing the temporary memory regions for data transfer.
3.  **Caching:** Storing copies of frequently accessed data in a fast memory location (RAM) to avoid slow I/O reads (e.g., Disk Cache).
4.  **Spooling (Simultaneous Peripheral Operations On-Line):** Holding output data for devices that cannot interleave data from multiple users (e.g., printing jobs are held in a spool directory until the printer is ready).
5.  **Error Handling:** Detecting, reporting, and recovering from hardware or data transfer errors.

---

## 💽 Disk Scheduling Algorithms

The primary role of disk scheduling is to **minimize disk seek time**—the time it takes for the disk arm to move to the cylinder containing the requested track. By logically ordering pending requests, the OS can improve disk performance and throughput. 

### 1. FCFS Scheduling (First Come First Serve)

* **Principle:** Services requests in the exact **order they arrive**.
* **Pros:** Fair and easy to implement.
* **Cons:** Does not minimize seek time. If requests are scattered across the disk, the head will frequently move back and forth across the entire disk, leading to **poor performance**.

![[Pasted image 20251121072459.png]]
![[Pasted image 20251121072506.png]]

### 2. SSTF Scheduling (Shortest Seek Time First)

* **Principle:** Selects the request that is **closest** to the current position of the disk head.
* **Pros:** Significant improvement in average seek time over FCFS. High throughput.
* **Cons:** Can lead to **starvation**, where requests far from the current head position may never be serviced if a stream of new, closer requests keeps arriving.

![[Pasted image 20251121072521.png]]

### 3. SCAN Scheduling (Elevator Algorithm)

* **Principle:** The disk arm moves in **one direction**, servicing all requests in its path, until it reaches the **end of the disk**. It then **reverses direction** and services requests on the way back.
* **Pros:** Prevents starvation and provides a good average response time, as the head keeps moving across the entire disk surface like an elevator.
* **Cons:** Favors requests near the middle of the disk. Requests waiting just behind the direction change have the longest wait time.

### 4. C-SCAN Scheduling (Circular - SCAN)

* **Principle:** An improved version of SCAN that provides a more uniform wait time. The head moves from one end of the disk to the other, servicing requests in one direction only.
* **Return Trip:** After reaching the end, it immediately **returns to the starting end without servicing any requests** (a fast, non-service seek).
* **Pros:** Treats all cylinders more equally than SCAN, ensuring requests are serviced almost once per full scan cycle.

### 5. LOOK Scheduling (A Practical SCAN)

* **Principle:** Similar to SCAN, but instead of moving all the way to the physical end of the disk, the head only moves to the **last request** in the current direction.
* **Action:** When it reaches the last request in that direction, it immediately **reverses direction**.
* **Pros:** Prevents the wasted seek time of moving to the absolute end of the disk when there are no requests there, making it more efficient than the standard SCAN algorithm.