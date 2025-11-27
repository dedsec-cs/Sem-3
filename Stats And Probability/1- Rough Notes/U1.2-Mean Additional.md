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

| Section      | Number of Students ($N$) | Mean Weight ($\bar{X}$) | Total Weight ($N \times \bar{X}$) |
| :----------- | :----------------------- | :---------------------- | :-------------------------------- |
| A            | 40                       | 60 kg                   | 2400 kg                           |
| B            | 60                       | 70 kg                   | 4200 kg                           |
| **Combined** | **$N_1 + N_2 = 100$**    |                         | **Total Sum = 6600 kg**           |

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

| Component  | Score ($X$) | Weight ($W$)       | $WX$ ($W \times X$)   |
| :--------- | :---------- | :----------------- | :-------------------- |
| Homework   | 90          | 20                 | 20 $\times$ 90 = 1800 |
| Midterm    | 80          | 30                 | 30 $\times$ 80 = 2400 |
| Final Exam | 88          | 50                 | 50 $\times$ 88 = 4400 |
| **Total**  |             | **$\sum W = 100$** | **$\sum WX = 8600$**  |

**Calculation:**
$$\bar{X}_w = \frac{\sum WX}{\sum W} = \frac{8600}{100} = 86$$

**Answer:** The student's final weighted mean grade is 86.

---
