## Mode

---

### Definition

The **Mode** is a measure of central tendency that identifies the **most frequently occurring value** in a dataset. Unlike the mean (average) or median (middle value), the mode is simply the value that appears the highest number of times.

A dataset can have:
* **One Mode (Unimodal):** If one value appears most frequently. (e.g., $1, 2, 2, 3, 4$)
* **Two Modes (Bimodal):** If two different values have the same highest frequency. (e.g., $1, 2, 2, 3, 3, 4$)
* **Multiple Modes (Multimodal):** If more than two values share the same highest frequency.
* **No Mode:** If all values occur with the same frequency (e.g., $1, 2, 3, 4, 5$).

---

### Formula

There is **no single calculation formula** for the mode in the same way there is for the mean.
* For **discrete data**, the mode is found by **inspection** (counting frequencies).
* For **continuous frequency distribution**, a specific formula is used to *estimate* the mode from the modal class.

**Continuous Frequency Distribution Formula:**
$$
\text{Mode} = L + \frac{f_1 - f_0}{2f_1 - f_0 - f_2} \times i
$$
(The components of this formula are explained in the continuous distribution section below).

---

### Examples

#### In Case Of Discrete Distribution

This category includes both raw, ungrouped data and data organized into a discrete frequency table.

**Case 1: Ungrouped Data (Raw List)**

**Procedure:** Count the occurrences of each number and find the one that appears most.

* **Example (Unimodal):**
    * **Data:** $5, 7, 8, 2, 7, 10, 7$
    * **Frequencies:** 5 (1), 8 (1), 2 (1), 10 (1), **7 (3 times)**
    * **Mode = 7**

* **Example (Bimodal):**
    * **Data:** $10, 15, 12, 10, 18, 15, 11$
    * **Frequencies:** **10 (2 times)**, **15 (2 times)**, 12 (1), 18 (1), 11 (1)
    * **Mode = 10 and 15**

* **Example (No Mode):**
    * **Data:** $1, 2, 3, 4, 5, 6$
    * **Frequencies:** All values appear only once.
    * **Mode = No Mode**

**Case 2: Discrete Frequency Distribution (Table)**

**Procedure:** Look for the **highest frequency ($f$)** in the table. The **mode** is the corresponding value ($x$) in that row.

**Example:**

| $x$ (Value) | $f$ (Frequency) |                                    |
| :---------: | :-------------: | ---------------------------------- |
|     10      |        2        |                                    |
|     20      |        5        |                                    |
|     30      |        8        | $\leftarrow$ **Highest Frequency** |
|     40      |        3        |                                    |
|     50      |        1        |                                    |

1.  **Find Highest Frequency:** The highest frequency ($f$) is **8**.
2.  **Find Corresponding $x$:** The $x$ value for $f=8$ is **30**.
3.  **Mode = 30**

---

#### In Case Of Continuous Frequency Distribution

In this case, data is grouped into class intervals (e.g., $10-20$). We cannot find an exact mode, so we **estimate** it using a formula.

**Procedure:**
1.  **Identify the Modal Class:** This is the class interval with the **highest frequency ($f_1$)**.
2.  **Apply the Mode Formula:**

$$
\text{Mode} = L + \frac{f_1 - f_0}{2f_1 - f_0 - f_2} \times i
$$

**Explanation of Formula Components:**
* **$L$** = **Lower limit** of the Modal Class.
* **$f_1$** = **Frequency** of the Modal Class (the highest frequency).
* **$f_0$** = **Frequency** of the class **preceding** (before) the Modal Class.
* **$f_2$** = **Frequency** of the class **succeeding** (after) the Modal Class.
* **$i$** = **Class width** (Upper limit - Lower limit) of the Modal Class.

**Example:**

| Class Interval | $f$ (Frequency) | |
| :------------: | :-------------: | :--- |
| $10-20$        | 5               | ($f_0$) |
| $20-30$        | 15              | ($f_1$) $\leftarrow$ **Modal Class** |
| $30-40$        | 8               | ($f_2$) |
| $40-50$        | 4               | |

1.  **Identify Modal Class:** The highest frequency is **15**, so the Modal Class is **$20-30$**.

2.  **Identify Components:**
    * $L$ = $20$ (Lower limit of $20-30$)
    * $f_1$ = $15$ (Frequency of $20-30$)
    * $f_0$ = $5$ (Frequency of the class *before*, $10-20$)
    * $f_2$ = $8$ (Frequency of the class *after*, $30-40$)
    * $i$ = $10$ ($30 - 20$)

3.  **Apply Formula:**
    $$
    \text{Mode} = 20 + \frac{15 - 5}{2(15) - 5 - 8} \times 10
    $$
    $$
    \text{Mode} = 20 + \frac{10}{30 - 13} \times 10
    $$
    $$
    \text{Mode} = 20 + \frac{10}{17} \times 10
    $$
    $$
    \text{Mode} = 20 + \frac{100}{17}
    $$
    $$
    \text{Mode} = 20 + 5.88
    $$
    $$
    \text{Mode} \approx \mathbf{25.88}
    $$
    The estimated mode is 25.88, which falls logically within the modal class ($20-30$).

**Advanced Note: Empirical Relationship**
For distributions that are moderately skewed (not symmetrical), there is an approximate relationship between the mean, median, and mode:

$$
\text{Mode} \approx 3 \times \text{Median} - 2 \times \text{Mean}
$$
This is often used to estimate the mode if the mean and median are already known.