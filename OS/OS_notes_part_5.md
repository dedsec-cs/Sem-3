Page  77          
(Structure  of Magnetic  disks  (Harddisk  drive))  
When the disk is in use, a drive motor spins it at high speed. Most drives rotate 60 to 
200 times per second. Disk speed has two parts. The transfer rate is the rate at which data 
flow between the drive and the computer. The positioning time (or random -access time) 
consists  of seek  time  and  rotational  latency . The  seek  time  is the time  to move  the disk  arm 
to the desired  cylinder.  And  the rotational  latency  is the time  for the desired  sector  to rotate 
to the disk head . Typical disks  can transfer several megabytes of data per second and they 
have seek times and rotational latencies of several milliseconds.  
Capacity  of Magnetic  disks(C)  = S x T x P x N 
Where  S= no. of surfaces  = 2 x no. of disks, T=  no. of tracks  in a surface, 
P= no. of sectors per track, N= size of each sector  
Transfer  Time:  The transfer  time  to or from  the disk  depends  on the rotation  speed  of the 
disk in the following fashion:  
T = b / ( r x N) 
Where  T= transfer  time,  b=number  of bytes  to be transferred,  N= number  of bytes  on a track,  
r= rotation  speed,  in revolutions  per second.  
Modern disk drives are addressed as large one -dimensional arrays of logical blocks, 
where the logical block is the smallest unit of transfer. The one -dimensional array of logical 
blocks is mapped onto the sectors of the disk sequentially. Sector 0 is the first sector of the 
first  track  on the outermost  cylinder.  The  mapping proceeds  in order through  that  track,  then 
through  the rest of  the tracks  in that  cylinder,  and then through  the rest of  the cylinders  from 
outermost to innermost.  
By using this mapping, we can convert a logical block number into an old -style  disk 
address that consists of a cylinder number, a track number within that cylinder, and a sector 
number within that track. In practical, it is difficult to perform this translation, for two 
reasons. First, most disks have some defective sectors, but the mapping hides this by 
substituting  spare  sectors from  elsewhere on  the disk.  Second,  the number  of sectors per  track 
is not a constant on some drives.  
 


Page  78  
                     
The density of bits per track is uniform. This is called Constant  linear velocity  (CLV). 
The disk  rotation  speed  can stay  constant  and the density  of bits decreases  from  inner  tracks 
to outer tracks to  keep the  data rate  constant. This method is used  in hard disks and is known  
as constant angular velocity (CAV).  
DISK  SCHEDULING   
The seek time is the time for the disk arm to move the heads to the  cylinder containing 
the desired sector. The rotational latency is the time waiting for the disk to rotate the desired 
sector  to the disk  head.  The disk  bandwidth  is the total  number  of bytes  transferred  divided 
by the total time between  the first  request  for service and  the completion of the last  transfer.  
We can improve  both  the access  time  and  the bandwidth  by scheduling  the servicing  of 
disk I/O requests in a good order. Several algorithms exist to schedule the servicing of disk 
I/O requests as follows:  
1. FCFS  Scheduling  
The simplest  form  of scheduling  is first -in-first -out (FIFO)  scheduling,  which  processes 
items from the queue in sequential order. We illustrate this with a request queue (0 -199):  
98, 183, 37, 122,  14, 124,  65, 67 
Consider  now  the Head  pointer  is in cylinder  53. 
(FCFS  disk  scheduling)  
2. SSTF  Scheduling  
It stands for shortest -seek -time -first (SSTF) algorithm. The SSTF algorithm selects the 
request with the minimum seek time from the current head position. Since seek time increases 
with  the number  of cylinders  traversed  by the head,  SSTF  chooses  the pending  request  closest 
to the current head position. We illustrate this with a request queue (0 -199):  
98, 183, 37, 122,  14, 124,  65, 67 
Consider  now  the Head  pointer  is in cylinder  53. 
 
 
 
 
 
 
 


Page  79  
                     
 
(SSTF  disk  scheduling)  
3.  SCAN  Scheduling  
In the SCAN algorithm, the disk arm starts at one end of the disk, and moves toward 
the other  end,  servicing  requests  as it reaches  each  cylinder,  until  it gets  to the other  end of the 
disk. At the other end, the direction of head movement is reversed, and servicing continues. 
The  head continuously scans back and forth across the  disk. We illustrate  this with a request 
queue (0 -199): 98, 183, 37, 122, 14, 124, 65, 67  
Consider  now  the Head  pointer  is in cylinder  53. 
(SCAN  disk  scheduling)  
4. C-SCAN  Scheduling  
Circular SCAN (C -SCAN) scheduling is a variant  of SCAN  designed  to provide  a 
more uniform wait time. Like SCAN, C -SCAN moves the head from one end of the disk to the 
other,  servicing  requests along  the way.  When  the head  reaches  the other end,  it immediately 
returns  to the beginning  of the disk, without servicing any requests on  the return  trip.  The C - 
SCAN scheduling algorithm essentially treats the cylinders as a circular list that wraps 
around  from  the final  cylinder  to the first  one.  We illustrate  this  with  a request  queue  (0-199): 
98, 183,  37, 122,  14, 124, 65,  67. Consider now  the Head pointer is in cylinder 53.  
 
 
 
 
 


Page  80  
 
  
(C-SCAN  disk  scheduling)  
5.  LOOK  Scheduling  
Practically, both SCAN and C -SCAN algorithm is not implemented this way. More 
commonly, the  arm goes only as far as the final request in each direction. Then, it reverses 
direction immediately, without going all the way to the end of the disk. These versions of 
SCAN and C -SCAN are called LOOK and C-LOOK scheduling,  because  they  look  for a 
request  before  continuing  to move  in a given  direction.  We illustrate  this with  a request  queue 
(0-199): 98, 183, 37, 122, 14, 124, 65, 67  
Consider  now  the Head  pointer  is in cylinder  53. 
(C-LOOK  disk  scheduling)  
Selection  of a Disk -Scheduling  Algorithm  
 SSTF is common and has a natural appeal.  
 SCAN  and C-SCAN  perform  better  for systems  that  place  a heavy  load  on the disk. 
 Performance depends on the number and types of requests.  
  Requests  for disk  service  can be influenced  by the file  allocation  method.  
 The disk -scheduling  algorithm should be written as a separate module of the operating  
system, allowing it to be replaced with a different algorithm if necessary.  
 Either SSTF or LOOK is a reasonable choice for the default algorithm.  
 
DISK  MANAGEMENT   
The operating  system  is responsible  for several  aspects  of disk  management.  
Disk  Formatting  


Page  81                       
A new magnetic disk is a blank slate. It is just platters of a magnetic recording material. 
Before  a disk  can store  data,  it must  be divided  into  sectors  that  the disk  controller  can read 
and write. This process is called low -level formatting (or physical formatting).  
Low -level formatting fills the disk with a special data structure for each sector. The 
data structure for a sector consists of a header, a data area, and a  trailer. The header and 
trailer  contain  information  used  by the disk  controller,  such  as a sector  number  and  an error - 
correcting code (ECC).  
To use a disk to hold files, the operating system still needs to record its own data 
structures  on the disk.  It does  so in two  steps.  The  first  step  is to partition  the disk  into  one or 
more groups of cylinders. The operating system can treat each partition as though it were a 
separate  disk.  For instance,  one partition  can hold  a copy  of the operating  system's  executable 
code, while another holds  user files. After partitioning,  the second step is logical formatting 
(or creation of a file system). In this step, the operating system stores the initial file -system 
data structures onto the disk.  
Boot  Block  
When a computer is powered up or rebooted, it needs to have an initial program to 
run. This initial program is called bootstrap program. It initializes all aspects of the system 
(i.e. from CPU registers to device controllers and the contents of main memory) and then 
starts the operating system.  
To do its job, the bootstrap program finds the operating system kernel on disk, loads 
that kernel into memory, and jumps to an initial address to begin the operating -system 
execution.  
For most  computers,  the bootstrap  is stored  in read -only  memory  (ROM).  This  location 
is convenient, because ROM needs no initialization and is at a fixed location that the 
processor can start executing when powered up or reset. And since ROM is read only, it 
cannot be infected by a computer virus. The problem is that changing this bootstrap code 
requires changing the ROM hardware chips.  
For this reason, most systems store a tiny bootstrap loader program in the boot ROM, 
whose  only  job is to bring  in a full bootstrap  program  from  disk.  The full bootstrap  program 
can be changed  easily:  A new version is  simply written onto  the disk.  The full bootstrap 
program  is stored  in a partition  (at a fixed  location  on the disk)  is called  the boot  blocks . A 
disk that has a boot partition is called a boot disk or system disk.  
Bad  Blocks  
Since disks have moving parts and small tolerances, they are prone to failure. 
Sometimes  the failure  is complete,  and  the disk  needs  to be replaced,  and  its contents  restored 
from backup media to the new disk.  
More  frequently,  one or more  sectors  become  defective.  Most  disks  even  come  from  the 
factory with bad blocks. Depending on the disk and controller in use, these blocks  are 
handled in a variety of ways.  
The controller maintains a list of bad blocks on the disk. The list is initialized during 
the low-level  format at the  factory, and is  updated over the life  of the disk. The  controller can 
be told to replace each bad  sector logically with one of the spare sectors. This scheme is 
known as sector sparing or forwarding.  
SWAP -SPACE  MANAGEMENT   
 


Page  82                       
The swap -space management is a low -level task of the operating system. The main 
goal for the design and implementation of swap space is to provide the best throughput for 
the virtual -memory system.  
Swap -Space  Use 
Swap space is used in various ways by different operating systems depending on the 
implemented memory -management algorithms.  
Those  systems  are implemented  swapping,  they  may  use swap  space  to hold  the entire 
process  image,  including  the code  and  data  segments.  The  amount of  swap space  needed  on a 
system can vary depending on the amount of physical memory,  
Swap -Space  Location  
A swap  space can  reside  in two places:  Swap space  can be  carved out  of the normal  file 
system, or it can be in a separate disk partition.  
If the swap space is simply a large file within the file system, normal file -system 
routines can be used to create it, name it, and allocate its space. This approach is easy to 
implement and is also inefficient.  
Alternatively, swap space can be  created in a separate  disk partition. No  file system  or 
directory  structure  is placed  on this space.  A separate  swap -space  storage  manager is  used  to 
allocate and deallocate the blocks. This manager uses algorithms optimized for speed and 
storage efficiency.  
RAID  STRUCTURE   
A Redundant Array  of Inexpensive  Disks(RAID)  may be  used  to increase  disk  reliability. 
RAID may be implemented in hardware or in the operating system.  
The RAID consists of seven levels, zero through six. These levels designate  different 
design architectures that share three common characteristics:  
 RAID  is a set of physical  disk  drives  viewed  by the operating  system  as a single  logical 
drive.  
 Data are distributed across  the physical  drives  of an array in  a scheme known  as striping, 
described subsequently.  
 Redundant disk capacity is used to store parity information, which guarantees data 
recoverability in case of a disk failure.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


Page  83         
(RAID  levels)  
(Here P indicates error -correcting bits and C indicates a second copy of the data) 
The RAID levels are described as follows:  
➢ RAID Level 0: RAID level 0 refers to disk arrays with striping at the level of blocks, but 
without any redundancy (such as parity bits). Figure(a) shows an array of size 4.  
➢ RAID Level 1: RAID level 1 refers to disk mirroring. Figure (b) shows a mirrored 
organization that holds four disks' worth of data.  
➢ RAID Level 2: RAID level 2 is also known as memory -style error -correcting code (ECC) 
organization. Each byte in a memory system may have a parity bit associated with it that 
records  whether  the numbers  of bits in the byte  set to 1 is even  (parity=O)  or odd 
(parity=l). The idea of ECC can be used directly in disk arrays via striping of bytes across  
disks.  
➢ RAID level 3: RAID level 3, or bit-interleaved parity organization, improves on level 2 by 
noting that, disk controllers can detect whether a sector has been read correctly, so a single 
parity bit can be used for error correction, as well as for detection. The idea is as  follows. If 
one of the sectors  gets  damaged,  we know  exactly  which  sector  it is, and,  for each  bit in the 


Page  84                       
sector, we can figure out whether it is a 1 or a 0 by computing the parity of the 
corresponding bits from sectors in the other disks. If the parity of the remaining bits  is 
equal to the stored parity, the missing bit is 0; otherwise, it is 1.  
➢ RAID Level 4: RAID level 4 or block -interleaved parity organization uses block -level 
striping, as in RAID 0 and in addition keeps a parity block on a separate disk  for 
corresponding  blocks from  N other  disks. This scheme is  shown  pictorially  in Figure(e).  If 
one of the disks fails, the parity block can be used with the corresponding blocks from the 
other disks to restore the blocks of the failed disk.  
➢ RAID  level  5: RAID  level  5 or block -interleaved  distributed  parity  is similar  as level  4 
but level 5  spreading data and parity  among all  N + 1 disks, rather  than  storing data in N 
disks and  parity in  one disk. For  each  block,  one of the disks  stores  the parity,  and the 
others store data. By spreading the parity across all the disks in the set, RAID 5 avoids the 
potential overuse of a single parity disk that can occur with RAID 4.  
➢ RAID  Level  6: RAID  level  6 (is also  called  the P+Q  redundancy  scheme)  is much  like 
RAID  level  5, but stores  extra  redundant  information  to guard  against  multiple  disk 
failures.  Instead  of using  parity,  error -correcting  codes  such  as the Reed -Solomon  codes 
are used.  
 
 
 
 
 
 
 
 
 
 
 
I/O SYSTEM  
The role of the operating system in  computer I/O is to manage and control I/O 
operations and I/O devices. A device communicates with a computer system by sending 
signals  over a  cable  or even  through  the air. The  device  communicates with the  machine  via a 
connection point. If one or more devices use a common set of wires for communication, the 
connection is called a bus.  
When device A has  a cable that plugs into device B, and device B  has a cable that plugs  
into  device C, and  device C  plugs into  a port  on the computer,  this arrangement  is called  a 
daisy chain. A daisy chain usually operates as a bus.  
Buses  are used  widely  in computer  architecture  as follows:  
 
 
 
 
 
 
 


Page  85  
                     
 
(A typical  PC bus structure)  
This  figure  shows  a PC1 bus (the  common  PC system  bus)  that  connects  the processor - 
memory subsystem to the fast devices, and an expansion bus that connects relatively slow 
devices such as the keyboard and serial and parallel ports. In the upper -right portion of the 
figure, four disks are connected together on a SCSI bus plugged into a SCSI controller.  
A controller is a collection of electronics that can operate a port, a bus, or a device. A 
serial -port controller is a simple device controller. It is a single chip (or portion of a chip) in 
the computer that controls the signals on the wires of a serial port.  
Since the SCSI protocol is complex, the SCSI bus controller is often implemented as a 
separate circuit board (or a host adapter) that plugs into the computer. It contains a processor, 
microcode, and some private memory to enable it to process the SCSI protocol messages.  
Some devices have their own built -in controllers. This board is the disk controller. It 
has microcode and a processor to do many tasks, such as bad -sector mapping, prefetching, 
buffering, and caching.  
An I/O  port  consists  of four  registers,  called the status,  control,  data -in, and data -out 
registers.  
 The status register  contains bits that can  be read  by the host. These bits indicate states such  
as whether the current command has completed, whether a  byte  is available  to be read  
from the data -in register, and whether there has been a device error.  
 The control  register  can be written  by the host  to start  a command  or to change  the mode 
of a device.  
 The data -in register  is read  by the host  to get input.  
 The data -out register  is written  by the host  to send  output.  
The external  devices  can be grouped  into  three  categories:  
 


Page  86                       
1. Human  readable: Suitable  for communicating  with  the computer  user.  Examples  include 
printers  and  terminals,  the latter  consisting  of video  display,  keyboard,  and perhaps  other 
devices such as a mouse.  
2. Machine  readable:  Suitable  for communicating  with  electronic  equipment.  Examples are 
disk drives, USB keys, sensors, controllers, and actuators.  
3. Communication: Suitable for communicating with remote devices. Examples are digital 
line drivers and modems.  
ORGANIZATION  OF THE  I/O FUNCTION(I/O  Technique)   
There  are three  techniques  for performing  I/O operations:  
1. Programmed I/O:  The processor issues an I/O command, on  behalf of a  process,  to an 
I/O module;  that  process  busy  waits  for the operation  to be completed  before  proceeding.  
2. Interrupt -driven I/O:  The processor issues an I/O command on behalf of  a process.  
There  are two  possibilities.  If the I/O  instruction  from  the process  is non blocking,  then 
the processor continues to execute instructions from the process that issued the I/O 
command. If the I/O instruction is blocking, then the next instruction that the processor 
executes is from the OS, which will put the current process in a blocked state and schedule 
another process.  
3. Direct memory access (DMA):  A DMA module controls the exchange of data between 
main  memory  and an I/O module.  The processor  sends  a request  for the transfer  of a 
block of data to the DMA module and is interrupted only after the entire block has been 
transferred.  
Interrupt -driven  I/O 
The basic  interrupt  mechanism  works  as follows.  
 The CPU hardware has a wire called the interrupt -request line that the CPU senses after 
executing every instruction.  
 When the CPU detects that a  controller  has asserted a  signal on the interrupt request  line,  
the CPU saves a small  amount of state, such as the current value of the instruction pointer,  
and jumps to the interrupt -handler routine at a fixed address in memory.  
 The interrupt handler determines the cause of the interrupt, performs the necessary 
processing, and executes a return from interrupt instruction to return the CPU to the 
execution state prior to the interrupt.  
The  above  mechanism  concludes  that  the device  controller  raises  an interrupt  by asserting 
a signal on the interrupt request line, the CPU catches the interrupt and dispatches to the 
interrupt handler, and the handler clears  the interrupt by servicing the device.  
 
 
 
 
 
 
 
 
 
 
 
 
 


Page  87         
 
(Diagram  of Interrupt -driven  I/O cycle)  
In a modern operating  system,  we need  more sophisticated  interrupt -handling features  as 
follows:  
➢ First,  we need  the ability  to defer  interrupt  handling  during  critical  processing.  
➢ Second,  we need  an efficient  way  to dispatch  to the proper  interrupt  handler  for a device.  
➢ Third,  we need  multilevel  interrupts,  so that  the operating  system  can distinguish  between 
high - and low -priority interrupts, and can respond with  the appropriate degree of 
urgency.  
In modern  computer  hardware,  these  three  features  are provided  by the CPU  and by 
the interrupt -controller hardware.  
Direct  Memory  Access  
The DMA unit is capable of mimicking the processor and of taking over control of the 
system  bus just like a processor.  It needs  to do this to transfer  data  to and from  memory over 
the system bus. The DMA technique works as follows:  
 When  the processor  wishes  to read  or write  a block  of data,  it issues  a command  to the 
DMA module by sending to the DMA module the following information:  
➢ Whether a read or write is requested, using the read or write control  line 
between the processor and the DMA module.  
 


Page  88  
 
➢ The  address  of the I/O device  involved,  communicated  on the data  lines.  
➢ The  starting location in memory  to read  from  or write  to, communicated on  the 
data lines and stored by the DMA module in its address register.  
➢ The number of words to be read or written, again communicated via the data  
lines and stored in the data count register.  
 Then the processor continues with other work. It has delegated this I/O operation to the 
DMA module.  
 The  DMA  module  transfers  the entire  block  of data,  one word at  a time,  directly  to or from 
memory, without going through the processor.  
 When the transfer is complete, the  DMA  module  sends  an interrupt  signal  to the 
processor.  Thus,  the processor  is involved only at  the beginning  and end of the transfer.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(Steps  in a DMA  transfer)  
APPLICATION  I/O INTERFACE   
I/O system calls encapsulate device behaviors in generic classes. Each general kind is 
accessed through a standardized set of functions, called an interface. The differences are 
encapsulated in kernel modules called device drivers that internally are custom tailored to 
each device, but that export one of the standard interfaces.  
Devices  vary  in many  dimensions:  
o Character -stream  or block  
o Sequential  or random -access  
o Sharable  or dedicated  
o Speed  of operation  
o read -write,  read  only,  or write  only  


Page  89  
                     
 
 
(Diagram  of a kernel  I/O structure)  
The purpose  of the device -driver  layer  is to hide  the differences  among  device 
controllers from  the I/O subsystem  of the kernel,  much  as the I/O system  calls  encapsulate 
the behavior of devices in a few generic classes that hide  hardware  differences  from  
applications. Making the I/O subsystem independent of the hardware simplifies the job of the 
operating -system developer. It also benefits the hardware manufacturers. They  either  design 
new devices to  be compatible with an existing  host  controller interface  (such  as SCSI -2), or 
they  write  device  drivers to  interface  the new  hardware  to popular  operating  systems.  Thus, 
new peripherals can  be attached to a computer without  waiting  for the operating -system 
vendor to develop support code.  
KERNEL  I/O SUBSYSTEM   
Kernels provide many services related to I/O. Several services (i.e. scheduling, 
buffering, caching, spooling, device reservation and error handling) are provided by the 
kernel's I/O subsystem and build on the hardware and device driver infrastructure.  
1. I/O Scheduling:  It is used  to schedule  a set of I/O requests  that  means  to determine  a 
good order  in which  to execute  them.  Scheduling  can improve  overall  system  performance  
and can reduce the average waiting time for I/O to complete.  
2. Buffering : A buffer is a memory area that stores data while they are transferred between 
two devices or between a device and an application. Buffering is done for three reasons.  
➢ One reason is to cope with a speed mismatch between the producer and consumer of a 
data stream.  
 


Page  90                       
➢ A second use of  buffering is to adapt  between  devices  that  have  different  data -transfer 
sizes.  
➢ A third  use of buffering  is to support  copy  semantics  for application I/O.  
3. Caching:  A cache  is a region  of fast memory  that  holds  copies  of data.  Access  to the 
cached  copy  is more  efficient  than  access to  the original.  Cache  is used  to improve  the I/O 
efficiency  for files  that  are shared  by applications  or that  are being  written  and reread  rapidly.  
The  difference between a buffer and a  cache is  that a buffer may  hold the  only existing 
copy  of a data  item, whereas  a cache  just holds  a copy  on faster  storage  of an item  that  resides 
elsewhere. Caching and buffering are distinct functions, but sometimes a region of memory 
can be used for both purposes.  
4. Spooling : A spool  is a buffer  that  holds  output  for a device,  such as  a printer,  that  cannot 
accept interleaved data streams. Although a printer can serve only one job at a time, several 
applications may wish to print their output concurrently, without having their output mixed 
together.  The  operating system solves  this problem by  intercepting all output to the  printer.  
Each application's output is spooled to a separate disk file. When an application 
finishes printing, the spooling system queues the corresponding spool file for output to the 
printer.  
The spooling system copies the queued spool files to the printer one at a time. The 
operating system provides a control interface that enables users and system administrators to 
display  the queue,  to remove  unwanted  jobs  before  those  jobs  print,  to suspend  printing 
while the printer is serviced, and so on.  
5.  Device  Reservation:  
It provides  support  for exclusive  device  access,  by enabling  a process  to allocate  an idle 
device, and to deallocate that device when it is no longer needed. Many operating  systems 
provide  functions  that  enable  processes  to coordinate  exclusive  access  among  them.  It 
watches out for deadlock to avoid.  
Transforming  I/O request  to Hardware  Operations   
Consider  reading  a file from  disk  for a process:  
➢ Determine  device  holding  file 
➢ Translate  name  to device  representation  
➢ Physically  read  data  from  disk  into  buffer  
➢ Make  data  available  to requesting  process  
➢ Return  control  to process  
The  following  steps  are described  the lifecycle  of a blocking  read  request:  
1. A process issues a blocking read() system call to a file descriptor of a file that has been 
opened previously.  
2. The system -call code in the kernel checks the parameters for correctness. In the case of 
input, if the data are already available in the buffer cache, the data are returned to the 
process and the I/O request is completed.  
3. Otherwise, a physical I/O needs to be performed, so the process is removed from the run 
queue and is placed on the wait queue for the device, and the I/O request is scheduled. 
Eventually, the I/O subsystem sends the request to the device driver. Depending on the 
operating system, the  request is sent via a subroutine  call or via an in -kernel message.  
 
 


Page  91  
                     
4. The device driver allocates kernel buffer space to receive the data, and schedules the I/O. 
Eventually,  the driver sends  commands  to the device  controller by writing  into  the device 
control registers.  
5. The device  controller  operates  the device  hardware  to perform  the data  transfer.  
6. The driver may poll for status and data, or it may have set up a DMA transfer into kernel 
memory. We assume that the transfer is managed by a DMA controller, which generates 
an interrupt when the transfer completes.  
7. The correct interrupt handler receives the interrupt via  the interrupt -vector  table,  stores  
any necessary data, signals the device driver, and returns from the interrupt.  
8. The device driver receives the signal, determines which I/O request completed, 
determines  the request's  status, and  signals  the kernel  I/O subsystem  that  the request  has 
been completed.  
9. The kernel transfers data  or returns  codes to the address  space  of the requesting  process, 
and moves the process from the wait queue back to the ready queue.  
10. Moving the  process  to the ready queue  unblocks  the process. When the  scheduler assigns 
the process  to the CPU,  the process  resumes  execution  at the completion  of the system  call.  
 
(The  life cycle  of an I/O request)  
 
