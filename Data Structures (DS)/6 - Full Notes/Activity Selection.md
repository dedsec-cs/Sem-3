## **Activity Selection

The Activity Selection Problem is a greedy algorithm where you try to perform the **maximum number of activities** using a single resource (like one meeting room, one machine, or one person).

- **Key Constraint:** You can only do one thing at a time. Activities cannot overlap.
    
- **The Goal:** Pick the set of activities that allows you to do the _most_ tasks, not necessarily the longest ones.
    

---

### **2. The Problem Statement**

- **Given:** A list of activities, each with a **Start Time** and a **Finish Time**.
    
- **Goal:** Select the maximum number of non-overlapping activities.
    

Example Scenario:

You have a meeting room.

- Meeting A: 10:00 - 11:00
    
- Meeting B: 10:30 - 12:30
    
- Meeting C: 11:00 - 12:00
    
- **Optimum Choice:** You pick A and C. (You can do 2 meetings). If you picked B, you could only do 1.
---
### **Example 1: The "Conference Room" Scenario**

Context: You are managing a single conference room. Three teams want to book it.

Goal: Approve as many bookings as possible.

| **Team**   | **Start Time** | **Finish Time** |
| ---------- | -------------- | --------------- |
| **Team A** | 9              | 11              |
| **Team B** | 10             | 12              |
| **Team C** | 11             | 13              |

Step 1: Sort by Finish Time

They are already sorted by finish time (11, 12, 13).

**Step 2: Execution (Greedy Trace)**

1. **Pick Team A:** It finishes earliest (at 11). **(Selected)**.
    
    - _Room is busy until 11._
        
2. **Check Team B:** Starts at 10.
    
    - Does $10 \ge 11$? **No**. (Conflict). **(Skip)**.
        
3. **Check Team C:** Starts at 11.
    
    - Does $11 \ge 11$? **Yes**. (Room is free). **(Selected)**.
        
    - _Room is busy until 13._
        

**Final Selection:** Team A and Team C. (Total: 2 activities).

---

### **Example 2: The "TV Show" Scenario (Complex Overlaps)**

**Context:** You want to watch as many TV shows as possible on a single channel, but you can't watch two at once.

**The List (Unsorted):**

- **Show P:** 1 to 4
    
- **Show Q:** 3 to 5
    
- **Show R:** 0 to 6
    
- **Show S:** 5 to 7
    
- **Show T:** 8 to 9
    
- **Show U:** 5 to 9
    

Step 1: Sort by Finish Time (Ascending)

We rearrange the list based on when the show ends.

|**Show**|**Start**|**Finish**|**Status**|
|---|---|---|---|
|**P**|1|**4**|_1st Choice_|
|**Q**|3|**5**||
|**R**|0|**6**||
|**S**|5|**7**||
|**T**|8|**9**||
|**U**|5|**9**||

**Step 2: Execution (Greedy Trace)**

1. **Pick Show P:** Finishes at 4. **(Selected)**.
    
    - _Busy until 4._
        
2. **Check Show Q:** Starts at 3. ($3 < 4$). **Skip**.
    
3. **Check Show R:** Starts at 0. ($0 < 4$). **Skip**.
    
4. **Check Show S:** Starts at 5.
    
    - Does $5 \ge 4$? **Yes**. **(Selected)**.
        
    - _Busy until 7._
        
5. **Check Show T:** Starts at 8.
    
    - Does $8 \ge 7$? **Yes**. **(Selected)**.
        
    - _Busy until 9._
        
6. **Check Show U:** Starts at 5. ($5 < 9$). **Skip**.
    

**Final Selection:** Show P, Show S, and Show T. (Total: 3 shows).
---

### **3. The Algorithm (Greedy Strategy)**

The Logic:

To fit the most activities in, you should always pick the activity that finishes the earliest.

- _Why?_ Because finishing early releases the resource (the room) as soon as possible, leaving more time for other activities.
    

#### **Pseudocode**

Plaintext

```
Function ActivitySelection(Activities):

    1. SORT Activities based on Finish Time (Ascending Order)
       (If two activities finish at the same time, the order between them doesn't matter)

    2. Select the first activity from the sorted list (It ends earliest).
       Print "Selected Activity 1"
       LastFinishTime = Activity[0].finish

    3. FOR i = 1 to TotalActivities - 1:
    
           // Check if the current activity starts AFTER the last one finished
           IF Activities[i].start >= LastFinishTime:
           
               Print "Selected Activity i"
               
               // Update the finish time to this new activity's finish time
               LastFinishTime = Activities[i].finish

    4. END
```

---

### **4. C Language Implementation**

Here is the C code using a simple structure and sorting method.

C

```
#include <stdio.h>

// Define a structure for an Activity
struct Activity {
    int id;
    int start;
    int finish;
};

void activitySelection(struct Activity A[], int n) {
    int i, j;
    struct Activity temp;

    // STEP 1: Sort by Finish Time (Ascending) using Bubble Sort
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (A[j].finish > A[j + 1].finish) {
                // Swap
                temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }

    // STEP 2: The Greedy Selection
    printf("\n--- Selected Activities ---\n");

    // Always select the first activity (after sorting)
    printf("Activity %d (Start: %d, Finish: %d)\n", A[0].id, A[0].start, A[0].finish);
    
    int lastFinishTime = A[0].finish;

    // STEP 3: Check the rest
    for (i = 1; i < n; i++) {
        // If this activity starts after (or when) the last one finished
        if (A[i].start >= lastFinishTime) {
            printf("Activity %d (Start: %d, Finish: %d)\n", A[i].id, A[i].start, A[i].finish);
            
            // Update the last finish time
            lastFinishTime = A[i].finish;
        }
    }
}

int main() {
    // Example Input
    // Activity 1: 1 to 2
    // Activity 2: 3 to 4
    // Activity 3: 0 to 6
    // Activity 4: 5 to 7
    // Activity 5: 8 to 9
    struct Activity activities[5] = {
        {1, 1, 2},
        {2, 3, 4},
        {3, 0, 6},
        {4, 5, 7},
        {5, 8, 9}
    };

    int n = 5;

    activitySelection(activities, n);

    return 0;
}
```

### **Output of the Code**

Plaintext

```
--- Selected Activities ---
Activity 1 (Start: 1, Finish: 2)
Activity 2 (Start: 3, Finish: 4)
Activity 4 (Start: 5, Finish: 7)
Activity 5 (Start: 8, Finish: 9)
```

_(Notice Activity 3 [0-6] was skipped because it overlapped with the others)._

### **Complexity Analysis**

- **Time Complexity:** $O(N \log N)$ due to the sorting step. The selection loop is only $O(N)$.
    
- **Space Complexity:** $O(1)$ (No extra data structures used).