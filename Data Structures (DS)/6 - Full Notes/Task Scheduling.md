## **Task/Job Scheduling

**Task Scheduling** is a greedy optimization problem where you have a list of jobs.

- Every job has a **Profit** (money you get if you do it) and a **Deadline** (time limit).
    
- **Constraint:** Each job takes **1 unit of time** to complete.
    
- **Goal:** Arrange the jobs to get the **Maximum Profit**. You will likely have to ignore some low-profit jobs if they can't fit within the deadlines.
    

---

### **2. The Greedy Strategy**

To make the most money:

1. **Be Greedy:** Always look at the **highest paying job** first.
    
2. **Be Smart:** Do the job **as late as possible** (closest to its deadline).
    
    - _Why?_ If a job needs to be done by 5 PM, doing it from 4-5 PM is smarter than doing it at 9-10 AM. This saves the early morning hours for other jobs that _must_ be done early (e.g., a job with a 10 AM deadline).
        

**The Algorithm Steps:**

1. Sort all jobs by **Profit** (High to Low).
    
2. Find the maximum deadline (say, `D_max`). Create a timeline with that many empty slots.
    
3. Take the first job (Highest Profit). Check its deadline (say `d`).
    
4. Look at the time slot `d`. Is it empty?
    
    - **Yes:** Book it.
        
    - **No:** Look at `d-1`, then `d-2`, etc. Book the first empty slot you find.
        
    - If you reach 0 and find no empty slots, **skip the job**.
        

---

### **3. Numerical Examples**

#### **Example 1: The Basic Scenario**

**Scenario:** You have 4 jobs.

|**Job ID**|**Profit**|**Deadline**|
|---|---|---|
|**A**|100|2|
|**B**|19|1|
|**C**|27|2|
|**D**|25|1|

**Step 1: Sort by Profit (High to Low)**

1. **A** (100, Deadline 2)
    
2. **C** (27, Deadline 2)
    
3. **D** (25, Deadline 1)
    
4. **B** (19, Deadline 1)
    

Step 2: Create Slots

Max Deadline is 2. We have 2 slots: [Slot 1], [Slot 2].

**Step 3: Execution**

1. **Pick Job A (Profit 100, Deadline 2):**
    
    - Check Slot 2. Empty? **Yes**.
        
    - _Schedule:_ `[Empty, A]`
        
2. **Pick Job C (Profit 27, Deadline 2):**
    
    - Check Slot 2. Busy (A is there).
        
    - Check Slot 1. Empty? **Yes**.
        
    - _Schedule:_ `[C, A]`
        
3. **Pick Job D (Profit 25, Deadline 1):**
    
    - Check Slot 1. Busy (C is there). No previous slots.
        
    - _Result:_ **Reject D**.
        
4. **Pick Job B (Profit 19, Deadline 1):**
    
    - Check Slot 1. Busy.
        
    - _Result:_ **Reject B**.
        

**Final Answer:** Jobs C and A. **Total Profit:** $27 + 100 = 127$.

---

#### **Example 2: The "High Profit Conflict"**

**Scenario:** Sometimes high-paying jobs fight for the same spot.

|**Job ID**|**Profit**|**Deadline**|
|---|---|---|
|**J1**|20|2|
|**J2**|15|2|
|**J3**|10|1|
|**J4**|5|3|

Step 1: Sort by Profit

List: J1(20), J2(15), J3(10), J4(5).

Step 2: Create Slots

Max Deadline is 3. Slots: [1] [2] [3].

**Step 3: Execution**

1. **Job J1 (20, D:2):** Go to Slot 2. Empty? Yes.
    
    - _Status:_ `[Empty, J1, Empty]`
        
2. **Job J2 (15, D:2):** Go to Slot 2. Busy (J1).
    
    - Check Slot 1 (Previous). Empty? Yes.
        
    - _Status:_ `[J2, J1, Empty]`
        
3. **Job J3 (10, D:1):** Go to Slot 1. Busy (J2).
    
    - No earlier slots. **Reject J3**.
        
4. **Job J4 (5, D:3):** Go to Slot 3. Empty? Yes.
    
    - _Status:_ `[J2, J1, J4]`
        

**Final Answer:** Jobs J2, J1, J4. **Total Profit:** $15 + 20 + 5 = 40$.

---

#### **Example 3: The "Gap" Scenario**

**Scenario:** A job has a very late deadline, leaving a gap in the middle.

|**Job ID**|**Profit**|**Deadline**|
|---|---|---|
|**X**|50|4|
|**Y**|40|1|
|**Z**|30|1|

Step 1: Sort by Profit

List: X(50), Y(40), Z(30).

Step 2: Create Slots

Max Deadline is 4. Slots: [1] [2] [3] [4].

**Step 3: Execution**

1. **Job X (50, D:4):** Go to Slot 4. Empty? Yes.
    
    - _Status:_ `[Empty, Empty, Empty, X]`
        
2. **Job Y (40, D:1):** Go to Slot 1. Empty? Yes.
    
    - _Status:_ `[Y, Empty, Empty, X]`
        
3. **Job Z (30, D:1):** Go to Slot 1. Busy (Y).
    
    - No earlier slots. **Reject Z**.
        

Final Answer: Jobs Y and X. Total Profit: $40 + 50 = 90$.

(Note: Slots 2 and 3 remain empty because no job fit those specific criteria, even though we had space).

---

### **4. C Code Implementation**

C

```
#include <stdio.h>
#include <stdbool.h>

// Structure to represent a Job
struct Job {
    char id;     // Job Name
    int profit;  // Profit if completed
    int dead;    // Deadline
};

void printJobScheduling(struct Job arr[], int n) {
    // STEP 1: Sort all jobs by profit (Descending order)
    struct Job temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j].profit < arr[j + 1].profit) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    // STEP 2: Initialize Result Array and Slots
    // We assume max deadline is not huge for this example (e.g., max 10)
    int result[10]; // To store result (Job IDs)
    bool slot[10];  // To keep track of free time slots
    
    // Initialize all slots as free
    for (int i = 0; i < 10; i++)
        slot[i] = false;

    // STEP 3: Iterate through all sorted jobs
    for (int i = 0; i < n; i++) {
        
        // Find a free slot for this job (arr[i])
        // Start from the last possible slot (min(deadline, max_slots) - 1)
        // We do 'min' check just in case deadline > array size
        for (int j = (arr[i].dead < 10 ? arr[i].dead : 10) - 1; j >= 0; j--) {
            
            // If slot is found empty
            if (slot[j] == false) {
                result[j] = i;  // Add job index to result
                slot[j] = true; // Mark slot as occupied
                break;          // Move to next job
            }
        }
    }

    // Print the result
    printf("Selected Jobs sequence: ");
    int totalProfit = 0;
    for (int i = 0; i < 10; i++) {
        if (slot[i]) {
            printf("%c ", arr[result[i]].id);
            totalProfit += arr[result[i]].profit;
        }
    }
    printf("\nTotal Profit: %d\n", totalProfit);
}

int main() {
    // Using Example 2 Data
    struct Job arr[] = { 
        {'A', 20, 2}, 
        {'B', 15, 2}, 
        {'C', 10, 1}, 
        {'D', 5, 3} 
    };
    
    int n = 4; // Number of jobs
    printJobScheduling(arr, n);
    
    return 0;
}
```

**Output:**

```
Selected Jobs sequence: B A D 
Total Profit: 40
```

_(B is done in slot 1, A in slot 2, D in slot 3)._
