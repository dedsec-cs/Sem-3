## **Huffman Encoding

**Huffman Encoding** is a greedy algorithm used for **Lossless Data Compression**. It reduces the size of data without losing any information.

- **The Problem:** Computers store text using fixed-size codes (like ASCII, where every letter is 8 bits). This is wasteful. For example, in a book, the letter 'e' appears millions of times, while 'z' appears rarely. Storing both as 8 bits is inefficient.
    
- **The Solution:** Assign **Variable-Length Codes**.
    
    - Give **Short codes** to frequent characters (e.g., 'e' might be `0`).
        
    - Give **Long codes** to rare characters (e.g., 'z' might be `11001`).
        
- **Prefix Rule:** To prevent confusion, no code can be a **prefix** of another. (e.g., If A=`0`, then B cannot be `01`, because the computer wouldn't know if `01` is "A then 1" or just "B").
    

---

### **2. The Algorithm (Greedy Strategy)**

**The Strategy:** Build a binary tree from the bottom up. Always combine the two characters/nodes with the **lowest frequency** (smallest count).

**Algorithm Steps:**

1. **Count:** Calculate the frequency of every character in the text.
    
2. **Leaf Nodes:** Create a leaf node for each character.
    
3. **Priority Queue:** Put all nodes in a list sorted by frequency (Low to High).
    
4. **Loop:** While there is more than one node in the list:
    
    - **Extract:** Remove the **two nodes** with the smallest frequencies (Left and Right).
        
    - **Merge:** Create a new internal node. Its frequency is the sum of Left+Right.
        
    - **Insert:** Add this new node back into the list.
        
5. **Trace:** The remaining node is the **Root**. Assign `0` to left edges and `1` to right edges. Trace the path from root to character to get its code.
    

---

### **3. Numerical Examples**

#### **Example 1: The Basic Trace**

**Input:** A string with these character counts:

- **A:** 5
    
- **B:** 9
    
- **C:** 12
    
- **D:** 13
    
- **E:** 16
    
- **F:** 45
    

**Execution:**

1. **Sort:** `[A:5, B:9, C:12, D:13, E:16, F:45]`
    
2. **Pick Smallest 2 (A & B):**
    
    - Combine 5+9=14.
        
    - New List: `[C:12, D:13, (AB):14, E:16, F:45]`
        
3. **Pick Smallest 2 (C & D):**
    
    - Combine 12+13=25.
        
    - New List: `[(AB):14, E:16, (CD):25, F:45]`
        
4. **Pick Smallest 2 (AB & E):**
    
    - Combine 14+16=30.
        
    - New List: `[(CD):25, (ABE):30, F:45]`
        
5. **Pick Smallest 2 (CD & ABE):**
    
    - Combine 25+30=55.
        
    - New List: `[F:45, (CDABE):55]`
        
6. **Pick Smallest 2 (F & CDABE):**
    
    - Combine 45+55=100. (Root Node)
        

**Resulting Codes (Approximate based on tree structure):**

- **F** (Most frequent) → `0` (1 bit)
    
- **A** (Least frequent) → `1100` (4 bits)
    

---

#### **Example 2: Constructing Codes**

**Input:**

- **a:** 10
    
- **b:** 50
    
- **c:** 40
    
- **d:** 20
    

**Step 1: Sort** `[a:10, d:20, c:40, b:50]`

**Step 2: Combine smallest (a & d)**

- New Node `(ad)` = 10+20=30.
    
- List: `[(ad):30, c:40, b:50]`
    

**Step 3: Combine smallest ((ad) & c)**

- New Node `(adc)` = 30+40=70.
    
- List: `[b:50, (adc):70]`
    

**Step 4: Combine smallest (b & (adc))**

- New Node `Root` = 50+70=120.
    

**Tree Visualization:**

Plaintext

```
        [Root: 120]
        /         \
     [b: 50]    [adc: 70]
    (Code: 0)   /       \
             [ad: 30]  [c: 40]
            (Code: 10) (Code: 11)
             /     \
         [a: 10]  [d: 20]
       (Code: 100) (Code: 101)
```

**Final Codes:**

- **b:** `0` (Shortest code for most frequent)
    
- **c:** `11`
    
- **a:** `100`
    
- **d:** `101`
    

---

### **4. C Code Implementation**

Implementing Huffman involves a **Min-Heap** and **Tree pointers**. This can be scary for a newbie. Below is a **simplified version** that focuses on the logic. Instead of a complex Min-Heap, I use a simple array and a custom sort function to simulate the priority queue so you can understand the _Huffman logic_ clearly.

C

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 1. Structure for a Tree Node
struct MinHeapNode {
    char data;              // The character (e.g., 'a')
    unsigned freq;          // Frequency (e.g., 10)
    struct MinHeapNode *left, *right; // Left and Right children
};

// 2. Structure for the Min Heap (Collection of nodes)
struct MinHeap {
    unsigned size;
    unsigned capacity;
    struct MinHeapNode** array;
};

// Helper function to create a new node
struct MinHeapNode* newNode(char data, unsigned freq) {
    struct MinHeapNode* temp = (struct MinHeapNode*)malloc(sizeof(struct MinHeapNode));
    temp->left = temp->right = NULL;
    temp->data = data;
    temp->freq = freq;
    return temp;
}

// 3. Helper to Swap two nodes (used in sorting/heapifying)
void swapMinHeapNode(struct MinHeapNode** a, struct MinHeapNode** b) {
    struct MinHeapNode* t = *a;
    *a = *b;
    *b = t;
}

// 4. A Simple "Sort" function to simulate Priority Queue behavior
// (In a pro code, we would use a Min-Heapify function, but this is easier to read)
void sortHeap(struct MinHeap* minHeap) {
    for (int i = 0; i < minHeap->size - 1; i++) {
        for (int j = 0; j < minHeap->size - i - 1; j++) {
            if (minHeap->array[j]->freq < minHeap->array[j + 1]->freq) {
                // We want the SMALLEST at the END of the array for easy extraction
                // (Just a simple reversal of logic for easy popping)
                swapMinHeapNode(&minHeap->array[j], &minHeap->array[j+1]);
            }
        }
    }
}

// 5. The Main Huffman Algorithm
struct MinHeapNode* buildHuffmanTree(char data[], int freq[], int size) {
    struct MinHeapNode *left, *right, *top;
    
    // Create the initial pool of nodes
    struct MinHeap* minHeap = (struct MinHeap*)malloc(sizeof(struct MinHeap));
    minHeap->size = size;
    minHeap->array = (struct MinHeapNode**)malloc(minHeap->size * sizeof(struct MinHeapNode*));
    
    for (int i = 0; i < size; ++i)
        minHeap->array[i] = newNode(data[i], freq[i]);

    // Iterate while size of heap is not 1
    while (minHeap->size != 1) {
        
        // Sort to get smallest nodes at the end (Simulating Extract Min)
        sortHeap(minHeap);

        // Step 1: Extract the two nodes with the smallest frequency
        left = minHeap->array[minHeap->size - 1];
        minHeap->size--; // Reduce size
        
        right = minHeap->array[minHeap->size - 1];
        minHeap->size--; // Reduce size

        // Step 2: Create a new internal node with frequency = left + right
        // '$' is a special character for internal nodes
        top = newNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;

        // Step 3: Add this new node back to the heap
        minHeap->array[minHeap->size] = top;
        minHeap->size++;
    }

    // The remaining node is the root
    return minHeap->array[0];
}

// 6. Function to print the codes (Traversing the tree)
void printCodes(struct MinHeapNode* root, int arr[], int top) {
    // 0 on Left, 1 on Right
    if (root->left) {
        arr[top] = 0;
        printCodes(root->left, arr, top + 1);
    }
    if (root->right) {
        arr[top] = 1;
        printCodes(root->right, arr, top + 1);
    }

    // If it's a leaf node, print the character and its code
    if (!(root->left) && !(root->right)) {
        printf("%c: ", root->data);
        for (int i = 0; i < top; ++i)
            printf("%d", arr[i]);
        printf("\n");
    }
}

int main() {
    char arr[] = { 'a', 'b', 'c', 'd' };
    int freq[] = { 10, 50, 40, 20 };
    int size = sizeof(arr) / sizeof(arr[0]);

    printf("--- Huffman Codes ---\n");
    struct MinHeapNode* root = buildHuffmanTree(arr, freq, size);

    int printArr[100], top = 0;
    printCodes(root, printArr, top);

    return 0;
}
```

**Output:**

Plaintext

```
--- Huffman Codes ---
b: 0
a: 100
d: 101
c: 11
```

_(Notice how 'b' has the highest frequency (50) and gets the shortest code `0`, while 'a' has the lowest (10) and gets the longest `100`.)_