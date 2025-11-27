# Questions

1. At A Particular Time Of Computation The Value Of A Counting Semaphore is 7. Then 20 P operations and 15 V operations were completed on this semaphore. Obtain the resulting value of the semaphore

2. The `enter_CS()` and `leave_CS()` function to implement critical section of a process are realized using test and set instruction as follows:
```c
void enter_CS(X){
	while test-and-set(X);
} 

void leave_CS(X){
	X = 0;
} 
``` 

In The Above Solution X is memory location associated with the CS and is initialized to 0. Determine whether the above solution to CS Problem is deadlock-free or starvation-free or the process enter CS in FIFO order

3. Consider the resource allocation graph given in the figure.
   
   a) Find If The System is in a deadlock state.
   b) Otherwise, find a safe sequence.

4. Consider a system having m resources of the same type. These resources are shared by 3 processes  A,B and C , which have peak demands of 3,4 and 6 respectively. For What Value Of M Deadlock will not occur ?
5. A Computer System uses the banker's algorithm to deal with deadlocks. It current state is shown in the tables below , where P0, P1, P2 are processes and R0,R1,R2 are the resources types 
----
# Solutions


## Answer 1:
### Given:
- Initial value of the counting semaphore = **7**
- **20 P operations** are performed
- **15 V operations** are performed

We need to find the **final value** of the semaphore.

---

### Recall:
- **P (wait)**: Decrements the semaphore value by 1 (if value > 0). If value = 0, the process waits.
- **V (signal)**: Increments the semaphore value by 1.

So:
- Each **P** → **-1**
- Each **V** → **+1**

---

### Step-by-step Calculation:

1. **Start**: Semaphore = **7**

2. Perform **20 P operations**:
   - Each P decreases the value by 1.
   - But the semaphore **cannot go below 0** in standard behavior (though in pure counting, we compute net effect).
   - However, **this is a theoretical question**, and we assume operations are completed as stated (implying enough processes were able to perform P even if it goes negative — this is common in such assignment problems).

   So:
   ```
   After 20 P: 7 − 20 = −13
   ```

3. Perform **15 V operations**:
   - Each V increases the value by 1.
   ```
   After 15 V: −13 + 15 = 2
   ```

 Final Value of the Semaphore: **2**


## Answer 2:

**Solution: Test-and-Set based mutual exclusion**

```c
void enter_CS(int *X) {        // X is a shared lock variable, init = 0
    while (test_and_set(X));   // spin until we can set X = 1
}

void leave_CS(int *X) {
    *X = 0;                    // release the lock
}
```

`test_and_set(X)` atomically does:

```
old = *X;
*X = 1;
return old;
```

---

### 1. **Deadlock-free?** Yes

- **Reason**:  
  The lock `X` is **always released** by the process that holds it (`leave_CS` sets `X = 0`).  
  No process can hold the lock forever (assuming `leave_CS` is eventually called).  
  Therefore, **some process will always be able to acquire the lock eventually** → **no deadlock**.

---

### 2. **Starvation-free?** No

- **Reason**:  
  This is a **busy-waiting (spinlock)** solution with **no fairness guarantee**.  
  A process that keeps arriving when the lock is free can **repeatedly grab the lock** before a waiting process gets a chance (due to scheduling/timing).  
  → A process may **spin forever** → **starvation is possible**.

---

### 3. **Processes enter CS in FIFO order?** No

- **Reason**:  
  There is **no queue** or ordering mechanism.  
  Entry depends on **which process executes `test_and_set` when `X == 0`**.  
  This is **non-deterministic** and depends on **scheduler timing** → **not FIFO**.

---

### Final Answer:

| Property               | Satisfied? | Reason |
|------------------------|------------|--------|
| **Deadlock-free**      | Yes        | Lock is always released |
| **Starvation-free**    | No         | No fairness; a process can spin forever |
| **FIFO order entry**   | No         | No ordering; depends on timing |

**Summary**: The solution ensures **mutual exclusion** and is **deadlock-free**, but **neither starvation-free nor FIFO**.

---
