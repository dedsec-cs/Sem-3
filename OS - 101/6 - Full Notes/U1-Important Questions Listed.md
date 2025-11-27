## 1\. Operating System Fundamentals & Types 💻

 1. Compare and contrast **multitasking** and **multiprogramming**, considering their respective strengths and weaknesses.
 2.  Explain the concept of a **batch operating system**. Discuss its advantages and limitations in modern computing environments.
 3. Describe the **architecture of a multiprogramming operating system**. How does it improve CPU utilization compared to a single-program system?
 4. Discuss **real-time operating systems (RTOS)**. Provide examples of applications where RTOS is essential.
 5. Describe the architecture of a **multiprocessor operating system**. How does it enhance system performance compared to a single-processor system?
 6. Explain the concept of a **real-time operating system (RTOS)**. Discuss the differences between **hard real-time** and **soft real-time** systems with examples.
 7. Give the **type of OS** that will be used in each case and give a reason:
  * Air Traffic Control Systems
  * Payroll system
  * Medical imaging systems
  * Server
  * Robots
  * Bank Statements
  * Cloud
  * Weapon and missile systems

-----

## 2\. Kernel and System Calls ⚙️

This category covers the core component of the OS (the kernel) and the mechanism for accessing OS services (system calls).

  1. Discuss the role of a **kernel** in an operating system. Explain the differences between a **monolithic kernel** and a **microkernel**.
  2. Describe the process of making a **system call** in an operating system. Include the steps involved and the role of the kernel in handling the call with example.
 3. Explain the need of various types of **system call** in an operating system.
 4. How does the distinction between **kernel mode** and **user mode** function as a rudimentary form of protection (security) system.
 5. Explain how the $\text{fork}()$ and $\text{exec}()$ system calls are used together in Linux to create and execute new processes. Then, write a simple C program that:
      * Creates a child process using $\text{fork}()$.
      * The child process replaces itself using $\text{exec}()$ to run the $\text{ls}$ command.
      * The parent process waits for the child to finish before exiting.
      * Now consider the following code snippet using the $\text{fork}()$ and $\text{wait}()$ system calls. Assume that the code compiles and runs correctly, and that the system calls run successfully without any errors.

```
int x = 4;
while (x > 0) {
	fork();
	printf("hello");
	wait(NULL);
	x--;
}
```

The total number of times the $\text{printf}$ statement is executed is

6. Describe the working of a **kernel** in an operating system. Explain how it manages communication between hardware and software components.

-----

## 3\. Linux Commands and Shell Scripting 🖥️

This category focuses on practical usage of the Linux environment, including basic commands and writing shell scripts.

1. Write and explain the Linux commands to:
      * Display the present working directory
      * Create, view, and navigate directories
      * Display system information

2. Write a shell script that uses a function to calculate the **factorial** of a number entered by the user, but only if the number is **prime**. If the entered number is not prime, display an appropriate message.

3.  Discuss the importance of **shell scripting in Linux**. Provide an example of a script that uses variables, loops, and conditional statements.

4. Complete the following shell script to find the **average of numbers** given at the command line.

```bash
#!/bin/bash
sum=0
count=$#
for num in "$@"
do
sum=$(( # Missing calculation
done
avg=$(( # Missing calculation
echo "Average = $avg"
))
```
  
  5. Describe the role of the **Command Line Interface (CLI)** in Linux compared to the **Graphical User Interface (GUI)**. Also summarize the purpose of basic Linux commands such as $\text{ls}$, $\text{ls -l}$, $\text{mkdir}$, $\text{rmdir}$, $\text{cp}$, and $\text{rm}$ in Linux.
  
  6. Write a shell script to calculate the **Fibonacci sequence**. Explain each step of the script.
  
  7. Predict the output of the following shell script when executed as:
```bash
	#!/bin/bash
	num=$1
	pos=1
	while [ $num -ne 0 ]
	do
		digit=$((num % 10))
		if [ $((pos % 2)) -ne 0 ]
		then
			 # Missing code
		fi
		echo -n "$digit "
		num=$((num/10))
		pos=$((pos+1))
	done
	echo
```
  
  8. Write a shell script to display the digits which are in **odd position** in a given 5-digit number. Explain each step of the script.

Would you like me to provide answers to the questions sorted by topic, starting with **Operating System Fundamentals & Types**?