Page  59  
Structure  of the Page  Table                       
 One more bit is attached to each entry in the page table: a valid -invalid bit. When this bit 
is set to "valid," this value indicates that the associated page is in the process' logical - 
address  space,  and is a legal  (or valid)  page.  If the bit is set to "invalid,"  this value  indicates 
that the page is not in the process' logical -address space.  
 Illegal addresses are trapped by using the valid -invalid bit.  The  operating system sets this 
bit for each page to allow or disallow accesses to that page.  
 
(Valid  (v) or invalid  (i) bit in a page  table)  
 
 
There  are different  structures  of page  table  described  as follows:  
1. Hierarchical Page table:  When the number of pages is very high, then the page table 
takes large amount of memory space. In such cases, we use multilevel paging  scheme  for 
reducing  size  of page  table.  A simple  technique  is a two-level  page  table.  Since  the page  table 
is paged,  the page  number  is further  divided  into  parts:  page  number  and page  offset.  Thus, 
a logical address is as follows:  
 
Where p i is an index into the outer page table, and p2 is the displacement within the page of 
the outer page table.  
Two -Level  Page -Table  Scheme:  
 
 
 
 
 
 
 
 


Page  60  
                     
 
Address  translation  scheme  for a two-level  paging  architecture:  
 
 
2. Hashed  Page  Tables:  This  scheme  is applicable  for address  space  larger  than  32bits.  In 
this scheme, the virtual page number is hashed into a page table. This page table contains a 
chain of  elements hashing to the same location. Virtual page numbers are compared in this 
chain searching for a match. If a match is found, the corresponding physical frame is 
extracted.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


Page  61      
    
3. Inverted  Page Table : 
 One  entry  for each  real  page  of memory.  
 Entry consists  of the virtual address  of the page stored in  that real  memory location, with 
information about the process that owns that page.  
 Decreases  memory  needed  to store  each  page  table,  but increases  time  needed  to search 
the table when a page reference occurs.  
 
Shared  Pages  
Shared  code  
 One copy of  read -only (reentrant) code shared among processes (i.e., text editors,  
compilers, window systems).  
 Shared  code  must  appear  in same  location  in the logical  address  space  of all processes.  
Private  code  and  data  
 Each  process  keeps  a separate  copy  of the code  and  data.  
 The  pages  for the private  code  and  data  can appear  anywhere  in the logical  address  space.  
 
SEGMENTATION   
Segmentation  is a memory -management  scheme  that  supports  user  view  of memory.  A 
program  is a collection  of segments.  A segment  is a logical  unit  such  as: main  program,  
 
 


Page  62  
                     
procedure, function, method, object, local variables, global variables, common block,  stack, 
symbol table, arrays etc.  
A logical -address space is a collection of segments. Each segment has a name and a 
length. The user specifies each address by two quantities: a segment name/number and an 
offset.  
Hence, Logical address consists of a two tuple: <segment -number, offset> 
Segment table maps two -dimensional physical addresses and each entry in table has:  
base  – contains  the starting  physical  address  where  the segments  reside  in memory. 
limit – specifies the length of the segment.  
Segment -table  base  register  (STBR)  points  to the segment  table’s  location  in memory.  
Segment -table  length  register  (STLR)  indicates  number  of segments  used  by a program.  
 
(Diagram  of Segmentation  Hardware)  
 
The  segment number is used as an index into the segment table. The offset d of the 
logical address must be between 0 and the segment  limit.  If it is not,  we trap to  the operating 
system that logical addressing attempt beyond end of segment. If this offset is legal, it is 
added to the segment base to produce the address in physical memory of  the desired byte.  
Consider  we have  five segments  numbered  from  0 through  4. The segments  are stored 
in physical memory as shown in figure. The segment table has a separate  entry  for each  
segment,  giving  start  address  in physical  memory  (or base)  and the length  of that  segment 
(or limit). For example, segment 2 is 400 bytes long and begins at location 4300.  Thus,  a 
reference to byte 53 of segment 2 is mapped onto location 4300 + 53 = 4353.  
 
 
 
 
 
 
 
 


Page  63  
                     
 
(Example  of segmentation)  
 
 
VIRTUAL  MEMORY  
Virtual memory is a technique that allows the execution of processes that may not be 
completely in memory. Only part of the program needs to be in memory for execution. It 
means that Logical address space can be much larger than physical address space. Virtual 
memory  allows  processes  to easily  share  files  and  address  spaces,  and  it provides  an efficient 
mechanism for process creation.  
Virtual memory is the separation of user logical memory from physical memory. This 
separation allows an extremely large virtual memory to be provided for programmers when 
only a smaller  physical memory is available. Virtual memory makes the  task  of programming 
much  easier,  because  the programmer  no longer  needs  to worry  about  the amount  of physical 
memory available.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 


Page  64     
   
(Diagram  showing  virtual  memory  that  is larger  than  physical  memory)  
 
Virtual  memory  can be implemented  via: 
➢ Demand  paging  
➢ Demand segmentation  
DEMAND  PAGING   
A demand -paging system is similar to a paging system with swapping. Generally, 
Processes reside  on secondary memory  (which  is usually a  disk).  When we want to execute  a 
process, we swap it into memory. Rather than swapping the entire process into memory, it 
swaps the required page. This can be done by a lazy swapper.  
A lazy swapper never swaps a page into  memory unless that page will be needed. A 
swapper manipulates entire processes, whereas a pager is concerned with the individual 
pages of a process.  
Page  transfer  Method:  When  a process  is to be swapped  in, the pager  guesses  which  pages 
will be used  before  the process  is swapped  out again.  Instead  of swapping  in a whole  process, 
the pager  brings  only  those  necessary  pages  into  memory.  Thus,  it avoids  reading  into 
memory pages that will not be used anyway, decreasing the swap time and the amount  of 
physical memory needed.  
 


Page  65  
                     
(Transfer  of a paged  memory  to contiguous  disk  space)  
Page  Table:   
➢ The valid -invalid bit scheme of Page table can be used for indicating which pages are 
currently in memory.  
➢ When this bit  is set  to "valid", this value indicates that  the associated page is both legal and  
in memory.  If the bit is set to "invalid",  this value  indicates  that  the page  either  is not valid 
or is valid but is currently on the disk.  
➢ The page -table entry for a page that is brought into memory is set as usual, but the page - 
table entry for a page that is not currently in memory is simply marked invalid, or 
contains the address of the page on disk.  
 
(Page  table  when  some  pages  are not in main  memory)  
 
When  a page  references an  invalid  page,  then it is  called  Page  Fault . It means  that  page is 
not in main memory. The procedure for handling page fault is as follows:  
1. We check  an internal  table  for this process,  to determine  whether  the reference  was  a 
valid or invalid memory access.  
2. If the reference was invalid, we terminate the process. If it was valid, but we have not 
yet brought in that page in to memory.  
3. We find  a free  frame  (by taking  one from  the free -frame  list).  
4. We schedule  a disk  operation  to read  the desired  page  into  the newly  allocated  frame.  
5. When  the disk  read  is complete,  we modify  the internal  table  kept  with  the process  and 
the page table to indicate that the page is now in memory.  
6. We restart  the instruction that  was interrupted  by the illegal  address trap.  The process 
can now access the page as though it had always been in memory.  
 


Page  66  
                     
 
(Diagram  of Steps  in handling a  page  fault)  
Note: The pages are copied  into  memory, only when they are required. This mechanism is  
called Pure Demand Paging . 
Performance  of Demand  Paging  
Let p be the probability  of a page  fault  (0< p < 1). Then  the effective  access  time  is 
Effective  access  time  = (1  - p) x memory  access  time  + p x page  fault  time  
In any case,  we are faced  with  three  major  components  of the page -fault  service  time:  
1. Service  the page -fault  interrupt.  
2. Read  in the page.  
3. Restart  the process.  
 
 
 
PAGE  REPLACEMENT   
The  page  replacement  is a mechanism  that  loads  a page  from  disc  to memory  when  a 
page of memory needs to be allocated. Page replacement can be described as follows:  
1. Find  the location  of the desired  page  on the disk.  
2. Find  a free  frame:  
a. If there  is a free  frame,  use it. 
b. If there  is no free  frame,  use a page -replacement  algorithm  to select  a victim  frame.  
c. Write  the victim  page  to the disk;  change  the page  and frame  tables  accordingly.  
3. Read  the desired  page  into  the (newly)  free  frame;  change  the page  and frame  tables.  
4. Restart  the user  process.  
 
 


Page  67  
                     
 
(Diagram  of Page  replacement)  
Page Replacement Algorithms : The page replacement algorithms decide which 
memory pages to page out (swap out, write to disk) when a page of memory needs to  be 
allocated. We evaluate an algorithm by running it on a particular string of memory references  
and computing  the number  of page faults.  The string  of memory  references  is called  a 
reference string.  
The different  page  replacement  algorithms  are described  as follows:  
1. First -In-First -Out (FIFO)  Algorithm:  
A FIFO replacement algorithm associates with each page the time when that page was 
brought  into  memory.  When  a page  must  be replaced,  the oldest  page  is chosen  to swap  out. 
We can create  a FIFO  queue  to hold  all pages  in memory.  We replace  the page  at the head  of 
the queue.  When  a page is brought  into  memory,  we insert  it at the tail  of the queue.  
Example:  
(FIFO  page -replacement  algorithm)  
Note : For some  page -replacement  algorithms,  the page  fault  rate  may  increase  as the number 
of allocated frames increases. This most unexpected result is known as Belady's anomaly.  
2. Optimal  Page  Replacement  algorithm:  
One result of the discovery of Belady's anomaly was the search for an optimal page 
replacement algorithm. An optimal page -replacement algorithm has the lowest page -fault 
rate of all algorithms, and will never suffer from Belady's anomaly. Such an algorithm does 
exist, and has been called OPT or MIN.  
 
 
 


Page  68  
                     
It is simply “Replace the page that will not be used for the longest period of time”. Use 
of this page -replacement algorithm guarantees the lowest possible pagefault rate for a fixed 
number of frames.  
Example:  
 
(Optimal  page -replacement  algorithm)  
3. LRU  Page  Replacement  algorithm  
If we use the recent past as an approximation of the near future, then we will replace 
the page that has not been used for the longest period of time. This approach is the least - 
recently -used (LRU) algorithm.  
LRU replacement  associates with  each  page the time of  that  page's  last use.  When  a 
page must  be replaced, LRU  chooses that  page  that  has not  been  used for  the longest  period 
of time.  
Example:  
(LRU  page -replacement  algorithm)  
The major problem is how to implement LRU replacement. An LRU page -replacement 
algorithm may require substantial hardware assistance. The problem is to determine an order  
for the frames defined by the time of last use. Two implementations are feasible:  
Counters:  We associate with each page -table entry a time -of-use field, and add to the CPU a 
logical clock or counter. The clock is incremented for every memory reference. Whenever a 
reference to a page is made, the contents of the clock register are copied to the time -of-use 
field in the page -table entry for that page. We replace the page with the smallest time value. 
This scheme requires a search of the page table to find the LRU page, and a write to memory 
(to the time -of-use field in the page table) for each memory access. The times must also be 
maintained when page tables are changed (due to CPU scheduling).  
Stack:  Another approach to implementing LRU replacement is to keep a stack of page 
numbers. Whenever a page is referenced, it is removed from the stack and put on the top. In 
this way,  the top of  the stack is  always  the most  recently used page  and  the bottom  is the LRU 
page. Because entries must be removed from the middle of the stack, it is best implemented 
by a doubly linked list, with a head and tail pointer. Each update is a little more expensive, 
but there  is no search  for a replacement;  the tail pointer  points  to the bottom  of the stack,  
 


Page  69                       
which is the LRU  page. This approach is particularly appropriate for software or microcode 
impleme -ntations of LRU replacement. Example:  
 
(Use  of a stack  to record  the most  recent  page  references)  
4. LRU  Approximation  Page  Replacement  algorithm  
In this algorithm, Reference  bits are associated with  each entry  in the page  table. 
Initially, all bits are cleared (to 0) by the operating system. As a user process executes, the bit 
associated with each page referenced is set (to 1) by the hardware. After some time, we can 
determine which pages have been used and which have not been used by examining  the 
reference bits.  
This  algorithm  can be classified  into  different  categories  as follows:  
i. Additional -Reference -Bits Algorithm: It can keep an 8 -bit(1 byte) for each page 
in a page table in memory. At regular intervals, a timer interrupt transfers control to the 
operating system. The operating system shifts the reference bit for each page into the high - 
order bit of its 8 -bit, shifting the other bits right over 1 bit position, discarding the low -order  
bit. These  8 bits shift  registers  contain  the history of  page  use for  the last  eight  time periods.  
If we interpret these 8 -bits as unsigned integers, the page with the lowest number is the 
LRU page, and it can be replaced.  
ii. Second -Chance Algorithm: The basic algorithm of second -chance  replacement  is 
a FIFO  replacement  algorithm.  When  a page  has been  selected,  we inspect  its reference  bit. 
If the value is 0,  we proceed to replace this page. If the reference bit is set to 1,  we give that 
page a second chance and move on to select the next FIFO page. When a page gets a second 
chance, its reference bit is cleared and its arrival time  is reset to  the current  time.  Thus,  a 
page that  is given  a second  chance  will not be replaced  until  all other  pages are replaced.  
5. Counting -Based  Page  Replacement  
We could keep a counter of the number of references that have been made to each 
page, and develop the following two schemes.  
i. LFU page replacement algorithm: The least frequently used (LFU) page - 
replacement algorithm requires that the page with the smallest count be  replaced.  The 
reason  for this selection  is that  an actively  used  page  should  have  a large  reference count.  
ii. MFU page -replacement algorithm : The most frequently used (MFU) page 
replacement algorithm is based on the argument that the page with the largest count be 
replaced.  
ALLOCATION  OF FRAMES   
 


Page  70  Global  Versus  Local  Allocation                       
When a page fault occurs, there is a free frame available to store new page into a frame. 
While the page  swap  is taking  place,  a replacement  can be selected,  which  is written  to the 
disk as the user process continues to execute. The operating system allocate all its buffer and  
table space from the free -frame list for new page.  
Two  major  allocation  Algorithm/schemes.  
1. equal  allocation  
2. proportional  allocation  
1. Equal allocation:  The easiest  way  to split  m frames  among  n processes  is to give 
everyone an equal share, m/n frames. This scheme is called equal allocation.  
2. proportional allocation: Here,  it allocates  available  memory  to each  process  according 
to its size. Let the size of the virtual memory for process pi be si, and define  S= ∑ Si  
Then,  if the total  number  of available  frames  is m, we allocate  ai frames  to process  pi, where  
ai is approximately  ai = Si/ S x m. 
We can classify page -replacement algorithms into two broad categories: global 
replacement and local replacement.  
Global replacement allows a process to select a replacement frame from the set of all 
frames, even if that frame is currently allocated to some other process; one process can take a 
frame from another.  
Local replacement requires that each process select from only its own set of allocated 
frames.  
 
The system spends most of its time shuttling pages between main memory and 
secondary memory due to frequent page faults. This behavior is known as thrashing.  
A process is  thrashing if it is spending more  time paging than executing.  This leads  to: 
low CPU utilization and the operating system thinks that  it needs to increase the degree of  
multiprogramming.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(Thrashing)  
 
THRASHING  


Page  71                       
FILE  SYSTEM  INTERFACE  
The file system provides the mechanism for on -line storage of and access to both data 
and programs of the operating system and all the users of the computer system. The file 
system consists of two distinct parts: a collection of files, each storing related data, and a 
directory structure, which organizes and provides information about all the files in the 
system.  
FILE  CONCEPT   
A file is a collection  of related information  that  is recorded  on secondary  storage.  From 
a user's perspective, a file is  the smallest allotment of logical secondary storage and data can 
not be written to secondary storage unless they are within a file.  
Four  terms  are in common  use when  discussing  files:  Field,  Record,  File and Database  
 A field is the basic element of data. An individual field contains a single value, such as an 
employee’s last  name, a date, or the value of  a sensor reading. It  is characterized  by its 
length and data type.  
 A record is a collection of related fields that can be treated as a unit by some application 
program. For example, an employee record would contain such fields as name, social 
security number, job classification, date of hire, and so on.  
 A file is a collection of similar records. The file is treated as a single entity by users and 
applications and may be referenced by name.  
 A database is a collection of related data. A database may contain all of the information 
related  to an organization  or project,  such  as a business  or a scientific  study.  The  database 
itself consists of one or more types of files.  
File  Attributes:  
A file has the following  attributes:  
 Name:  The  symbolic  file name  is the only  information  kept  in human  readable  form.  
 Identifier:  This  unique  tag, usually  a number,  identifies the  file within  the file system;  it is 
the non -human -readable name for the file.  
 Type:  This  information  is needed  for those  systems  that  support  different  types.  
 Location: This information is a pointer to a device and to the location of the file on that 
device.  
 Size: The current size of the file (in bytes, words, or blocks), and possibly the maximum 
allowed size are included in this attribute.  
 Protection: Access -control information determines who can do reading, writing, 
executing, and so on.  
 Time,  date,  and user identification:  This information may  be kept  for creation, 
modification and last use. These data can be useful for protection, security, and usage 
monitoring.  
File  Operations:  
The operating system can provide system calls to create, write, read, reposition, delete, and 
truncate files. The file operations are described as followed:  
 Creating  a file:  Two  steps  are necessary  to create  a file. First,  space  in the file system  must 
be found for the file. Second, an entry for the new file must be made in the directory. The 
directory entry records the name of the file and the location in the file system, and 
possibly other information.  
 


Page  72                       
 Writing a file:  To write a file, we make a system call specifying both the name of the file 
and the information to be written to the file. Given the name of the file, the system 
searches  the directory  to find  the location  of the file. The  system  must keep  a write  pointer 
to the location in the file where the next write is to take place. The write pointer must be 
updated whenever a write occurs.  
 Reading  a file:  To read  from  a file, we use a system  call that  specifies  the name  of the file 
and where  (in main  memory)  the next  block  of the file should  be put.  Again,  the directory 
is searched for the associated directory  entry,  and the  system needs to  keep a  read pointer  
to the location in the file where  the next  read is to  take  place. Once  the read has  taken 
place, the read pointer is updated.  
 Repositioning within a file:  The directory is searched for the appropriate entry, and the 
current -file-position is set to a given value. Repositioning within a file does not need  to 
involve any actual I/O. This file operation is also known as a file seeks.  
 Deleting  a file:  To delete  a file, we search  the directory  for the named  file. Having  found 
the associated  directory  entry,  we release  all file space,  so that  it can be reused  by other 
files, and erase the directory entry.  
 Truncating  a file:  The  user may  want  to erase  the contents  of a file but keep  its attributes. 
Rather than forcing the user to delete the file and then recreate it, this function allows all 
attributes to remain unchanged -except for file length -but lets the file be reset to length 
zero and its file space released.  
File  Types:    The files  are classified  into  different  categories  as follows:  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


Page  73    
The name is split into two parts -a name and an extension, The system uses the extension to 
indicate the type of the file and the type of operations that can be done on that file.  
ACCESS  METHODS   
When a file is used, this information must be  accessed and read into computer 
memory. The information in the file can be accessed in several ways. There are two major 
access methods as follows:  
Sequential Access:  Information in the file is processed in  order, one record after  the 
other. A read operation reads the next portion of the file and automatically advances a  file 
pointer, which tracks the I/O location. Similarly, a write appends to the end of the file and 
advances to  the end of the newly written material (the new end of file).  Sequential access is  
based on a tape model of a file, and works as well on sequential -access devices as it does on 
random -access ones.  
Direct Access:  A file is made up of fixed length logical records that allow programs to 
read and write records rapidly in no particular order.  The direct -access method is based on a 
disk  model  of a file, since  disks  allow  random  access  to any file block.  For direct  access,  the 
file is viewed  as a numbered  sequence  of blocks  or records.  A direct -access  file allows 
arbitrary blocks to be read or written. There are no restrictions on the order  of reading  or 
writing  for a direct -access  file. For the direct -access  method,  the file operations  must  be 
 
 


Page  74  
 
modified  to include  the block  number  as a parameter.  Thus,  we have  read n, where  n is the 
block number, rather than read next, and write n rather than write next.  
DIRECTORY  STRUCTURE   
A directory  is an object  that  contains  the names  of file system  objects.  File system 
allows  the users to  organize  files  and other  file system  objects through  the use  of directories. 
The structure created by placement of names in directories can take a number of forms: Single - 
level tree, Two -level tree, multi -level tree or cyclic graph.  
1. Single -Level Directory:  The simplest directory structure is  the single -level 
directory.  All files  are contained  in the same  directory,  which  is easy  to support  and 
understand. A single -level directory has significant limitations, when the number of  files 
increases or when the system has more than one user. Since all files are in the same directory, 
they must have unique names.  
 
 
 
 
 
 
 
2. Two -Level Directory : In the two -level directory structure, each user has its own  
user file directory (UFD). Each UFD has a similar structure, but lists only the files of a single 
user. When a user job starts or a user logs in, the system's master file directory (MFD) is 
searched.  The MFD is indexed  by user  name or  account  number,  and each  entry points to the 
UFD for that user.  
When a user refers to a particular file, only his own UFD is searched. Different users 
may  have files with the same name, as long as all the file names within each UFD are unique.  
To create a file for a user, the operating system searches only that user's UFD to 
ascertain whether another file of that name exists. To delete a file, the operating system 
confines its search  to the local  UFD;  thus, it cannot accidentally delete another user's  file that 
has the same name.  
 
 
 
 
 
 
 
 
 
3. Tree -structured directories : A tree structure is A more powerful and flexible 
approach to organize files and directories in  hierarchical. There  is a master  directory,  which  
has under it a number of user directories. Each of these user directories may have  sub- 
directories and files as entries. This is true at any level: That is, at any level, a directory may 
consist of entries for subdirectories and/or entries for files.  


Page  75  
   
4. Acyclic -Graph  Directories:  
An acyclic graph allows directories to have shared subdirectories and files. The same 
file or subdirectory may be in two  different directories. An acyclic graph is a natural 
generalization of the tree structured directory scheme.  
A shared file (or directory) is not the same  as two  copies of the  file. With  two copies,  
each  programmer  can view  the copy  rather  than  the original,  but if one programmer  changes 
the file, the changes will not appear in the other's copy.  
Shared  files  and subdirectories  can be implemented  in several  ways.  A common  way  is 
to create  a new  directory  entry  called  a link.  A link  is a pointer  to another  file or subdirectory.  
 
 
5. General  Graph  Directory:  
 
 


Page  76  
                     
When we add links to an existing tree -structured directory, the tree  structure  is 
destroyed, resulting in a simple graph structure.  
 
 
 
 
SECONDARY  STORAGE  STRUCTURE  
DISKS  STRUCTURE   
Magnetic disks provide the  bulk of secondary storage for modern computer systems. 
Each disk platter has a flat circular  shape,  like a CD. Common platter diameters range from  
1.8 to 5.25 inches. The two surfaces of a platter are covered with a magnetic material. We store 
information by recording it magnetically on the platters.  
A read -write  head  "flies"  just above  each  surface  of every  platter.  The heads  are 
attached  to a disk  arm,  which  moves  all the heads  as a unit.  The surface  of a platter  is 
logically divided into circular tracks, which are subdivided into sectors. The set of tracks that  
are at one arm position forms a cylinder. There may be thousands of concentric cylinders in a 
disk drive, and each track may contain hundreds of sectors. The  storage  capacity  of common  
disk drives is measured in gigabytes.  
 
 
 
 
 
 
 
 
 
 
 
 
