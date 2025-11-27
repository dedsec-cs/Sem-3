## 💾 Disk Management & Storage

### Boot Block

The **Boot Block** is the first physical block (sector) on a disk drive.

* **Purpose:** It holds the essential, low-level code required to initiate the system startup process, known as the **bootstrap program (or boot loader)**.
* **Process:** When the computer is powered on, the firmware (like BIOS or UEFI) loads and executes the code found in this block. This code's job is to load the rest of the Operating System kernel into memory.
* **Condition:** If the disk is not intended to contain an OS, this block may be empty or contain non-functional placeholder code.

---

### Free Space Management

The OS must track which disk blocks are currently allocated to files and which blocks are **free** and available for new files.

#### 1. Bit Vectors (Bit Map)

* **Implementation:** The free space list is represented as a **bit array** or **bit vector**.
* **Logic:** Each disk block is represented by a single bit.
    * If the bit is **1**, the corresponding block is **free**.
    * If the bit is **0**, the block is **allocated** (used).
* **Pros:** Easy to understand and relatively simple to find the first free block (just scan for the first '1').
* **Cons:** If the disk is very large (e.g., 1 TB with 4 KB blocks), the bit map itself becomes very large and must be stored in memory or frequently read from disk.

#### 2. Linked List

* **Implementation:** All the **free disk blocks are chained together** using pointers to form a single **linked list**.
* **Logic:** A special location on the disk (and cached in memory) holds a pointer to the **first free block**. That first block contains the address of the second free block, and so on.
* **Pros:** Requires very little space to store the list pointer.
* **Cons:** Finding $N$ contiguous free blocks requires traversing the list sequentially, which is very slow.

#### 3. Grouping

* **Implementation:** A modification of the linked list approach designed to speed up search time.
* **Logic:** The first free block is used to store the addresses of the next **$N$ free blocks**.
    * The first $N-1$ of these blocks are truly free.
    * The **$N^{th}$ block** contains the addresses of the next set of $N$ free blocks.
* **Pros:** Allows the OS to find the addresses of a large number of free blocks **quickly** with a single disk read, reducing I/O operations for finding free space.

---

### RAID (Redundant Array of Independent Disks)

**RAID** is a storage virtualization technology that combines multiple physical disk drives into one or more logical units for the purposes of **data redundancy, performance improvement, or both.**

* **Original Acronym:** Redundant Array of **Inexpensive** Disks.
* **Modern Acronym:** Redundant Array of **Independent** Disks.
* **Core Benefit:** Provides the ability to **survive one or more drive failures** (depending on the level used) while maintaining data accessibility and high throughput.

#### RAID Levels

| RAID Level | Technique | Redundancy | Key Use |
| :---: | :---: | :---: | :---: |
| **RAID 0** | **Stripping** (Data broken into blocks and written across multiple disks) | **None** | High read/write speed (performance only). |
| **RAID 1** | **Mirroring** (Data duplicated exactly on two or more disks) | **100%** | Excellent redundancy, moderate speed. |
| **RAID 3** | Byte-level Stripping + **Dedicated Parity** | Single disk failure | Good for large block sequential reads/writes. |
| **RAID 5** | Block-level Stripping + **Distributed Parity** | Single disk failure | Best general-purpose, good balance of speed and redundancy. |
| **RAID 6** | Block-level Stripping + **Dual Distributed Parity** | **Two** disk failures | High redundancy, lower write performance. |
| **RAID 1+0 (RAID 10)** | **Mirroring (RAID 1)** then **Stripping (RAID 0)** | High | Best performance *and* redundancy (can survive multiple simultaneous failures). |
| **RAID 0+1** | **Stripping (RAID 0)** then **Mirroring (RAID 1)** | Medium | Less redundant than RAID 1+0 (loses the entire array if one disk fails in a mirrored set). |
| **RAID 2** | Bit-level Stripping + **Hamming Code** | Single disk failure | Obsolete; complex and expensive hardware. |
| **RAID 4** | Block-level Stripping + **Dedicated Parity** | Single disk failure | Similar to RAID 5, but dedicated parity disk is a performance bottleneck. |

---

## 🗂️ File Systems

A **File System** is the method and data structure an Operating System uses to control how data is stored and retrieved on a storage device.

* **Definition:** Permits users to create logical data collections called **files** with desirable properties.
* **Desirable Properties:**
    * **Long-term existence:** Files persist on secondary storage.
    * **Sharable:** Files have names and **access permissions** to permit controlled sharing between processes.
    * **Structure:** Files can have an internal organization (like a sequence of bytes or records) useful for applications.

### File Attributes

The metadata associated with a file, maintained by the file system:

1.  **Name:** The symbolic name used by humans.
2.  **Identifier:** A unique, non-human-readable tag (like an inode number) used internally by the OS.
3.  **Type:** The format of the file (e.g., text, executable, image).
4.  **Location:** A pointer to where the file's data blocks reside on the disk.
5.  **Size:** The current size and possibly the maximum allowable size.
6.  **Protection:** Access control information (read, write, execute permissions).
7.  **Date & Time:** Creation, last modification, and last access times.

### Operations Performed on File Systems

The standard set of functions provided by the OS kernel for manipulating files:

1.  **Create:** Allocate space and create the initial directory entry.
2.  **Delete:** Release file space and remove the directory entry.
3.  **Open:** Transfer file metadata (attributes) from disk to main memory for fast access.
4.  **Close:** Transfer modified metadata back to disk and remove the file from memory tables.
5.  **Read:** Move data from the file to the user process's buffer.
6.  **Write:** Move data from the user process's buffer to the file.

### File Organization Methods

This refers to how records are arranged *within* a file, which determines access methods.

1.  **Sequential File Organization:** Records are stored and accessed strictly in a **sorted order** based on a **key field**. Retrieval requires searching sequentially from the beginning.
2.  **Serial File Organization:** Records are stored and accessed **one after another** in the order they were written, with no required sorted order.
3.  **Random (or Direct) File Organization:** Records are stored randomly but can be **accessed directly** using a **record key** (e.g., using a hash function) to immediately determine the record's storage location.
4.  **Ordered-Sequential File Organization (Indexed Sequential):** Similar to sequential, but an **index** is maintained to quickly locate the starting point of records, enabling faster searches.

### Access Mechanisms

These are the ways a program can read or write data within a file:

1.  **Sequential Access:** Read/write proceeds in order, from the beginning to the end (like reading a book).
2.  **Direct Access:** Read/write can jump to any arbitrary block address within the file (like accessing an array element).
3.  **Indexed Access:** A separate index structure is searched to find a pointer to the desired data block, combining the speed of direct access with the organization of sequential data.

---

## 📂 Directory

The **Directory** is the file system structure that provides the mapping between human-readable **file names** and their internal **file attributes** (metadata).

* **Function:** It acts as a **symbol table** that translates a file name provided by a user into its directory entry, which contains the necessary information for the OS to locate the file's data.

### Directory Implementation

1.  **Linear List:**
    * **Structure:** A list of file names, each paired with a pointer to its data blocks (or its file identifier/inode).
    * **Search:** Uses a **linear search** (checking entries one by one) to find a particular entry.
    * **Pros:** Simple to program and implement.
    * **Cons:** **Time-consuming** to execute, especially with many files.

2.  **Hash Table:**
    * **Structure:** A hash table is used to dramatically **decrease directory search time**.
    * **Logic:** A hash function takes the file name and computes an index (or pointer) directly to the file name's location in the linear list.
    * **Pros:** Insertion and deletion are straightforward, and search time is typically **O(1)** (constant time), making it very fast.

### Operations Performed on a Directory

These operations manage the directory structure itself:

1.  **Searching a file:** Finding the directory entry corresponding to a given file name.
2.  **Create a file:** Adding a new entry to the directory.
3.  **Delete a file:** Removing an entry from the directory.
4.  **Rename a file:** Modifying the name field in the directory entry.
5.  **List directory:** Reading and displaying all entries (file names and attributes) in the directory.