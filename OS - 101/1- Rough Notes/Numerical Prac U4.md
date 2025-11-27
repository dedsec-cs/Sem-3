**Extracted Questions (without solutions):**

1.  Consider a logical address space of eight pages of 1024 words each, mapped onto a physical memory of 32 frames then:
    a) How many bits are in logical address?
    b) How many bits are in physical address?
    c) The logical address is divided into two parts: the page address and then the file address.

2.  Given memory partitions of 100 K, 500 K, 200 K, 300 K and 600 K (in order), How would each of the first fit, best fit and worst fit algorithms place processes of 212 K, 417 K, 112 K and 426 K? Which algorithm makes the most efficient use of memory?

3.  Consider the reference string: 2, 3, 2, 4, 5, 2, 3, 2, 6, 2, 3, 2, 1, 2, 3. How many page faults would occur for FIFO, Optimal, and LRU page replacement algorithms? Assume a certain number of frames are available.


That's a fantastic idea! Numerical problems are the best way to solidify your understanding of Memory Management and Page Replacement Algorithms.

Here are **five examples** covering Address Space Calculation, Contiguous Allocation, and Page Replacement Algorithms.

---

## 1. 🔢 Address Space Calculation (Paging)

### Problem Statement

A computer system uses a **Logical Address Space** of **$2^{18}$ bytes**. The system uses **Paging** with a **Page Size** of **8 KB**.

1.  How many bits are in the Logical Address?
2.  How many pages are in the Logical Address Space?
3.  How many bits are needed for the Page Offset?

### Solution

The Logical Address (LA) is composed of the **Page Number (P)** and the **Page Offset (D)**.

#### A. Bits in the Logical Address

The total size of the logical address space is given as $2^{18}$ bytes.

$$\text{Logical Address Bits} = \log_2(\text{Logical Address Space Size})$$
$$\text{Logical Address Bits} = \log_2(2^{18})$$

$$\text{Logical Address requires **18 bits**}$$

#### B. Bits for the Page Offset (D)

The Page Size is 8 KB.

$$\text{Page Size} = 8 \text{ KB} = 8 \times 1024 \text{ bytes}$$
$$\text{Page Size} = 2^3 \times 2^{10} = 2^{13} \text{ bytes}$$
$$\text{Offset Bits (D)} = \log_2(\text{Page Size}) = \log_2(2^{13})$$

$$\text{Page Offset (D) requires **13 bits**}$$

#### C. Number of Pages

The number of pages is determined by dividing the total space by the page size.

$$\text{Page Number Bits (P)} = \text{LA Bits} - \text{Offset Bits} = 18 - 13 = 5 \text{ bits}$$
$$\text{Number of Pages} = 2^{\text{P}} = 2^5$$

$$\text{The Logical Address Space contains **32 pages**}$$

---

## 2. 📝 Contiguous Allocation: Best Fit

### Problem Statement

Given the following free memory holes and incoming processes, determine the final state of the holes after allocating processes using the **Best Fit** algorithm.

| Hole ID | Size (KB) |
| :---: | :---: |
| H1 | 400 |
| H2 | 180 |
| H3 | 600 |
| H4 | 512 |
| H5 | 250 |

| Process ID | Memory Requested (KB) |
| :---: | :---: |
| P1 | 212 |
| P2 | 417 |

### Solution

**Best Fit** finds the **smallest hole that is large enough** to satisfy the request.

#### A. Allocate P1 (212 KB)

1.  **Candidates (Hole - Request):** H1 (188), H3 (388), H4 (300), H5 (38).
2.  **Best Fit:** H5 (250 KB), as it leaves the smallest remainder (38 KB).
3.  **Result:** P1 allocated to H5. H5 size reduces to $250 - 212 = 38$ KB.

#### B. Allocate P2 (417 KB)

1.  **Candidates (Hole - Request):** H1 (400 - too small), H3 (600 - 183), H4 (512 - 95).
2.  **Best Fit:** H4 (512 KB), as it leaves the smallest remainder (95 KB).
3.  **Result:** P2 allocated to H4. H4 size reduces to $512 - 417 = 95$ KB.

### Final State of Free Holes

| Hole ID | Original Size (KB) | Process ID | New Size (KB) |
| :---: | :---: | :---: | :---: |
| H1 | 400 | Free | 400 |
| H2 | 180 | Free | 180 |
| H3 | 600 | Free | 600 |
| **H4** | **512** | **P2 (417)** | **95** |
| **H5** | **250** | **P1 (212)** | **38** |

---

## 3. 💣 Fragmentation Calculation (Fixed Partitioning)

### Problem Statement

A system uses **Fixed Partitioning** with four partitions: 500 KB, 400 KB, 300 KB, and 200 KB. The incoming processes are P1 (450 KB), P2 (200 KB), P3 (150 KB), and P4 (250 KB). All processes are allocated in the order P1 $\rightarrow$ P2 $\rightarrow$ P3 $\rightarrow$ P4. Calculate the total internal fragmentation.

### Solution

In Fixed Partitioning, a process is placed in the smallest *adequate* partition, but the entire partition is consumed, leading to internal fragmentation.

| Process | Requested (KB) | Allocated Partition (KB) | Internal Fragmentation (KB) |
| :---: | :---: | :---: | :---: |
| **P1** | 450 | 500 | $500 - 450 = 50$ |
| **P2** | 200 | 200 | $200 - 200 = 0$ |
| **P3** | 150 | 300 (smallest available $\geq$ 150) | $300 - 150 = 150$ |
| **P4** | 250 | 400 (only remaining $\geq$ 250) | $400 - 250 = 150$ |
| **Total** | | | **350** |

$$\text{Total Internal Fragmentation} = 50 + 0 + 150 + 150 = 350 \text{ KB}$$

---

## 4. 🔄 Page Replacement: FIFO Algorithm

### Problem Statement

Consider a page reference string: $\text{7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1}$.
The memory has **3 available frames**. Calculate the number of **Page Faults** using the **FIFO (First-In, First-Out)** algorithm.

### Solution

FIFO replaces the page that arrived in the frame first (the oldest page). 

| Reference | Frame 1 | Frame 2 | Frame 3 | Page Fault? | Replaced Page |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **7** | **7** | - | - | **Y** | - |
| **0** | 7 | **0** | - | **Y** | - |
| **1** | 7 | 0 | **1** | **Y** | - |
| 2 | **2** | 0 | 1 | **Y** | 7 |
| 0 | 2 | 0 | 1 | N | - |
| 3 | 2 | **3** | 1 | **Y** | 0 |
| 0 | 2 | 3 | **0** | **Y** | 1 |
| 4 | **4** | 3 | 0 | **Y** | 2 |
| 2 | 4 | **2** | 0 | **Y** | 3 |
| 3 | 4 | 2 | **3** | **Y** | 0 |
| 0 | **0** | 2 | 3 | **Y** | 4 |
| 3 | 0 | 2 | 3 | N | - |
| 2 | 0 | 2 | 3 | N | - |
| 1 | 0 | **1** | 3 | **Y** | 2 |
| 2 | 0 | 1 | **2** | **Y** | 3 |
| 0 | 0 | 1 | 2 | N | - |
| 1 | 0 | 1 | 2 | N | - |
| 7 | **7** | 1 | 2 | **Y** | 0 |
| 0 | 7 | **0** | 2 | **Y** | 1 |
| 1 | 7 | 0 | **1** | **Y** | 2 |

$$\text{Total Number of Page Faults} = 3 + 12 = **15**$$

---

## 5. ⏱️ Page Replacement: LRU Algorithm

### Problem Statement

Using the same page reference string: $\text{7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1}$.
The memory has **3 available frames**. Calculate the number of **Page Faults** using the **LRU (Least Recently Used)** algorithm.

### Solution

LRU replaces the page that has not been used for the longest time in the past. 

| Ref | Frame 1 | Frame 2 | Frame 3 | Fault? | LRU Page (to replace) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **7** | **7** | - | - | **Y** | - |
| **0** | 7 | **0** | - | **Y** | - |
| **1** | 7 | 0 | **1** | **Y** | - |
| 2 | **2** | 0 | 1 | **Y** | 7 |
| 0 | 2 | 0 | 1 | N | - |
| 3 | 2 | 0 | **3** | **Y** | 1 |
| 0 | 2 | 0 | 3 | N | - |
| 4 | **4** | 0 | 3 | **Y** | 2 |
| 2 | 4 | **2** | 3 | **Y** | 0 |
| 3 | 4 | 2 | 3 | N | - |
| 0 | **0** | 2 | 3 | **Y** | 4 |
| 3 | 0 | 2 | 3 | N | - |
| 2 | 0 | 2 | 3 | N | - |
| 1 | 0 | 2 | **1** | **Y** | 3 |
| 2 | 0 | 2 | 1 | N | - |
| 0 | 0 | 2 | 1 | N | - |
| 1 | 0 | 2 | 1 | N | - |
| 7 | **7** | 2 | 1 | **Y** | 0 |
| 0 | 7 | **0** | 1 | **Y** | 2 |
| 1 | 7 | 0 | 1 | N | - |

$$\text{Total Number of Page Faults} = 3 + 9 = **12**$$
