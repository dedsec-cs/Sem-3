## **Topic: Mathematic Properties Of Arithmetic Mean**

The Arithmetic Mean has several important mathematical properties that make it a very useful measure of central tendency.

### 1. Total of the deviations of the items from the mean is equal to zero.

This is a fundamental property. A "deviation" is the difference between an individual value ($X$) and the mean ($\bar{X}$).

This property states that if you find the deviation for every single value in the dataset and then add all those deviations together, the total sum will always be zero. This is because the mean is the "balancing point" of the dataset; the sum of the negative deviations (values below the mean) perfectly cancels out the sum of the positive deviations (values above the mean).

**Formula:**
* **For Individual Series:** $\sum (X - \bar{X}) = 0$
* **For Discrete/Continuous Series:** $\sum f(X - \bar{X}) = 0$ or $\sum f(m - \bar{X}) = 0$

---

**Example (Individual Series):**
Let's use the data from our very first example: 60, 70, 85, 45, 90.

1.  **First, find the mean ($\bar{X}$):**
    $\bar{X} = \frac{60 + 70 + 85 + 45 + 90}{5} = \frac{350}{5} = 70$
    The mean is **70**.

2.  **Now, find the deviations ($X - \bar{X}$) and sum them.**

| Marks ($X$) | Mean ($\bar{X}$) | Deviation ($X - \bar{X}$)    |
| :---------- | :--------------- | :--------------------------- |
| 60          | 70               | 60 - 70 = -10                |
| 70          | 70               | 70 - 70 = 0                  |
| 85          | 70               | 85 - 70 = 15                 |
| 45          | 70               | 45 - 70 = -25                |
| 90          | 70               | 90 - 70 = 20                 |
| **Total**   |                  | **$\sum (X - \bar{X}) = 0$** |

* **Sum of deviations:** $(-10) + 0 + 15 + (-25) + 20$
* Sum of positives: $15 + 20 = 35$
* Sum of negatives: $(-10) + (-25) = -35$
* **Total Sum:** $35 + (-35) = 0$

This proves the property.

---

**Example (Discrete Series):**
Let's use the discrete series example where the mean ($\bar{X}$) was **28.857**.
The $X$ values were: 10, 20, 30, 40, 50
The frequencies ($f$) were: 5, 8, 12, 6, 4 

1.  **Find the deviations ($X - \bar{X}$).**
2.  **Multiply the deviation by its frequency ($f(X - \bar{X})$).**
3.  **Sum the final column.**

| Marks ($X$) | Frequency ($f$) | Mean ($\bar{X}$) | Deviation ($X - \bar{X}$) | $f(X - \bar{X})$ |
| :--- | :--- | :--- | :--- | :--- |
| 10 | 5 | 28.857 | 10 - 28.857 = -18.857 | 5 $\times$ -18.857 = -94.285 |
| 20 | 8 | 28.857 | 20 - 28.857 = -8.857 | 8 $\times$ -8.857 = -70.856 |
| 30 | 12 | 28.857 | 30 - 28.857 = 1.143 | 12 $\times$ 1.143 = 13.716 |
| 40 | 6 | 28.857 | 40 - 28.857 = 11.143 | 6 $\times$ 11.143 = 66.858 |
| 50 | 4 | 28.857 | 50 - 28.857 = 21.143 | 4 $\times$ 21.143 = 84.572 |
| **Total** | **$N=35$** | | | **$\sum f(X - \bar{X}) = 0.005$** |

*(Note: The sum is 0.005 and not exactly 0. This is only due to rounding our mean ($\bar{X}$) to three decimal places. If we had used the exact fraction $\frac{1010}{35}$, the sum would be exactly 0.)*

---

### 2. Combined Mean Of The Two Groups

This property allows you to calculate the overall mean for a combined group, as long as you know the mean and the number of items in each individual subgroup.

You **cannot** simply take the average of the two means. You must "weight" each mean by the number of items in its group. The combined mean is the **total sum of all values in all groups** divided by the **total number of items in all groups**.

**Formula:**
If you have two groups, Group 1 and Group 2:
* $N_1$ = Number of items in Group 1
* $\bar{X}_1$ = Mean of Group 1
* $N_2$ = Number of items in Group 2
* $\bar{X}_2$ = Mean of Group 2

The combined mean ($\bar{X}_{12}$) is:
$$\bar{X}_{12} = \frac{(N_1 \times \bar{X}_1) + (N_2 \times \bar{X}_2)}{N_1 + N_2}$$

* $(N_1 \times \bar{X}_1)$ gives the total sum of all values in Group 1.
* $(N_2 \times \bar{X}_2)$ gives the total sum of all values in Group 2.
* $N_1 + N_2$ is the total number of items in both groups.

(This formula can be extended for three or more groups).

---

**Example:**
In a university, the 40 students in Section A have a mean weight of 60 kg, while the 60 students in Section B have a mean weight of 70 kg. Find the combined mean weight of all 100 students.

**Solution:**
We are given:
* **Group 1 (Section A):**
    * $N_1 = 40$ students
    * $\bar{X}_1 = 60$ kg
* **Group 2 (Section B):**
    * $N_2 = 60$ students
    * $\bar{X}_2 = 70$ kg

**Steps:**
1.  **Find the total weight of Section A:**
    $N_1 \times \bar{X}_1 = 40 \times 60 = 2400$ kg
2.  **Find the total weight of Section B:**
    $N_2 \times \bar{X}_2 = 60 \times 70 = 4200$ kg
3.  **Find the total combined weight of both sections:**
    $2400 + 4200 = 6600$ kg
4.  **Find the total number of students:**
    $N_1 + N_2 = 40 + 60 = 100$ students
5.  **Apply the formula:**
    $\bar{X}_{12} = \frac{6600}{100} = 66$ kg

**Summary Table:**

| Section | Number of Students ($N$) | Mean Weight ($\bar{X}$) | Total Weight ($N \times \bar{X}$) |
| :--- | :--- | :--- | :--- |
| A | 40 | 60 kg | 2400 kg |
| B | 60 | 70 kg | 4200 kg |
| **Combined** | **$N_1 + N_2 = 100$** | | **Total Sum = 6600 kg** |

**Answer:** The combined mean weight of all 100 students is 66 kg.

Here are the notes on Weighted, Geometric, and Harmonic Means.

---

## Weighted Mean

The **Weighted Arithmetic Mean** is an average where some values in the dataset are considered more important (or have more "weight") than others.

In a simple mean, every value has an equal weight (a weight of 1). In a weighted mean, each value ($X$) is multiplied by its assigned weight ($W$) before being summed. The total sum is then divided by the sum of all the weights.

This is commonly used for calculating a final grade (where exams are "weighted" more than homework) or in stock market indices.

### Formula
$$\bar{X}_w = \frac{\sum WX}{\sum W}$$

Where:
* $\bar{X}_w$ = The Weighted Mean
* $X$ = The value of each item
* $W$ = The weight assigned to each item
* $\sum WX$ = The sum of the product of each value and its weight
* $\sum W$ = The sum of all the weights

---

### Solved Example

**Question:** A student's final grade in a course is determined by three components: Homework (weighted 20%), a Midterm exam (weighted 30%), and a Final Exam (weighted 50%). The student's scores are: 90 on Homework, 80 on the Midterm, and 88 on the Final Exam. Calculate the student's weighted mean (final grade).

**Solution:**
Here, the scores are the values ($X$) and the percentages are the weights ($W$).

**Steps:**
1.  Identify the values ($X$) and their corresponding weights ($W$).
2.  Create a column $WX$ by multiplying each $X$ by its $W$.
3.  Find the sum of the $WX$ column ($\sum WX$).
4.  Find the sum of the $W$ column ($\sum W$).
5.  Apply the formula.

**Calculation Table:**
| Component | Score ($X$) | Weight ($W$) | $WX$ ($W \times X$) |
| :--- | :--- | :--- | :--- |
| Homework | 90 | 20 | 20 $\times$ 90 = 1800 |
| Midterm | 80 | 30 | 30 $\times$ 80 = 2400 |
| Final Exam | 88 | 50 | 50 $\times$ 88 = 4400 |
| **Total** | | **$\sum W = 100$** | **$\sum WX = 8600$** |

**Calculation:**
$$\bar{X}_w = \frac{\sum WX}{\sum W} = \frac{8600}{100} = 86$$

**Answer:** The student's final weighted mean grade is 86.

---

## Geometric Mean

The **Geometric Mean (GM)** is a type of average used for data that is multiplicative, not additive. It is most often used to find the average **rate of change**, such as average growth rates (e.g., population growth, interest rates, investment returns).

It is calculated by multiplying all $N$ values together and then taking the $N$-th root of the product.

### Formula
$$GM = \sqrt[N]{X_1 \times X_2 \times \dots \times X_N}$$

Where:
* $N$ = The total number of values
* $X_1, X_2, \dots$ = The values in the dataset (which must all be positive)

**Important:** When dealing with percentage growth rates (e.g., 15% growth), you must first convert them to growth factors (e.g., 1.15). A loss of 5% would be a factor of 0.95 (since $1.00 - 0.05 = 0.95$).

---

### Solved Example

**Question:** An investment's value grows by 5% in Year 1, 10% in Year 2, and 21% in Year 3. What is the average annual rate of growth?

**Solution:**
We cannot just average the percentages. We must use the Geometric Mean of the growth *factors*.

1.  **Convert percentages to growth factors ($X$):**
    * Year 1 ($X_1$): 5% growth = 1.05
    * Year 2 ($X_2$): 10% growth = 1.10
    * Year 3 ($X_3$): 21% growth = 1.21
2.  **Count the number of values ($N$):**
    * $N = 3$ (for 3 years)
3.  **Apply the formula:**
    $$GM = \sqrt[3]{1.05 \times 1.10 \times 1.21}$$
    * First, multiply the numbers inside:
        $1.05 \times 1.10 \times 1.21 = 1.39755$
    * Now, find the 3rd (cube) root:
        $$GM = \sqrt[3]{1.39755} \approx 1.118$$

4.  **Convert the GM factor back to a percentage:**
    * Average growth factor = 1.118
    * Average growth rate = $1.118 - 1.00 = 0.118$
    * Multiply by 100 to get the percentage: $0.118 \times 100 = 11.8\%$

**Answer:** The average annual rate of growth is 11.8%.

---

## Harmonic Mean

The **Harmonic Mean (HM)** is another type of average, typically used for sets of rates, specifically when averaging **speeds** (like km/h) over a fixed distance, or other rates like "items per hour."

It is defined as the reciprocal of the arithmetic mean of the reciprocals of the observations. This sounds complex, but the formula is straightforward. It gives less weight to large values and more weight to small values.

### Formula
$$HM = \frac{N}{\sum \left( \frac{1}{X} \right)}$$
or
$$HM = \frac{N}{\frac{1}{X_1} + \frac{1}{X_2} + \dots + \frac{1}{X_N}}$$

Where:
* $N$ = The total number of values
* $X$ = The values in the dataset
* $\sum \left( \frac{1}{X} \right)$ = The sum of the reciprocals of all values

---

### Solved Example

**Question:** A car travels to a city at a speed of 60 km/h and returns by the same route at a speed of 40 km/h. What is the average speed for the entire journey?

*(Note: The answer is **not** the arithmetic mean of 50 km/h)*

**Solution:**
This is an average of speeds over a fixed, equal distance, so the Harmonic Mean is the correct method.

1.  **Identify the values ($X$):**
    * $X_1 = 60$
    * $X_2 = 40$
2.  **Count the number of values ($N$):**
    * $N = 2$
3.  **Find the reciprocal of each value ($1/X$) and sum them.**

**Calculation Table:**
| Trip | Speed ($X$) | Reciprocal ($\frac{1}{X}$) |
| :--- | :--- | :--- |
| 1 (to city) | 60 | 1/60 |
| 2 (return) | 40 | 1/40 |
| **Total** | $N = 2$ | **$\sum (\frac{1}{X}) = \frac{1}{60} + \frac{1}{40}$** |

4.  **Calculate the sum of reciprocals:**
    * To add $\frac{1}{60} + \frac{1}{40}$, find a common denominator (which is 120).
    * $\frac{1}{60} = \frac{2}{120}$
    * $\frac{1}{40} = \frac{3}{120}$
    * $\sum (\frac{1}{X}) = \frac{2}{120} + \frac{3}{120} = \frac{5}{120}$

5.  **Apply the formula:**
    $$HM = \frac{N}{\sum \left( \frac{1}{X} \right)}$$
    $$HM = \frac{2}{\frac{5}{120}}$$
    * To divide by a fraction, we invert and multiply:
        $HM = 2 \times \frac{120}{5}$
        $HM = \frac{240}{5}$
        $HM = 48$

**Answer:** The average speed for the entire journey is 48 km/h.