## What Is An Operating System

Operating System Is A Special Software That Acts As The Backbone or as a middleware of a computer coordinating tasks between hardware and software, making everything easy to use effectively while utilizing the CPU Potential at it's best

In more formal way we can call OS as:
- Software Abstraction Of Hardware
- Interface Between User and Hardware
- Set Of Utils To Simplify Application Dev and Execution
- While Being An Control Program To Act as a government over the system


## Services Of OS 

OS provides a range of services to make life easier for users and programs both
- OS Provides UI For User interaction with the hardware 
- Program Execution
- I/O Operations 
- File System Manipulation 
- Communication (Inter-Process Communication)
- Error Detection
- Resource Allocation
- Accounting 
- Protection And Security 


## Goals Of OS

If you're making a general purpose OS it should have these
- Convenience and User Friendly To Use
- Efficiency 
- Portability
- Reliability 
- Scalability 
- Robustness

## Parts Of An Operating System
- OS is made up of two main components 
### Shell

- You Interact With Shell Directly
- Front Desk Of OS
- U Make Requests Using GUI or commands
- OS Perform Those Tasks

### Kernel
- Engine Of OS 
- Does All The Shit Behind The Scenes
- Main Allocator And Deallocator and Coordinator 

## System Calls
- Medium Of Requesting Services From An OS 
- Customer Placing Order 
- Shell sends System Calls To Kernel Which OS then process 
- Common System Calls:
	- Fork()
	- Write()
	- Read()
	- Open()

## Dual Mode Of Operating

- To Avoid Fuck Ups We Have Dual Mode Of Operating So No Monkey Fucks Up Any Sensitive Functionality While Having His ADHD Trigger any safety issue or doom the os
- Mode Bit is the bit that decide whether we have user mode or kernel mode enabled 
	- Mode Bit = 1 Hence User Mode
		- User Mode Have Only Programs Running Like Browser and Shit U Can Do Everything that don't need you to have any low level manipulation
	- Mode Bit = 0 Hence Kernel Mode 
		- As Soon As U wanna Tinker and make some system calls the mode bit switches to 0 make the system call and comes back to 1 and hence your programs runs smoothly



## Booting

Bootstrapping AKA The Process By Which Your Computer Fucking Turns On 
- OS is loaded , applications are run and responds to user inputs
- Checks are done during booting to ensure everything is working as soon as power button  
- Hardware and firmware are involved
	- Firmware aka BIOS or UEFI in modern computers
- Booting Sequence 
	- POST (Power On)
	- Boot Device Selection (Boot From HDD or SSD or Pendrive Hecker man)
	- Bootloader Loading 
	- Kernel Initialization 
	- User Space Initialization 

## Types Of Booting

- Cold Booting
- Warm Booting

## Generation Of OS

Each Generation Lasted 10 Years and after 1990s we have gen 5 only going on
Starting Time Is 1940s

- Gen 1 
	- No True OS
	- Examples GMOS 
	- Vacuum Tube Based Computers 
	- NO OS
	- Load Manually via switches or punch cards
	- Batch Processing Of One Job At Time
	- Slow
	- Error Prone
	- Need Humans For Shit
- Gen 2
	- FORTRAN Monitor System
	- Transistor Based
	- Batch Processing Systems
	- Tapes Collection For Programs 
	- Sequential Execution
	- Early Compilers and Assemblers 
- Gen 3
	- IBM OS/360 and UNIX
	- ICs Bases 
	- Multiprogramming
	- Time Sharing
	- Spooling For IO
	- Virtual Memory 
	- CLI Based 
- Gen 4
	- MS DOS, Windows 3.0, MacOS
	- Microprocessor and VLSI
	- Network Support
	- Multi-tasking Multi User
	- UI Friendly And Portable 
- Gen 5
	- ULSI and AI
	- Networked / Distributed 
	- Mobile OS
	- Parallel Processing 
	- NLP
	- Self Healing And Predictive Features


## OS Architectures and Different Types Of OS Architectures 

