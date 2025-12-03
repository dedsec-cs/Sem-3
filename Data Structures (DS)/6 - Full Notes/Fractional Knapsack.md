## Fractional Knapsack:
The **Fractional Knapsack Problem** is a greedy optimization algorithm where we have to fill a container (Knapsack) with items to get the **maximum total value**.

- **Key Feature:** You are allowed to take **fractions** of an item.
    
- **Analogy:** Think of the items as substances like gold dust, sugar, or flour—you can take half a kilo if you don't have space for a full kilo.

---

### **2. The Problem Statement**

- **Given:**
    
    1. A set of items, each with a **Weight** and a **Value**.
        
    2. A Knapsack with a maximum **Capacity** (how much weight it can hold).
        
- Goal:
    
    Maximize the total value in the knapsack without exceeding the capacity.
    

---

### **3. The Algorithm (Logic & Pseudocode)**

The core logic relies on a "Greedy Choice": **Always take the item with the highest value-to-weight ratio first.**

#### **Algorithm Steps 

1. **Calculate Ratio:** For every item, find out how valuable it is per kg ($Value \div Weight$).
    
2. **Sort:** Arrange the items from **highest ratio** to **lowest ratio**.
    
3. **Fill the Bag:**
    
    - Pick the best item.
        
    - If it fits completely, put it in.
        
    - If it doesn't fit, cut it (take the fraction that fits).
        
    - Stop when the bag is full.
        

#### **Pseudocode**

This is the logic written in a generic way (not specific to C or Python).

Plaintext

```
Function FractionalKnapsack(Capacity, Items):

    1. FOR each item in Items:
           item.ratio = item.value / item.weight

    2. SORT Items in Descending Order based on item.ratio

    3. CurrentWeight = 0
       TotalValue = 0

    4. FOR each item in SortedItems:
    
           // Case 1: The bag is already full
           IF CurrentWeight == Capacity:
               BREAK Loop

           // Case 2: The whole item fits
           IF (CurrentWeight + item.weight <= Capacity):
               CurrentWeight = CurrentWeight + item.weight
               TotalValue = TotalValue + item.value
           
           // Case 3: The item is too big, take a fraction
           ELSE:
               RemainingSpace = Capacity - CurrentWeight
               Fraction = RemainingSpace / item.weight
               
               TotalValue = TotalValue + (item.value * Fraction)
               CurrentWeight = Capacity  // Bag is now full
               BREAK Loop

    5. RETURN TotalValue
```

---

### **How to Trace this Pseudocode (Dry Run)**

Let's assume:

- **Bag Capacity:** 50kg
    
- **Item A:** Value 60, Weight 10 (Ratio: 6)
    
- **Item B:** Value 100, Weight 20 (Ratio: 5)
    
- **Item C:** Value 120, Weight 30 (Ratio: 4)
    

**Execution:**

1. **Sort:** A (Ratio 6), B (Ratio 5), C (Ratio 4).
    
2. **Loop Item A:** Fits? Yes (10 <= 50).
    
    - Bag has 10kg. Value is 60.
        
3. **Loop Item B:** Fits? Yes (10+20 <= 50).
    
    - Bag has 30kg. Value is 60+100 = 160.
        
4. **Loop Item C:** Fits? No (30+30 > 50).
    
    - **Else Condition:**
        
    - Remaining Space = $50 - 30 = 20$.
        
    - Fraction = $20 / 30 = 0.66$.
        
    - Add Value = $120 \times 0.66 = 80$.
        
    - **Total Value:** $160 + 80 = 240$.
        
    - **Break.**

---

### **4. C Language Implementation**

Here is a clean, newbie-friendly C code. I used a simple structure to keep the item details together and a basic sort so you can see exactly how the logic works.

C

```
#include <stdio.h>

// Define a structure to represent an Item
struct Item {
    int id;
    float weight;
    float value;
    float ratio; // We will calculate this: value / weight
};

void fractionalKnapsack(int n, float capacity, struct Item items[]) {
    float totalValue = 0.0;
    int i, j;
    struct Item temp;

    // STEP 1: Calculate Ratio for each item
    for (i = 0; i < n; i++) {
        items[i].ratio = items[i].value / items[i].weight;
    }

    // STEP 2: Sort items by Ratio in Descending Order (Simple Bubble Sort)
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (items[j].ratio < items[j + 1].ratio) {
                // Swap the items
                temp = items[j];
                items[j] = items[j + 1];
                items[j + 1] = temp;
            }
        }
    }

    // STEP 3: The Greedy Loop
    printf("\n--- Selected Items ---\n");
    for (i = 0; i < n; i++) {
        // If the item fits completely
        if (items[i].weight <= capacity) {
            capacity -= items[i].weight;
            totalValue += items[i].value;
            printf("Added Item %d (Full) - Value: %.2f\n", items[i].id, items[i].value);
        }
        // If the item does not fit, take a fraction
        else {
            float fraction = capacity / items[i].weight;
            totalValue += items[i].value * fraction;
            printf("Added Item %d (Fraction: %.2f) - Value: %.2f\n", items[i].id, fraction, (items[i].value * fraction));
            capacity = 0; // The bag is full
            break; // Stop the loop
        }
    }

    printf("\nMaximum Total Value in Knapsack: %.2f\n", totalValue);
}

int main() {
    // Example Input
    // We have 3 items
    struct Item items[3] = {
        {1, 10.0, 60.0, 0.0},  // Item 1: Weight 10, Value 60
        {2, 20.0, 100.0, 0.0}, // Item 2: Weight 20, Value 100
        {3, 30.0, 120.0, 0.0}  // Item 3: Weight 30, Value 120
    };
    
    float capacity = 50.0;
    int n = 3;

    printf("Knapsack Capacity: %.2f\n", capacity);
    
    fractionalKnapsack(n, capacity, items);

    return 0;
}
```

### **Output of the Code**

Plaintext

```
Knapsack Capacity: 50.00

--- Selected Items ---
Added Item 1 (Full) - Value: 60.00
Added Item 2 (Full) - Value: 100.00
Added Item 3 (Fraction: 0.67) - Value: 80.00

Maximum Total Value in Knapsack: 240.00
```

### **Why this works (Complexity)**

- **Time Complexity:** $O(N \log N)$.
    
    - Sorting the items takes the longest time ($N \log N$).
        
    - The loop to pick items only takes $O(N)$.
        
- **Space Complexity:** $O(1)$ (if we ignore the input storage), as we strictly use a few variables for calculation.
- 