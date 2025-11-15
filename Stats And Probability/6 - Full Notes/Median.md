## Median

---

### Definition

The **Median** is a **measure of central tendency**. It is the single value that represents the **exact middle** of a dataset that has been arranged in ascending (smallest to largest) or descending (largest to smallest) order.

The median is also known as the **50th percentile** because it divides the dataset into two equal halves:
* $50\%$ of the data values are **less than or equal to** the median.
* $50\%$ of the data values are **greater than or equal to** the median.

The median is often preferred over the mean (average) when a dataset has **extreme values (outliers)**, because the median is not affected by them.

---

### Formula For Both Odd And Even

The "formula" for the median is first about finding its **position** in an ordered dataset. Let **$N$** be the total number of observations (the count of all data points).

**Step 1:** **Order the data** from smallest to largest.

**Step 2:** Find the position of the median using the formula:
$$
\text{Median Position} = \frac{N + 1}{2}
$$

**Case 1: $N$ is Odd (e.g., $N=5, 7, 9$)**
* When $N$ is odd, the formula $\frac{N + 1}{2}$ gives a whole number.
* **Formula:** The median is the value at this *exact position*.
* **Example:** If $N=7$, the position is $\frac{7 + 1}{2} = 4$. The median is the **4th value** in the ordered list.

**Case 2: $N$ is Even (e.g., $N=6, 8, 10$)**
* When $N$ is even, the formula $\frac{N + 1}{2}$ gives a decimal (e.g., 3.5, 5.5).
* A position like "3.5" means the median lies *between* the 3rd and 4th values.
* **Formula:** The median is the **average of the two middle values** (the values on either side of the decimal position).
* **Example:** If $N=6$, the position is $\frac{6 + 1}{2} = 3.5$. The median is the **average of the 3rd and 4th values**.

---

### Examples

#### Ungrouped Data

This is a raw list of numbers.

**Example 1: $N$ is Odd**
* **Data:** $19, 12, 16, 25, 14$
* **Step 1 (Order):** $12, 14, 16, 19, 25$
* **Step 2 ($N$):** $N = 5$ (Odd)
* **Step 3 (Position):** $\frac{5 + 1}{2} = \frac{6}{2} = 3$rd position.
* **Step 4 (Median):** The 3rd value in the ordered list is **16**.

**Example 2: $N$ is Even**
* **Data:** $30, 10, 20, 50, 40, 60$
* **Step 1 (Order):** $10, 20, 30, 40, 50, 60$
* **Step 2 ($N$):** $N = 6$ (Even)
* **Step 3 (Position):** $\frac{6 + 1}{2} = \frac{7}{2} = 3.5$th position.
* **Step 4 (Median):** The position 3.5 is between the 3rd and 4th values.
    * 3rd value = $30$
    * 4th value = $40$
    * Median = $\frac{30 + 40}{2} = \frac{70}{2} = \mathbf{35}$

---

#### Discrete Frequency Distribution

This is when data is presented in a table showing each value ($x$) and how many times it occurs (frequency, $f$).

**Procedure:**
1.  Calculate the **Cumulative Frequency ($cf$)**. This is a running total of the frequencies.
2.  Find the total frequency, $N = \sum f$.
3.  Find the median position using $\frac{N + 1}{2}$.
4.  Locate the $cf$ value that is **just greater than or equal to** the median position.
5.  The median is the **$x$ value** (the data value, not the frequency) corresponding to that $cf$.

**Example:**

| $x$ (Marks) | $f$ (Students) | $cf$ (Cumulative Freq.) |
| :---------: | :------------: | :---------------------: |
| 10          | 2              | 2                       |
| 20          | 5              | $2 + 5 = 7$             |
| 30          | 8              | $7 + 8 = 15$            |
| 40          | 3              | $15 + 3 = 18$           |
| 50          | 2              | $18 + 2 = 20$           |

* **Step 2 ($N$):** $N = \sum f = 20$ (Even)
* **Step 3 (Position):** $\frac{20 + 1}{2} = \frac{21}{2} = 10.5$th position.
* **Step 4 (Locate $cf$):** We need to find the $cf$ just greater than or equal to $10.5$.
    * $cf$ of 2 is too small.
    * $cf$ of 7 is too small.
    * $cf$ of **15** is the first one greater than $10.5$.
* **Step 5 (Median):** The $x$ value corresponding to the $cf$ of 15 is **30**.
    * (This means the 8th, 9th, 10th, 11th, 12th, 13th, 14th, and 15th students all scored 30. Since we are looking for the 10.5th value, it falls in this group.)

---

#### Continuous Frequency Distribution

This is when data is grouped into class intervals (e.g., $10-20, 20-30$). We first find the *Median Class* and then use a formula to estimate the median value within that class.

**Procedure:**
1.  Calculate the **Cumulative Frequency ($cf$)**.
2.  Find the total frequency, $N = \sum f$.
3.  Find the median *class location* using $\frac{N}{2}$. (Note: We use $\frac{N}{2}$ here, not $\frac{N+1}{2}$, as per standard convention for continuous data).
4.  Find the **Median Class**: This is the class interval whose $cf$ is **just greater than or equal to** the $\frac{N}{2}$ value.
5.  Apply the Median Formula:

$$
\text{Median} = L + \frac{\left(\frac{N}{2} - cf\right)}{f} \times i
$$

Where:
* **$L$** = **Lower limit** of the Median Class.
* **$N$** = **Total frequency** ($\sum f$).
* **$cf$** = **Cumulative frequency of the class *preceding* (before) the Median Class**.
* **$f$** = **Frequency** of the **Median Class** itself.
* **$i$** = **Class width** (Upper limit - Lower limit) of the Median Class.

**Example:**

| Class Interval (Marks) | $f$ (Students) | $cf$ (Cumulative Freq.) |
| :--------------------: | :------------: | :---------------------: |
| $0-10$                 | 5              | 5                       |
| $10-20$                | 10             | $5 + 10 = 15$           |
| $20-30$                | 20             | $15 + 20 = 35$          |
| $30-40$                | 8              | $35 + 8 = 43$           |
| $40-50$                | 7              | $43 + 7 = 50$           |

* **Step 2 ($N$):** $N = 50$
* **Step 3 (Location):** $\frac{N}{2} = \frac{50}{2} = 25$th position.
* **Step 4 (Median Class):** We look for the $cf$ just greater than or equal to $25$.
    * $cf$ of 5 is too small.
    * $cf$ of 15 is too small.
    * $cf$ of **35** is the first one greater than $25$.
    * Therefore, the **Median Class** is **$20-30$**.

* **Step 5 (Apply Formula):**
    * $L$ = $20$ (Lower limit of $20-30$)
    * $N$ = $50$
    * $cf$ = $15$ (The $cf$ of the class *before* $20-30$)
    * $f$ = $20$ (The frequency of the $20-30$ class)
    * $i$ = $10$ ($30 - 20$)

$$
\text{Median} = 20 + \frac{\left(\frac{50}{2} - 15\right)}{20} \times 10
$$
$$
\text{Median} = 20 + \frac{(25 - 15)}{20} \times 10
$$
$$
\text{Median} = 20 + \frac{10}{20} \times 10
$$
$$
\text{Median} = 20 + 0.5 \times 10
$$
$$
\text{Median} = 20 + 5
$$
$$
\text{Median} = \mathbf{25}
$$
The median mark is 25. This value makes sense as it falls within our $20-30$ median class.