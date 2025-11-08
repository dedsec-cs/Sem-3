Page  19                       
As an example, consider the following four processes, with the length of the CPU -burst time given in 
milliseconds:  
 
Process  Arrival  Time  Burst  Time  
P1 0 8 
P2 1 4 
P3 2 9 
p4 3 5 
If the processes arrive at the ready queue at the times shown and need the indicated burst times, then 
the resulting preemptive SJF schedule is as depicted in the following Gantt chart:  
 
Process PI is started at time 0, since it is the only process in the queue. Process PZ arrives at time 1.  
The remaining time for process P1 (7 milliseconds) is larger than the time required by process P2 (4 
milliseconds), so process P1 is preempted, and process P2 is scheduled. The average waiting time for this 
example is ((10 - 1) + (1 - 1) + (17 - 2) + (5 - 3))/4 = 26/4 = 6.5 milliseconds. A nonpreemptive SJF scheduling 
would result in an average waiting time of 7.75 milliseconds.  
Priority  Scheduling  
 
The SJF algorithm is a special case of the general priority -scheduling algorithm. A priority is associated 
with each process, and the CPU  is allocated to  the process with the highest priority. Equal -priority processes are 
scheduled in FCFS order.  
An SJF algorithm is simply a priority algorithm where the priority (p) is the inverse of the (predicted) next 
CPU burst. The larger the CPU burst, the lower the priority, and vice versa.  
Note that we discuss scheduling in terms of high priority and low priority. Priorities are generally some 
fixed range of  numbers, such as 0 to 7,  or 0 to 4,095. However, there is no general agreement on whether  0 is 
the highest or lowest priority. Some systems use low numbers to represent low priority; others use low numbers 
for high priority. This difference can lead to confusion. In this  text, we use low numbers to represent high priority. 
As an example, consider  the following  set of processes,  assumed to have arrived  at time 0, in the order  PI, P2,  
..., Ps, with the length  of the CPU -burst  time given  in milliseconds:  
 
Process  Burst  Time Priority  
P1 10 3 
p2 1 1 
p3 2 4 
P4 1 5 
P5 5 2 
Using  priority  scheduling,  we would  schedule  these  processes  according  to the following  Gantt  chart:  
 
The average  waiting  time is 8.2 milliseconds.  Priorities  can be defined  either  internally  or externally.  
Internally  defined  priorities  use some  measurable  quantity  or quantities  to compute  the priority  of a process.  
For example, time limits, memory requirements, the number of open files, and the ratio of average I/O 
burst to average CPU burst have been used in computing priorities. External priorities are set by criteria that are 
external to the operating system, such as the importance of  the process, the type and amount of funds  being 
paid for computer use, the department sponsoring the work, and other, often political, factors.  
Priority scheduling can be either preemptive or nonpreemptive. When a process arrives at the ready 
queue, its priority is compared with the priority of the currently running process. A preemptive priority -scheduling 
algorithm will preempt the CPU if the priority of the newly arrived process is higher than the priority of the  
currently running process. A nonpreemptive priority -scheduling  
algorithm  will simply  put the new process  at the head  of the ready  queue.  
A major  problem with  priority -scheduling  algorithms  is indefinite  blocking  (or starvation).  A process  that is 
ready to run but lacking the CPU can be considered blocked -waiting for the CPU. A priority -scheduling algorithm 
can leave some low -priority processes waiting indefinitely for the CPU.  


Page  20                       
A solution to the problem of indefinite blockage of low -priority processes  is aging. Aging is  a technique of 
gradually increasing the priority of processes that wait in the system for a long time. For example, if priorities 
range from 127 (low) to 0 (high), we could decrement the priority of a waiting process by 1 every 15 minutes. 
Eventually, even a process with an initial priority of 127 would have the highest priority in the system and would 
be executed. In  fact, it would take no  more than 32 hours for a priority  127 process to age to a priority 0 process.  
Round -Robin  Scheduling  
 
The round -robin  (RR) scheduling algorithm is designed especially  for timesharing systems. It is similar to 
FCFS scheduling, but preemption is added to switch between processes. A small unit of time, called a time 
quantum (or time slice), is defined. A time quantum is generally from 10 to 100 milliseconds. The ready queue is 
treated as a circular queue. The CPU scheduler goes around the ready queue, allocating the CPU to each 
process for a time interval of up to 1 time quantum.  
To implement RR scheduling, we keep the ready queue as a FIFO queue of processes. New processes 
are added to the tail of the ready queue. The CPU scheduler picks the  first process  from the ready queue, sets a 
timer to interrupt after 1 time quantum, and dispatches the process.  
One of two things will then happen. The process may have a CPU burst of less than 1 time quantum. In 
this case, the process itself will release the CPU voluntarily. The scheduler will then proceed to the next process 
in the ready queue. Otherwise, if the CPU burst of the currently running process is longer than 1 time quantum, 
the timer  will go off  and will cause  an interrupt to the operating  system.  A context  switch  will be executed, and 
the process will be put at the tail of the ready queue. The CPU scheduler will then select the next process in the 
ready queue.  
The average  waiting  time under  the RR policy,  however,  is often  quite  long.  
 
Consider the following set of processes that arrive at time 0, with the length of the CPU -burst time given 
in milliseconds:  
Process  Burst  Time  
PI 24 
P2 3 
P3 3 
If we use a time quantum of  4 milliseconds, then process P1 gets the first 4 milliseconds. Since it requires 
another 20 milliseconds, it is preempted after the  first time quantum, and the CPU is given to the next process in 
the queue, process P2. Since process P2 does not need 4 milliseconds, it quits before its time quantum expires. 
The CPU is then given to the next process, process P3. Once each process has received 1 time quantum, the 
CPU is returned to process P1 for an additional time quantum. The resulting RR schedule is  
 
The average  waiting  time is 17/3 = 5.66 milliseconds.  
In the RR scheduling algorithm, no process is allocated the CPU for more than 1 time quantum in a row.  
If a process' CPU burst exceeds 1 time quantum, that process is preempted and is put back in the ready queue. 
The RR scheduling algorithm is preemptive.  
If there are n processes in the ready queue and the time quantum is q, then each process gets l/n of the 
CPU time in chunks of at most q time units. Each process must wait no longer than (n - 1) x q time units until its 
next time quantum. For example, if there are five processes, with a time quantum of 20 milliseconds, then each 
process will get up to 20 milliseconds every 100  
milliseconds.  
The performance of  the RR algorithm  depends heavily  on the size of the time quantum. At one extreme,  
if the time quantum is very large (infinite), the RR policy is the same as the FCFS policy. If the time quantum is 
very small (say 1 microsecond), the RR approach is called processor sharing, and appears (in theory) to the 
users as though each of n processes has its own processor running at l/n the speed of the real processor. This 
approach was used in Control Data Corporation (CDC) hardware to implement 10 peripheral processors  with 
only one  set of hardware  and 10 sets  of registers. The  hardware  executes  one instruction  for one  set of registers, 
then goes on to the next. This cycle continues, resulting  in 10 slow  processors rather than one  fast processor.  
Multilevel  Queue  Scheduling  
Another class of scheduling algorithms has been created for situations in which processes are easily 
classified  into different  groups.  For example,  a common  division  is made  between  foreground  (or interactive)  
 


Page  21                       
processes and background (or batch) processes. These two types of processes have different response -time 
requirements, and  so might have  different scheduling needs. In addition,  foreground processes may have  priority 
(or externally defined) over background processes.  
 
 
Preemptive Vs  Nonpreemptive  Scheduling  
 
 
The Scheduling algorithms can be divided into two categories with respect to how they deal  with clock 
interrupts.  
Nonpreemptive Scheduling: A scheduling discipline is nonpreemptive , if once a process has been used the 
CPU, the CPU cannot be taken away from that process.  
Preemptive Scheduling : A scheduling discipline is preemptive, if once a process has been used the CPU, the 
CPU can taken away.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


Page  22  
                     
 
Thread  
A thread, sometimes called a  lightweight process (LWP), is a  basic unit of CPU utilization; it comprises a 
thread ID, a program counter, a register set, and a stack. It shares with other threads belonging to the same 
process its code section, data section, and other operating -system resources, such as open files and signals. A 
traditional (or  heavyweight)  process has a single thread of  control. If the process has multiple threads of  control,  
it can do more than one task at a time.  
Motivation  
Many software packages that run on modern desktop PCs are multithreaded.An application typically is 
implemented as a separate process with several thread of control.  
Single -threaded  and multithreaded  
 
Ex: A web browser might have one thread display images or text  while another thread retrieves data  
from the network. A word processor may have a thread for displaying graphics, another thread for reading 
keystrokes from the user, and a third thread for performing spelling and grammar checking in the background.  
In certain situations  a single application  may be required to perform several similar  tasks. For example, a 
web server accepts client requests for web pages, images, sound, and so forth. A busy web server may have 
several (perhaps hundreds) of clients concurrently accessing it. If the web server ran as a traditional single - 
threaded process, it would be able to service only one client at a time.  
One solution is to have the server run as a single process that accepts requests. When the server 
receives a request, it creates a separate process to service that request. In fact, this process -creation method  
was in common use before threads became popular. Process creation is  very heavyweight, as was shown in the 
previous chapter. If the new process will perform the same tasks as the existing process, why incur all that 
overhead? It is generally more efficient for one process that  contains multiple threads to serve the  same 
purpose. This approach would multithread the web -server process. The server would create a separate thread 
that would listen for client requests; when a request was made, rather than creating another process, it would 
create another thread to service the request.  
Threads also play a vital role in remote procedure call (RPC) systems. RPCs allow inter -process 
communication by providing a communication mechanism similar to ordinary function or procedure calls. 
Typically, RPC servers are multithreaded. When a server receives a message, it services the message using a 
separate thread. This allows the server to service several concurrent requests.  
Benefits  
The benefits  of multithreaded  programming  can be broken  down  into four major  categories:  
1. Responsiveness: Multithreading an interactive application may allow a program to continue running even if 
part of it is blocked or is performing a lengthy operation, thereby increasing responsiveness to the user. For 
instance, a multithreaded web browser could still allow user interaction  
in one thread while  an image  is being  loaded  in another  thread.  
 


Page  23                       
2. Resource sharing: By default, threads share the memory and the resources of the process to which they 
belong. The benefit of code sharing is that it allows an application to have several different threads of activity all 
within the same address space.  
3. Economy : Allocating  memory  and resources  for process  creation  is costly.  Alternatively,  because  threads  
share resources of the process to which they belong, it is  more economical to create and context switch threads. 
It can be difficult to gauge empirically the difference in overhead for creating and maintaining a process rather 
than a thread, but in general it is much more time consuming to create and manage processes than threads. In 
Solaris 2, creating a process is about 30 times slower than is creating a thread, and context switching is about 
five times slower.  
4. Utilization of multiprocessor architectures : The benefits of multithreading can be greatly increased in a 
multiprocessor architecture, where each thread may be running in parallel on a different processor. A single - 
threaded process can only run on one CPU, no matter how many are available.  
Multithreading on a multi -CPU machine increases concurrency. In a single processor architecture, the 
CPU generally moves between each thread so quickly as to create an illusion of parallelism, but in reality only 
one thread is running at a time.  
The OS supports  the threads  that can provided  in following  two levels:  
User -Level  Threads  
User -level threads implement in user -level libraries, rather than via systems calls, so thread switching 
does not need to call operating system and to cause interrupt to the kernel. In fact, the kernel knows nothing 
about user -level threads and manages them as if they were single -threaded processes.  
Advantages : 
• User -level  threads  do not require  modification  to operating  systems.  
• Simple  Representation:  Each  thread  is represented  simply  by a PC, registers,  stack  and a small  control 
block, all stored in the user process address space.  
• Simple  Management:  This simply  means  that creating  a thread,  switching  between  threads  and 
synchronization between threads can all be done without intervention of the kernel.  
• Fast and Efficient:  Thread  switching  is not much  more  expensive  than a procedure  call. 
Disadvantages:  
• There  is a lack of coordination  between  threads  and operating  system  kernel.  
• User -level  threads  require  non-blocking  systems  call i.e., a multithreaded  kernel.  
Kernel -Level  Threads  
In this method, the kernel knows about and manages the threads. Instead of thread table in each process, the 
kernel has a thread table that keeps track of  all threads in the system. Operating  Systems kernel provides 
system  call to create  and manage  threads. 
Advantages:  
• Because kernel has full knowledge of all threads, Scheduler may decide to give more time to a process 
having large number of threads than process having small number of threads.  
• Kernel -level  threads  are especially  good  for applications  that frequently  block.  
Disadvantages:  
• The kernel -level threads are slow and inefficient. For  instance, threads operations are hundreds of times 
slower than that of user -level threads.  
Since kernel must manage and schedule threads as well as processes. It require a full thread control  block  
(TCB) for each thread to maintain information about threads. As a result there is significant overhead and 
increased in kernel complexity.  
Multithreading  Models  
Many systems provide support for both user and kernel threads, resulting in different multithreading 
models. We look at three common types of threading implementation.  
Many -to-One Model  
 
The many -to-one model maps many user -level threads to one kernel thread. Thread management is 
done in user space, so it is efficient, but the entire process will block if a thread makes a blocking system call. 
Also, because only one thread can access the kernel at a time, multiple threads are unable to run in parallel on 
multiprocessors.  
One-to-one Model  
 


Page  24  
                     
The one -to-one model maps each user thread to a kernel thread. It provides more concurrency than the 
many -to-one model by allowing another thread to run when a thread makes a blocking system call; it also allows 
multiple threads to run in parallel on multiprocessors. The only drawback to this model is that creating a user 
thread requires creating the corresponding kernel thread. Because the overhead of creating kernel threads can 
burden the performance of an application, most implementations of this model restrict the number of threads 
supported by the system. Windows NT, Windows 2000, and OS/2 implement the one -to-one model.  
Many -to-Many  Model  
The many -to-many model multiplexes many user -level threads to a smaller or equal number of kernel 
threads. The number of kernel threads may be specific to either a particular application or a particular machine 
(an application may be allocated more kernel threads on a multiprocessor than on a uniprocessor). Whereas  the 
many -to-one model allows the developer to create as many user threads as she wishes, true concurrency is not 
gained because the kernel can schedule only one thread at a time. The one -to-one model allows for greater 
concurrency, but the developer has to be careful not to create too many threads within an application (and in 
some instances may be limited in the number of threads she can create). The many -to-many model suffers  from 
neither of these shortcomings: Developers can create as many user threads as necessary, and the  
corresponding kernel threads can run in parallel on a multiprocessor.  
 
(Diagram  of many -to-one model,  one-to-one model  and many -to-many  model ) 
Process  vs. Thread  
 
Process  Thread  
1.Process  cannot  share  the same  memory 
area(address space)  1.Threads  can share  memory  and files.  
2.It takes  more  time to create  a process  2.It takes  less time to create  a thread.  
3.It takes  more  time to complete  the execution  and 
terminate.  3.Less  time to terminate.  
4.Execution  is very slow.  4.Execution  is very fast. 
5.It takes  more  time to switch  between  two 
processes.  5.It takes  less time to switch  between  two threads.  
6.System  calls  are required  to communicate  each 
other  6.System  calls  are not required.  
7.It requires  more  resources  to execute.  7.Requires  fewer  resources.  
 
8.Implementing  the communication  between 
processes is bit more difficult.  8.Communication  between  two threads  are very 
easy to implement because threads share the 
memory  
 
 
 
 
 


Page  29  Inter -process Communication (IPC)  
• Mechanism  for processes  to communicate  and to synchronize  their actions.  
• Message  system  – processes  communicate  with each  other  without  resorting  to shared  variables.  
• IPC facility  provides  two operations:  
1. send (message ) – message  size fixed  or variable  
2. receive (message ) 
• If P and Q wish  to communicate,  they need  to: 
1. establish  a communication  link between  them  
2. exchange  messages  via send/receive  
• Implementation  of communication  link 
1. physical  (e.g.,  shared  memory,  hardware  bus) 
2. logical  (e.g.,  logical  properties)  
Direct  Communication  
Processes  must  name  each  other  explicitly:  
✦ send  (P, message ) – send  a message  to process  P 
✦ receive (Q, message ) – receive  a message  from  process  Q Properties  of communication  link 
✦ Links  are established  automatically.  
✦ A link is associated  with exactly  one pair of communicating  processes.  
✦ Between  each  pair there  exists  exactly  one link. 
✦ The link may be unidirectional,  but is usually  bi-directional.  
Indirect  Communication  
Messages  are directed  and received  from  mailboxes  (also  referred  to as ports).  
✦ Each  mailbox  has a unique  id. 
✦ Processes  can communicate  only if they share  a mailbox.  
Properties  of communication  link 
✦ Link established  only if processes  share  a common  mailbox  
✦ A link may be associated with  many  processes.  
✦ Each  pair of processes  may share  several  communication  links.  
✦ Link may be unidirectional  or bi-directional.  
Operations  
✦ create  a new mailbox  
✦ send  and receive  messages  through  mailbox  
✦ destroy a mailbox 
Primitives  are defined  as: 
send (A, message ) – send  a message  to mailbox  A 
receive (A, message ) – receive  a message  from  mailbox  A 
 
Mailbox  sharing  
✦ P1, P2, and P3 share  mailbox A. 
✦ P1, sends;  P2 and P3 receive.  
✦ Who  gets the  message?  
Solutions  
✦ Allow  a link to be associated  with at most  two processes.  
✦ Allow  only one process  at a time to execute  a receive  operation.  
✦ Allow  the system  to select  arbitrarily  the receiver.  Sender  is notified  who the receiver  was. 
 
Concurrent  Processes  
The concurrent processes executing in the operating system may be either independent processes or 
cooperating processes. A process is independent if it cannot affect or be affected by the other processes 
executing in the system.Clearly, any process that does not share any data (temporary or persistent) with any 
other  process  is independent.  On the other  hand,  a process  is cooperating  if it can affect  or be affected  by the 


Page  30   

Page  31                       
other processes executing in the system.Clearly, any process that shares data with other processes is a 
cooperating process.  
We may want to  provide  an environment  that allows  process  cooperation 
for several reasons:  
Information sharing: Since several users may be interested in the same piece of information (for instance, a 
shared file), we must provide an environment to allow concurrent access to these types of resources.  
Computation speedup: If we want a particular task to run faster, we must break it into subtasks, each of  wluch 
will be executing in parallel with the others. Such a speedup can be achieved only if the computer has multiple 
processing elements (such as CPUS or I/O channels).  
Modularity: We may want to construct the system in a modular fashion,dividing the system functions into 
separate processes or threads.  
Convenience: Even an individual user may have many tasks on which to work at one time. For instance, a user 
may be editing, printing, and compiling in parallel.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


Page  32                       
Message -Passing  System  
The function of a message system is to allow processes to communicate with one another without the 
need to resort to shared data. We have already seen message passing used as a method of communication in 
microkernels. In this scheme, services are provided as ordinary user processes. That is, the services operate 
outside of the kernel. Communication among the user processes is accomplished through the passing of 
messages. An IPC facility provides at least the two operations: send (message) and receive (message).  
Messages sent by a process can be of either fixed or variable size. If only fixed -sized messages can be 
sent, the system -level implementation is straightforward. This restriction, however, makes the task of 
programming more difficult. On the other hand, variable -sized messages require a more complex system -level 
implementation, but the programming task becomes simpler.  
If processes P and Q want to communicate, they must send messages to and receive messages from 
each other; a communication link must exist between them. This link can be implemented in a variety of ways.  
We are concerned here not with the link's physical implementation, but rather with its logical implementation. 
Here are several methods for logically implementing a link and the send/receive operations:  
• Direct  or indirect  communication  
• Symmetric  or asymmetric  communication  
• Automatic  or explicit  buffering  
• Send  by copy  or send  by reference  
• Fixed -sized  or variable -sized  messages  
We look at each  of these  types  of message  systems  next.  
Synchronization  
Communication between processes takes place by calls to send and receive primitives. There are different  
design options for implementing each primitive. Message passing may be either blocking or nonblocking -also 
known as synchronous and asynchronous.  
Blocking send : The sending process  is blocked until the message is  received by the receiving process  or by the 
mailbox.  
Nonblocking  send:  The sending  process  sends  the message  and resumes  operation.  
Blocking  receive:  The receiver  blocks  until a message  is available.  
Nonblocking  receive:  The receiver  retrieves  either  a valid  message  or a null. 
Different combinations of send and receive are possible. When both the send and receive are blocking, 
we have a rendezvous between the sender and the receiver.  
Buffering  
Whether the communication is direct or indirect, messages exchanged by communicating processes reside in a 
temporary queue. Basically, such a queue can be implemented in three ways:  
Zero capacity: The queue has maximum length 0; thus, the link cannot have any messages waiting in it. In this 
case, the sender must block until the recipient receives the message.  
Bounded capacity: The queue has finite length n; thus, at most n messages can reside in it. If the queue is not 
full when a new message is sent, the latter is placed in the queue (either the message is copied or a pointer to  
the message is kept), and the sender can continue execution without waiting. The link has a finite capacity, 
however. If the link is full, the sender must block until space is available in the queue.  
Unbounded capacity: The queue has potentially infinite length; thus, any number of messages can wait in it. 
The sender never blocks.The zero -capacity case is sometimes referred to as a message system with no 
buffering; the other cases are referred to as automatic buffering.  
 
Client -Server  Communication  
• Sockets  
• Remote  Procedure  Calls  
• Remote  Method  Invocation  (Java)  
 
 
 
 
 
 


Page  33                       
Process  Synchronization  
A situation where several processes access and manipulate the same data concurrently and  the 
outcome of the execution depends on the particular order in which the access takes place, is called a race 
condition . 
 
Producer -Consumer  Problem  
Paradigm  for cooperating  processes,  producer  process  produces  information  that is consumed  by a 
consumer  process.  
To allow producer and consumer processes to run concurrently, we must  have available a buffer  of 
items that can be filled by the  producer and emptied  by the consumer. A producer can produce one item  while 
the consumer is consuming another item. The producer and consumer must be synchronized, so that the 
consumer does not try to consume an item that has not yet been produced. In this situation, the consumer must 
wait until an item is produced.  
✦ unbounded -buffer  places  no practical  limit on the size of the buffer.  
✦ bounded -buffer  assumes  that there  is a fixed  buffer  size. 
 
Bounded -Buffer  – Shared -Memory  Solution  
The consumer  and producer  processes  share  the following  variables.  
Shared  data 
 
#define  BUFFER_SIZE  10 
Typedef struct  
{ 
. . . 
} item;  
item buffer[BUFFER_SIZE]; 
int in = 0;  
int out =  0; 
Solution  is correct,  but can only use BUFFER_SIZE -1 elements.  
The shared buffer is implemented as a circular array with two logical pointers: in and out. The variable in points  
to the next free position  in the buffer;  out points  to the first  full position in  the buffer.  The buffer  is empty when  in 
== out ; the buffer  is full when  ((in + 1) % BUFFERSIZE)  == out. 
The code for the producer  and consumer  processes  follows.  The producer  process  has a local variable  
nextproduced  in which  the new  item to be produced  is stored:  
 
Bounded -Buffer  – Producer  Process  
item nextProduced; 
while (1)  
{ 
while  (((in + 1) % BUFFER_SIZE)  == out) 
; /* do nothing */ 
buffer[in]  = nextProduced;  
in = (in + 1) % BUFFER_SIZE;  
} 
 
Bounded -Buffer  – Consumer  Process  
item nextConsumed;  
 


Page  34                       
while  (1) 
{ 
while  (in == out) 
; /* do nothing */ 
nextConsumed  = buffer[out];  
out = (out + 1) % BUFFER_SIZE;  
} 
 
The critical  section  problem  
Consider a system consisting of n processes {Po,P1, ..., Pn -1). Each process has a segment of code, 
called a critical section , in which the process may be changing common variables, updating a table, writing a 
file, and so on. The important feature of the system is that, when one process is executing in its critical  section,  
no other process is to be allowed to execute in its critical section. Thus, the execution of critical sections by the 
processes is mutually exclusive in time. The critical -section problem is to design a protocol that the processes 
can use to cooperate. Each process must request permission to enter its critical section. The section of code 
implementing this request is the entry section. The critical section may be followed by an exit section. The 
remaining code is the remainder section.  
 
 
do{ 
Entry  section  
Critical  section 
Exit section  
Remainder  section  
}while(1);  
 
A solution  to the critical -section  problem  must  satisfy  the following  three  requirements:  
1. Mutual Exclusion: If process Pi is executing in its critical  section, then no other processes can  be executing 
in their critical sections.  
2. Progress:  If no process  is executing  in its critical  section  and some  processes  wish  to enter  their critical  
sections,  then only those  processes  that are not executing  in their remainder  section  can participate  in the 
decision on which will enter its critical section next, and this selection cannot be postponed indefinitely.  
3. Bounded  Waiting:  There  exists  a bound  on the number  of times  that other  processes  are allowed  to enter  
their critical  sections  after  a process  has made  a request  to enter  its critical  section  and before  that request  is 
granted.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


Page  35                       
 
Peterson’s  solution  
Peterson’s  solution  is a software  based  solution  to the critical  section  problem.  
Consider two  processes  P0 and P1. For convenience,  when  presenting  Pi, we use Pi to denote  the other 
process; that is, j == 1 - i. 
The processes  share  two variables: 
boolean flag [2] ;  
int turn; 
Initially  flag [0] =  flag [1] = false, and the  value of turn is  immaterial (but is either 0 or 1). The  structure of process 
Pi is shown below.  
do{ 
flag[i]=true 
turn=j  
while(flag[j]  && turn==j);  
critical  section 
flag[i]=false  
Remainder  section  
}while(1);  
To enter the critical section,  process Pi first  sets flag [il to be true and then sets turn to the value j, 
thereby asserting that  if the other process wishes to enter the critical section  it can  do so. If both processes try to 
enter at the same time, turn will be set to both i and j at roughly the same time. Only one of  these assignments 
will last; the other will occur, but will be overwritten immediately. The eventual value of turn decides which of the 
two processes is allowed to enter its critical section first.  
We now prove  that this solution  is correct.  We need to show  that: 
1. Mutual  exclusion  is preserved,  
2. The progress  requirement  is satisfied,  
3. The bounded -waiting  requirement  is met. 
To prove  property  1, we note that each  Pi enters  its critical  section  only if either  flag [jl == false  or turn == 
i. Also note that, if both processes can be executing in their critical  sections at the same time, then flag [i] ==flag 
[jl == true. These two observations imply that P0 and P1 could not have successfully executed their while 
statements at about the same time, since the value of  turn can be either  0 or 1, but cannot be both. Hence, one 
of the processes say Pj -must have successfully executed the while statement, whereas  Pi had to execute at  
least one additional statement ("turn == j"). However, since, at that time, flag [j] == true, and turn == j, and this 
condition will persist as long as Pi is in its critical section, the result follows:  
To prove properties 2 and 3, we note that a process Pi can be prevented from  entering the critical  
section  only if it is stuck in the  while loop  with the  condition flag [j] == true  and turn == j; this loop is the only one. 
If Pi is not  ready to enter  the critical section, then flag [  j ] == false and Pi  can enter  its critical  section.  If Pi has 
set flag[j] to true and is also executing in its while statement, then either turn == i or turn == j. If turn == i, then Pi 
will enter the critical section. If turn == j, then Pi will enter the critical section. However, once Pi exits its critical 
section, it will reset flag [ jl to  false, allowing Pi to enter  its critical section. If Pi resets  flag [ j 1 to true, it must also 
set turn to i.  
Thus, since Pi does not change the  value of the  variable turn while  executing the  while statement, Pi will 
enter the critical section (progress) after at most one entry by Pi (bounded waiting).  
 
 
 
 
 
 
 
 
 
 


Page  36                       
 
Synchronization  Hardware  
As with other aspects of software, hardware features can make the programming task easier and  
improve system efficiency. In this section, we present some simple hardware instructions that are available on 
many systems, and show how they can be used effectively in solving the critical -section problem.  
The definition  of the TestAndSet  instruction. 
boolean TestAndSet(boo1ean &target)  
{ 
boolean  rv = target; 
target = true;  
return rv;  
} 
The critical -section  problem  could  be solved  simply  in a uniprocessor  environment  if we could  forbid  
interrupts to occur while a shared variable is being modified. In this manner, we could be sure that the current 
sequence of instructions  would be allowed to execute in order without preemption. No other instructions  would  
be run, so no unexpected modifications could be made to the shared variable.  
Unfortunately, this solution is not feasible in a multiprocessor environment. Disabling interrupts on a 
multiprocessor can be time -consuming, as the message is passed to all the processors. This message passing 
delays entry into each critical section, and system efficiency decreases. Also, consider the effect on a system's 
clock, if the clock is kept updated by interrupts.  
Many machines therefore provide special hardware instructions that allow us  either to test and modify  
the content of  a word, or to swap the contents of  two words, atomically -that is, as  one uninterruptible unit. We 
can use these special instructions to solve the critical -section problem in a relatively simple manner. Rather than 
discussing one specific instruction for one specific machine, let us abstract the main concepts behind  these  
types of instructions.  
The TestAndSet instruction can be defined as shown in code. The important characteristic is that this instruction 
is executed atomically. Thus, if two TestAndSet instructions are executed simultaneously (each on a different 
CPU), they will be executed sequentially in some arbitrary order.  
Mutual -exclusion  implementation  with TestAndSet  
do{ 
 
while(TestAndSet(lock));  
critical  section 
lock=false  
Remainder  section  
}while(1);  
 
void Swap(boo1ean  &a, boolean  &b) { 
boolean temp = a;  
a = b; 
b = temp}  
If the machine supports the TestAndSet instruction, then we can implement mutual exclusion  by 
declaring a Boolean variable lock, initialized to false.  
If the  machine  supports the Swap instruction, then  mutual exclusion  can be provided as  follows. A global 
Boolean variable lock is declared and is initialized to false. In addition, each process also has a local Boolean 
variable key.  
 
 
 
 
 
 


Page  37                       
 
Semaphores  
The solutions to the critical -section problem presented before are not  easy to generalize to more  
complex problems. To overcome this difficulty, we can use a synchronization tool called a semaphore. A 
semaphore S is an integer variable that, apart from initialization, is accessed only through two standard atomic 
operations: wait and signal . These operations were originally termed P (for wait; from the Dutch proberen, to 
test) and V (for signal; from verhogen, to increment). The classical definition of wait in pseudocode is  
 
wait(S)  { 
while  (S <= 0) 
; // no-op 
S --; 
} 
The classical  definitions  of signal  in pseudocode  is 
 
Signal(S){ 
S++;  
} 
 
Modifications to the integer value of the semaphore in the wait and signal operations must be executed 
indivisibly. That is, when one process modifies the semaphore value, no  other process can simultaneously 
modify  that same semaphore  value. In addition, in  the case of  the wait (S), the  testing of the integer  value of S  (S 
5 O), and its possible modification (S --), must also be executed without interruption.  
 
Usage  
We can use semaphores to deal with the n -process critical -section problem. The n processes share a 
semaphore, mutex (standing for mutual exclusion), initialized to 1. Each process Pi is organized as shown in 
Figure.We can also use semaphores to solve various synchronization problems.  
For example, consider two concurrently running processes: PI with a statement S1 and P2 with a statement S2. 
Suppose that we require that S2 be executed only after S1 has completed. We can implement this scheme  
readily by letting P1 and P2 share a common semaphore synch,  initialized to 0,  and by inserting the statements  
in process PI, and the statements  
wait (synch)  ; 
s2; 
 
in process  P2. Because  synch  is initialized  to 0, P2 will execute  S2 only after  PI 
has invoked signal (synch) , which is after S1.  
 
 
s1; 
signal  (synch)  ; 
do { 
wait (mutex)  ; 
critical  section 
signal (mutex) ;  
remainder  section  
} while  (1); 
Mutual -exclusion  implementation  with semaphores.  
Implementation  
 
The main disadvantage of the mutual -exclusion solutions and of the semaphore definition given here, is 
that they all require  busy waiting.  While  a process  is in its critical  section,  any other  process  that tries to enter  its 
 


Page  38                       
critical section must loop continuously in the entry code. This continual looping is clearly a problem in a real 
multiprogramming system, where a single CPU is  
shared among many processes. Busy waiting wastes CPU cycles that some other process might be able to use 
productively. This type of semaphore is also called a spinlock (because the process "spins" while waiting for the 
lock). Spinlocks are useful in multiprocessor systems. The advantage of a spinlock is that no context switch is 
required  when a process must  wait on a lock, and a context switch may take considerable time. Thus,  when 
locks are expected to be held for short times, spinlocks are useful.  
To overcome the need for busy waiting, we can modify the definition of the wait and signal semaphore 
operations. When a process executes the wait operation and finds that the semaphore value is not positive, it 
must wait. However, rather than busy waiting, the process can block itself. The block operation places a process 
into a waiting queue associated with the semaphore, and the state of the process  is switched to the waiting state. 
Then, control is transferred to the CPU scheduler, which selects another process to execute.  
A process that is blocked, waiting on a semaphore S, should be restarted when some other process 
executes a signal operation. The process is restarted by a wakeup operation, which changes the process from  
the waiting state to  the ready state. The process  is then placed in  the ready queue. (The CPU  may or  may not be 
switched from the running process to the newly ready process, depending on the CPU -scheduling algorithm.)  
To implement semaphores  under this  definition,  we define  a semaphore  as a "C" struct: 
typedef struct {  
int value  ; 
struct  process  *L; 
) semaphore;  
 
Each semaphore has an integer value and a list of processes. When a process must wait on a semaphore, it is 
added to the list of processes. A signal operation removes one process from the list of waiting processes and 
awakens that process.  
The wait semaphore  operation  can now be defined  as 
 
void wait(semaphore  S) { 
S.value --; 
if (S.value  < 0) { 
add this process  to S . L; 
block() ;  
} 
The signal  semaphore  operation  can now be defined  as 
void signal(semaphore S) {  
S.value++;  
if (S.value  <= 0) { 
remove  a process  P from S  . L ; 
wakeup (PI) ;  
} 
 
The block  operation  suspends  the process  that invokes  it. The wakeup(P1) operation resumes  the execution of a 
blocked process P. These two operations are provided by the operating system as basic system calls.  
Binary  Semaphores  
The semaphore construct described in the previous sections is commonly known as  a counting semaphore,  
since its integer value can range over an unrestricted domain. A binary semaphore is a semaphore with an 
integer value that can range only between 0 and 1. A binary semaphore can be simpler to implement than a 
counting semaphore, depending on the underlying hardware architecture. We will now show how a counting 
semaphore can be implemented using binary semaphores. Let S be a counting semaphore.  
To implement  it in terms  of binary  semaphores  we need  the following  data structures:  
 
binary -semaphore  S1, S2; 


Page  39                       
int C; 
 
Initially  S1 = 1, S2 = 0, and the  value of integer C  is set to the initial  value of the  counting  semaphore S. 
The wait operation on the counting semaphore S can be implemented as follows:  
wait (S1) ; 
C--; 
i f (C < 0) { 
signal(S1)  ; 
wait (S2) ;  
} 
signal(S1);  
The signal  operation  on the counting  semaphore  S can be implemented  as follows: 
w a i t (S1) ;  
C++ ; 
i f (C <= 0) 
signal  (S2) ; 
e l s e 
signal  (S1) ; 
Classic  Problems  of Synchronization  
We present a number of different synchronization problems as examples  for a large class of concurrency -control 
problems. These problems are used for testing nearly every newly proposed synchronization 
scheme.Semaphores are used for synchronization in our solutions . 
 
The Bounded -Buffer  Problem  
The bounded -buffer problem is commonly used to illustrate the power of synchronization primitives. We 
present here a general structure of this scheme, without committing ourselves to any particular implementation. 
We assume that the pool consists of  n buffers, each capable of  holding one item. The mutex  semaphore 
provides mutual exclusion for accesses to the buffer pool and is initialized to the value 1. The empty and full 
semaphores count the number of empty and full buffers, respectively. The semaphore empty is initialized to the 
value n; the semaphore f u l l is initialized to the value 0.  
The code  for the producer  process  is 
 
do{ 
produce  an item in nextp  
... 
wait (empty)  ; 
wait (mutex)  ; 
... 
add nextp  to buffer  
. . . 
signal(mutex); 
signal (full) ;  
) while  (1); 
 
The code  for the consumer  process  is 
do{ 
wait (full) ; 
wait (mutex)  ; 
. . . 


Page  40                       
remove  an item from  buffer  to nextc  
... 
signal  (mutex)  ; 
signal  (empty)  ; 
... 
consume  the item in  nextc  
... 
) while  (1); 
 
Note the symmetry between the producer and the consumer.  We can interpret this  code as  the producer 
producing full buffers for the consumer, or as the consumer producing empty buffers for the producer.  
 
 
 
The Readers - Writers  Problem  
A data object (such as a file or record) is to be shared among several concurrent processes. Some of 
these processes may want only to read the content of the shared object, whereas others may want to update  
(that is,  to read  and write) the shared  object.  We distinguish  between  these  two types of  processes by referring 
to those processes that are interested in only reading as readers, and to the rest as writers. Obviously, if two 
readers access the shared data object simultaneously, no adverse effects will result. However, if a writer and 
some other process (either a reader or a writer) access the shared object simultaneously, chaos may ensue.  
To ensure that these difficulties do not arise, we require that the writers have exclusive access to the 
shared object. This synchronization problem is referred to as the readers -writers problem. Since it was originally 
stated, it has been used to test nearly every new synchronization primitive. The readers -writers problem has 
several variations, all involving priorities. The simplest one, referred to as the first readers -writers problem, 
requires that no reader will be kept waiting unless a writer has already obtained permission to use the shared 
object. In other words, no reader should wait for other readers to finish simply because a writer is waiting. The 
second readers -writers problem requires that, once a writer is ready, that writer performs its write as soon as 
possible. In other words, if a writer is waiting to access the object, no new readers may start reading.  
A solution to either problem may result in starvation. In the first case, writers may starve; in the second 
case, readers may starve.  For this reason, other  variants of the problem have been proposed. In  this section,  we 
present a solution to the first readers -writers problem.  
In the solution  to the first readers -writers  problem,  the reader processes 
share the following data structures:  
semaphore  mutex,  wrt; 
int readcount;  
 
The semaphores mutex and w r t are initialized to 1; readcount is initialized to 0. The semaphore w r t is 
common to both the reader and writer processes. The mutex semaphore is used to ensure mutual exclusion 
when the variable readcount is updated. The readcount variable keeps track of how many processes are  
currently reading the object. The semaphore wrt functions as a mutual -exclusion semaphore for the writers. It is 
also used by the first or last reader that enters or exits the critical section. It is not used by readers who enter or 
exit while other readers are in their critical sections.  
The code  for a  writer process  is 
do{ 
wait (wrt)  ; 
. . . 
writing  is performed  
... 
signal(wrt);  
}while(1);  
 
The code  for a reader process  is 
 
