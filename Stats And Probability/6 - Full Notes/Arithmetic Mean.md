## Arithmetic Mean

### Definition

The **Arithmetic Mean**, often simply called the **mean** or **average**, is the most common measure of central tendency. It is a single value that represents the "center" or "balancing point" of a set of data.

It is calculated by **summing all the values** in the dataset and then **dividing by the total number of values**. The mean is sensitive to all values in the data, including extremely large or small values (known as outliers).

---

### Formula

The formula for the mean differs slightly in its notation depending on whether you are calculating it for an entire **population** or just a **sample**.

* **Population Mean ($\mu$):** This is the mean of *all* individuals in a group of interest.
    $$
    \mu = \frac{\sum X}{N}
    $$
    * $\mu$ (mu) is the symbol for the population mean.
    * $\sum$ (Sigma) means "the sum of".
    * $X$ represents each individual value in the population.
    * $N$ is the total number of individuals in the population.

* **Sample Mean ($\bar{x}$):** This is the mean of a *subset* (a sample) taken from a population.
    $$
    \bar{x} = \frac{\sum x}{n}
    $$
    * $\bar{x}$ (x-bar) is the symbol for the sample mean.
    * $x$ represents each individual value in the sample.
    * $n$ is the total number of individuals in the sample.

For the following examples, we will use the sample notation ($\bar{x}$ and $n$), which is most commonly used in practice.

---

### Example

#### In Case Of Individual Series

An **individual series** (or ungrouped data) is a raw list of data points where each observation is listed individually.

**Procedure:**
1.  **Sum** all the individual values ($\sum x$).
2.  **Count** the total number of values ($n$).
3.  **Divide** the sum by the count.

**Example:**
A student's scores in 5 subjects are: $70, 75, 80, 85, 90$.

1.  **Sum the values ($\sum x$):**
    $70 + 75 + 80 + 85 + 90 = 400$

2.  **Count the values ($n$):**
    There are 5 scores, so $n = 5$.

3.  **Divide:**
    $\bar{x} = \frac{\sum x}{n} = \frac{400}{5} = 80$

The arithmetic mean (average score) is **80**.

#### In Case Of Frequency Distribution

A **frequency distribution** (or grouped data) organizes the data by showing how many times each value (or range of values) occurs.

**Case 1: Discrete Frequency Distribution**
Here, we have distinct data values ($x$) and their corresponding frequencies ($f$).

**Formula:**
$$
\bar{x} = \frac{\sum (f \cdot x)}{\sum f} \quad \text{or} \quad \bar{x} = \frac{\sum fx}{N}
$$
* $f$ is the frequency of each value.
* $x$ is the data value.
* $fx$ is the product of the value and its frequency.
* $\sum fx$ is the sum of all these products.
* $\sum f$ (or $N$) is the sum of all frequencies (the total number of observations).

**Example:**
The number of goals scored by a football team in 20 matches.

| Goals Scored ($x$) | Frequency ($f$) (No. of Matches) |
| :----------------: | :------------------------------: |
| 0                  | 2                                |
| 1                  | 5                                |
| 2                  | 8                                |
| 3                  | 3                                |
| 4                  | 2                                |

**Procedure (using a table):**
1.  Create a new column $fx$ by multiplying $f$ and $x$ for each row.
2.  Sum the $f$ column to get $N$ ($\sum f$).
3.  Sum the $fx$ column to get $\sum fx$.
4.  Divide $\sum fx$ by $N$.

| Goals Scored ($x$) | Frequency ($f$) | $f \cdot x$ |
| :----------------: | :-------------: | :---------: |
| 0                  | 2               | $2 \times 0 = 0$ |
| 1                  | 5               | $5 \times 1 = 5$ |
| 2                  | 8               | $8 \times 2 = 16$ |
| 3                  | 3               | $3 \times 3 = 9$ |
| 4                  | 2               | $2 \times 4 = 8$ |
| **Total** | **$\sum f = 20$** | **$\sum fx = 38$** |

**Calculation:**
$\bar{x} = \frac{\sum fx}{N} = \frac{38}{20} = 1.9$

The mean number of goals scored per match is **1.9**.

**Case 2: Continuous Frequency Distribution**
Here, data is grouped into class intervals (e.g., $0-10, 10-20$). Since we don't know the exact values, we must first find the **midpoint** of each class to represent $x$.

**Midpoint ($m$) Formula:** $m = \frac{\text{Lower Class Limit} + \text{Upper Class Limit}}{2}$

**Formula (using Midpoints):**
$$
\bar{x} = \frac{\sum (f \cdot m)}{\sum f} \quad \text{or} \quad \bar{x} = \frac{\sum fm}{N}
$$

**Example:**
The weights (in kg) of 50 students.

| Weight (kg) [Class] | Frequency ($f$) (No. of Students) |
| :-----------------: | :-------------------------------: |
| $40 - 50$           | 5                                 |
| $50 - 60$           | 15                                |
| $60 - 70$           | 20                                |
| $70 - 80$           | 10                                |

**Procedure (using a table):**
1.  Find the **Midpoint ($m$)** for each class.
2.  Create a new column $fm$ by multiplying $f$ and $m$.
3.  Sum the $f$ column to get $N$ ($\sum f$).
4.  Sum the $fm$ column to get $\sum fm$.
5.  Divide $\sum fm$ by $N$.

| Weight (kg) [Class] | Frequency ($f$) | Midpoint ($m$) | $f \cdot m$ |
| :-----------------: | :-------------: | :--------------------------: | :---------------: |
| $40 - 50$           | 5               | $(40+50)/2 = 45$             | $5 \times 45 = 225$ |
| $50 - 60$           | 15              | $(50+60)/2 = 55$             | $15 \times 55 = 825$ |
| $60 - 70$           | 20              | $(60+70)/2 = 65$             | $20 \times 65 = 1300$ |
| $70 - 80$           | 10              | $(70+80)/2 = 75$             | $10 \times 75 = 750$ |
| **Total** | **$\sum f = 50$** | - | **$\sum fm = 3100$** |

**Calculation:**
$\bar{x} = \frac{\sum fm}{N} = \frac{3100}{50} = 62$

The mean weight of the students is **62 kg**.

---

### **Topic: Arithmetic Mean**
### **Chapter: Statistical Techniques I**

The **Arithmetic Mean**, often just called the "mean" or "average," is the most common measure of central tendency. It represents a "typical" value in a set of data.

It is calculated by summing all the values in the dataset and then dividing by the total number of values.

* $\bar{X}$ (read as "X-bar") is the symbol for the Arithmetic Mean.
* $X$ refers to the individual values (observations) in the dataset.
* $N$ is the total number of values in the dataset.
* $\sum$ (Sigma) is a Greek letter that means "sum up." So, $\sum X$ means "sum up all the $X$ values."

---

# For Individual Series Or Ungrouped Data

An **Individual Series** (or ungrouped data) is a simple list of values, where each value is a separate observation. For example: {5, 10, 15, 20} or {100, 250, 175}.

## Direct Method

This is the most straightforward method, used when the data values are simple and not too large.

**Formula:**
$$\bar{X} = \frac{\sum X}{N}$$

**Steps:**
1.  **Add** all the individual values together to get the total sum ($\sum X$).
2.  **Count** the total number of values to get $N$.
3.  **Divide** the total sum ($\sum X$) by the number of values ($N$).

---

### Example 1: Simple Question

**Question:** The marks of 5 students in a test are: 60, 70, 85, 45, and 90. Find the arithmetic mean of their marks.

**Solution:**
Here, the values ($X$) are the marks.
We first organize the data in a table to find the sum.

| Student | Marks ($X$) |
| :--- | :--- |
| 1 | 60 |
| 2 | 70 |
| 3 | 85 |
| 4 | 45 |
| 5 | 90 |
| **Total** | **$\sum X = 350$** |

**Calculation:**
1.  **Sum ($\sum X$):** $60 + 70 + 85 + 45 + 90 = 350$
2.  **Number of values ($N$):** There are 5 students, so $N = 5$.
3.  **Mean ($\bar{X}$):**
    $$\bar{X} = \frac{\sum X}{N} = \frac{350}{5} = 70$$

**Answer:** The arithmetic mean of the marks is 70.

---

### Example 2: Missing Value

This type of problem gives you the mean and asks you to find a missing data point.

**Question:** The average (mean) monthly salary of 4 employees is 5000. The salaries of 3 employees are 4000, 6500, and 3500. What is the salary of the 4th employee?

**Solution:**
We are given:
* Mean ($\bar{X}$) = 5000
* Number of values ($N$) = 4
* Known values: 4000, 6500, 3500
* Missing value: Let's call it $X_4$

We use the same formula: $\bar{X} = \frac{\sum X}{N}$

**Steps:**
1.  We know the total sum ($\sum X$) can be found by rearranging the formula: $\sum X = \bar{X} \times N$
2.  **Calculate the total sum:**
    $\sum X = 5000 \times 4 = 20000$
    This means the salaries of all 4 employees must add up to 20000.
3.  **Calculate the sum of known values:**
    $4000 + 6500 + 3500 = 14000$
4.  **Find the missing value:**
    The total sum (20000) minus the sum of the 3 known salaries (14000) will give us the 4th salary.
    $X_4 = 20000 - 14000 = 6000$

**Answer:** The salary of the 4th employee is 6000.

**Verification Table:**

| Employee | Salary ($X$) |
| :--- | :--- |
| 1 | 4000 |
| 2 | 6500 |
| 3 | 3500 |
| 4 (Missing) | 6000 |
| **Total ($N=4$)** | **$\sum X = 20000$** |

**Check:** $\bar{X} = \frac{20000}{4} = 5000$. This matches the problem statement.

---

### Example 3: Other Cases (Combined Mean)

This is used when you have the means of two or more separate groups and want to find the overall mean of all groups combined. You **cannot** just average the two means.

**Question:** A company has 10 male employees with a mean salary of 30,000 and 20 female employees with a mean salary of 25,000. What is the mean salary of all 30 employees?

**Solution:**
We cannot do $\frac{30000 + 25000}{2}$. We must find the **total** money paid and divide by the **total** number of employees.

**Formula for Combined Mean ($\bar{X}_{12}$):**
$$\bar{X}_{12} = \frac{(N_1 \times \bar{X}_1) + (N_2 \times \bar{X}_2)}{N_1 + N_2}$$

* $N_1$ = Number of items in group 1 (10 males)
* $\bar{X}_1$ = Mean of group 1 (30,000)
* $N_2$ = Number of items in group 2 (20 females)
* $\bar{X}_2$ = Mean of group 2 (25,000)

**Steps:**
1.  **Find the total salary for Group 1 (Males):**
    $N_1 \times \bar{X}_1 = 10 \times 30000 = 300,000$
2.  **Find the total salary for Group 2 (Females):**
    $N_2 \times \bar{X}_2 = 20 \times 25000 = 500,000$
3.  **Find the total combined salary:**
    $300,000 + 500,000 = 800,000$
4.  **Find the total combined number of employees:**
    $N_1 + N_2 = 10 + 20 = 30$
5.  **Calculate the combined mean:**
    $\bar{X}_{12} = \frac{800,000}{30} = 26,666.67$

**Data Table:**

| Group | Number of Employees ($N$) | Mean Salary ($\bar{X}$) | Total Salary ($N \times \bar{X}$) |
| :--- | :--- | :--- | :--- |
| Males | 10 | 30,000 | 300,000 |
| Females | 20 | 25,000 | 500,000 |
| **Combined** | **30** | | **800,000** |

**Answer:** The mean salary of all 30 employees is 26,666.67.

---

## Shortcut Method Or Assumed Mean Method

When the number of items is very large, or the values themselves are large (e.g., 850, 920, 1050), adding them all up (Direct Method) is time-consuming and prone to errors.

The **Shortcut Method** simplifies the calculation.
1.  We **assume** a value for the mean (call it '$A$'). This 'A' can be any value, but it's easiest if you pick a value from the middle of the dataset.
2.  We then calculate the **deviation** (difference) of each value ($X$) from this Assumed Mean ($A$). We call this deviation '$d$'.
3.  We find the average of these deviations and add it to our assumed mean.

### Formula:
$$\bar{X} = A + \frac{\sum d}{N}$$

Where:
* $A$ = Assumed Mean
* $d$ = Deviation of each item from $A$ ($d = X - A$)
* $\sum d$ = Sum of all deviations
* $N$ = Number of values

---

### Example 1: Simple Question
(Using the same data from Direct Method Example 1 for comparison)

**Question:** The marks of 5 students in a test are: 60, 70, 85, 45, and 90. Find the arithmetic mean using the Shortcut Method.

**Solution:**
Data ($X$): 60, 70, 85, 45, 90
Let's **assume** a mean ($A$). A good guess from the middle of the data is 70.
So, $A = 70$.
Now, we create a table to find the deviations ($d = X - A$).

| Marks ($X$) | Assumed Mean ($A$) | Deviation ($d = X - A$) |
| :--- | :--- | :--- |
| 60 | 70 | 60 - 70 = -10 |
| 70 | 70 | 70 - 70 = 0 |
| 85 | 70 | 85 - 70 = 15 |
| 45 | 70 | 45 - 70 = -25 |
| 90 | 70 | 90 - 70 = 20 |
| **$N = 5$** | | **$\sum d = 0$** |

**Calculation:**
1.  **Find $\sum d$ (Sum of deviations):**
    $(-10) + 0 + 15 + (-25) + 20$
    $= (-10 - 25) + (15 + 20)$
    $= -35 + 35$
    $= 0$
2.  **Apply the formula:**
    $\bar{X} = A + \frac{\sum d}{N}$
    $\bar{X} = 70 + \frac{0}{5}$
    $\bar{X} = 70 + 0$
    $\bar{X} = 70$

**Answer:** The arithmetic mean is 70. This is the exact same answer we got with the Direct Method, which proves the method works.

*(Note: If you pick a different $A$, the answer will still be the same. For example, if we chose $A = 85$, $\sum d$ would be -75, and $\bar{X} = 85 + \frac{-75}{5} = 85 - 15 = 70$.)*

---

### Example 2: Using Shortcut Method for Larger Numbers

**Question:** Calculate the mean daily wage for 7 workers using the Assumed Mean Method.
Wages (in Rupees): 520, 480, 500, 550, 470, 490, 530

**Solution:**
These numbers are large. Let's pick an Assumed Mean ($A$). A good middle value is 500.
$A = 500$
$N = 7$

**Calculation Table:**

| Wage ($X$) | Assumed Mean ($A$) | Deviation ($d = X - A$) |
| :--- | :--- | :--- |
| 520 | 500 | 20 |
| 480 | 500 | -20 |
| 500 | 500 | 0 |
| 550 | 500 | 50 |
| 470 | 500 | -30 |
| 490 | 500 | -10 |
| 530 | 500 | 30 |
| **$N = 7$** | | **$\sum d = 40$** |

**Calculation:**
1.  **Find $\sum d$ (Sum of deviations):**
    $20 + (-20) + 0 + 50 + (-30) + (-10) + 30$
    * Positives: $20 + 50 + 30 = 100$
    * Negatives: $(-20) + (-30) + (-10) = -60$
    * $\sum d = 100 - 60 = 40$
2.  **Apply the formula:**
    $\bar{X} = A + \frac{\sum d}{N}$
    $\bar{X} = 500 + \frac{40}{7}$
    $\bar{X} = 500 + 5.714$
    $\bar{X} = 505.714$

**Answer:** The mean daily wage is 505.71 (rounded). This was much easier than adding all the 3-digit numbers and dividing by 7.


Here are the notes for calculating the Arithmetic Mean for Discrete and Continuous series.

---

## Step Deviation Method

This method is an extension of the Shortcut (Assumed Mean) Method. It is used to make calculations even simpler.

We use this method when the deviations from the assumed mean ($d$) are large, but they all share a **common factor** (e.g., all are divisible by 10, 5, or 100). We "step down" these deviations by dividing them by this common factor.

* $A$ = Assumed Mean
* $N = \sum f$ (Total Frequency)
* $i$ (or $h$ or $c$) = The common factor or class interval.
* $d = X - A$ (for Discrete) or $d = m - A$ (for Continuous)
* $d'$ (read as "d-dash") = The step deviation, where $d' = \frac{d}{i}$

**Formula for Step Deviation Method:**
$$\bar{X} = A + \left( \frac{\sum fd'}{N} \right) \times i$$

---

### Discrete Series

A **Discrete Series** (or frequency array) is a dataset where specific values ($X$) are listed along with their corresponding frequencies ($f$). The frequency shows how many times each value appears in the dataset.

* $X$ = The value of the observation (e.g., marks, goals scored)
* $f$ = Frequency (e.g., number of students, number of matches)
* $N$ = Total number of items, which is $\sum f$ (the sum of all frequencies).

We will use one example and solve it with all three methods (Direct, Shortcut, and Step Deviation) to show how they all result in the same answer.

**Example:** Find the arithmetic mean of the following data:

| Marks ($X$) | 10 | 20 | 30 | 40 | 50 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| No. of Students ($f$) | 5 | 8 | 12 | 6 | 4 |

---

### Method 1: Direct Method (for Discrete Series)

**Formula:**
$$\bar{X} = \frac{\sum fX}{\sum f}$$

**Steps:**
1.  Multiply each $X$ by its corresponding $f$ to get a new column, $fX$.
2.  Add all the values in the $fX$ column to get $\sum fX$.
3.  Add all the values in the $f$ column to get $N$ (or $\sum f$).
4.  Divide $\sum fX$ by $\sum f$.

**Solution Table:**

| Marks ($X$) | No. of Students ($f$) | $fX$ ($f \times X$) |
| :--- | :--- | :--- |
| 10 | 5 | 50 |
| 20 | 8 | 160 |
| 30 | 12 | 360 |
| 40 | 6 | 240 |
| 50 | 4 | 200 |
| **Total** | **$N = \sum f = 35$** | **$\sum fX = 1010$** |

**Calculation:**
$$\bar{X} = \frac{\sum fX}{\sum f} = \frac{1010}{35}$$
$$\bar{X} = 28.857$$

**Answer:** The mean marks are 28.857.

---

### Method 2: Shortcut Method (for Discrete Series)

**Formula:**
$$\bar{X} = A + \frac{\sum fd}{N}$$
Where $d = X - A$

**Steps:**
1.  Choose an Assumed Mean ($A$) from the $X$ values. (Let's choose $A = 30$).
2.  Calculate the deviations ($d = X - A$) for each $X$.
3.  Multiply each frequency ($f$) by its corresponding deviation ($d$) to get the $fd$ column.
4.  Find the sum of the $fd$ column ($\sum fd$) and the $f$ column ($N$).
5.  Apply the formula.

**Solution Table:**
(Using $A = 30$)

| Marks ($X$) | No. of Students ($f$) | Deviation ($d = X - A$) | $fd$ ($f \times d$) |
| :--- | :--- | :--- | :--- |
| 10 | 5 | 10 - 30 = -20 | 5 $\times$ -20 = -100 |
| 20 | 8 | 20 - 30 = -10 | 8 $\times$ -10 = -80 |
| 30 | 12 | 30 - 30 = 0 | 12 $\times$ 0 = 0 |
| 40 | 6 | 40 - 30 = 10 | 6 $\times$ 10 = 60 |
| 50 | 4 | 50 - 30 = 20 | 4 $\times$ 20 = 80 |
| **Total** | **$N = \sum f = 35$** | | **$\sum fd = -40$** |

*(Check $\sum fd$: (-100) + (-80) + 0 + 60 + 80 = -180 + 140 = -40)*

**Calculation:**
$$\bar{X} = A + \frac{\sum fd}{N}$$
$$\bar{X} = 30 + \frac{-40}{35}$$
$$\bar{X} = 30 - 1.143$$
$$\bar{X} = 28.857$$

**Answer:** The mean marks are 28.857 (the same as the Direct Method).

---

### Method 3: Step Deviation Method (for Discrete Series)

This method is ideal for this example because all the deviations ($d$) from the Shortcut Method (-20, -10, 0, 10, 20) are divisible by a common factor, which is 10.

**Formula:**
$$\bar{X} = A + \left( \frac{\sum fd'}{N} \right) \times i$$
Where $d' = \frac{X - A}{i}$

**Steps:**
1.  Choose an Assumed Mean ($A$). (Let's use $A = 30$).
2.  Choose a common factor ($i$). (Here, $i = 10$).
3.  Calculate the step deviations ($d' = \frac{d}{i} = \frac{X - A}{10}$).
4.  Multiply each frequency ($f$) by its corresponding step deviation ($d'$) to get the $fd'$ column.
5.  Find the sums $\sum fd'$ and $N = \sum f$.
6.  Apply the formula.

**Solution Table:**
(Using $A = 30$ and $i = 10$)

| Marks ($X$) | No. of Students ($f$) | Deviation ($d = X - A$) | Step Deviation ($d' = \frac{d}{10}$) | $fd'$ ($f \times d'$) |
| :--- | :--- | :--- | :--- | :--- |
| 10 | 5 | -20 | -2 | 5 $\times$ -2 = -10 |
| 20 | 8 | -10 | -1 | 8 $\times$ -1 = -8 |
| 30 | 12 | 0 | 0 | 12 $\times$ 0 = 0 |
| 40 | 6 | 10 | 1 | 6 $\times$ 1 = 6 |
| 50 | 4 | 20 | 2 | 4 $\times$ 2 = 8 |
| **Total** | **$N = \sum f = 35$** | | | **$\sum fd' = -4$** |

*(Check $\sum fd'$: (-10) + (-8) + 0 + 6 + 8 = -18 + 14 = -4)*

**Calculation:**
$$\bar{X} = A + \left( \frac{\sum fd'}{N} \right) \times i$$
$$\bar{X} = 30 + \left( \frac{-4}{35} \right) \times 10$$
$$\bar{X} = 30 + \left( \frac{-40}{35} \right)$$
$$\bar{X} = 30 - 1.143$$
$$\bar{X} = 28.857$$

**Answer:** The mean marks are 28.857. All three methods give the exact same result. The Step Deviation Method was the easiest, as it involved multiplying very small numbers.

---
---

### Continuous Series

A **Continuous Series** (or frequency distribution) is a dataset grouped into continuous class intervals (e.g., 0-10, 10-20).

**Key Step:** We cannot perform calculations with intervals. We must first convert the intervals into single values by finding their **Mid-point ($m$)**. Once we have the mid-point, we treat it *exactly* like '$X$' in a discrete series.

**Mid-point ($m$) = $\frac{\text{Lower Class Limit} + \text{Upper Class Limit}}{2}$**

For example, the mid-point of the class 0-10 is $\frac{0 + 10}{2} = 5$.

**Example:** Find the arithmetic mean of the following data:

| Marks (Class) | 0-10 | 10-20 | 20-30 | 30-40 | 40-50 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| No. of Students ($f$) | 5 | 12 | 15 | 10 | 8 |

---

### Method 1: Direct Method (for Continuous Series)

**Formula:**
$$\bar{X} = \frac{\sum fm}{N}$$

**Steps:**
1.  Find the mid-point ($m$) for each class interval.
2.  Multiply each mid-point ($m$) by its corresponding frequency ($f$) to get the $fm$ column.
3.  Find the total sum of the $fm$ column ($\sum fm$) and the $f$ column ($N$).
4.  Divide $\sum fm$ by $N$.

**Solution Table:**

| Marks (Class) | No. of Students ($f$) | Mid-point ($m$) | $fm$ ($f \times m$) |
| :--- | :--- | :--- | :--- |
| 0-10 | 5 | 5 | 5 $\times$ 5 = 25 |
| 10-20 | 12 | 15 | 12 $\times$ 15 = 180 |
| 20-30 | 15 | 25 | 15 $\times$ 25 = 375 |
| 30-40 | 10 | 35 | 10 $\times$ 35 = 350 |
| 40-50 | 8 | 45 | 8 $\times$ 45 = 360 |
| **Total** | **$N = \sum f = 50$** | | **$\sum fm = 1290$** |

**Calculation:**
$$\bar{X} = \frac{\sum fm}{N} = \frac{1290}{50}$$
$$\bar{X} = 25.8$$

**Answer:** The mean marks are 25.8.

---

### Method 2: Shortcut Method (for Continuous Series)

**Formula:**
$$\bar{X} = A + \frac{\sum fd}{N}$$
Where $A$ is an Assumed Mean (from the mid-points) and $d = m - A$.

**Steps:**
1.  Find the mid-points ($m$).
2.  Choose an Assumed Mean ($A$) from the mid-point column. (Let's choose $A = 25$).
3.  Calculate the deviations ($d = m - A$) for each mid-point.
4.  Multiply each frequency ($f$) by its deviation ($d$) to get the $fd$ column.
5.  Find the sums $\sum fd$ and $N$.
6.  Apply the formula.

**Solution Table:**

(Using $A = 25$)

| Marks (Class) | No. of Students ($f$) | Mid-point ($m$) | Deviation ($d = m - A$) | $fd$ ($f \times d$) |
| :--- | :--- | :--- | :--- | :--- |
| 0-10 | 5 | 5 | 5 - 25 = -20 | 5 $\times$ -20 = -100 |
| 10-20 | 12 | 15 | 15 - 25 = -10 | 12 $\times$ -10 = -120 |
| 20-30 | 15 | 25 | 25 - 25 = 0 | 15 $\times$ 0 = 0 |
| 30-40 | 10 | 35 | 35 - 25 = 10 | 10 $\times$ 10 = 100 |
| 40-50 | 8 | 45 | 45 - 25 = 20 | 8 $\times$ 20 = 160 |
| **Total** | **$N = \sum f = 50$** | | | **$\sum fd = 40$** |

*(Check $\sum fd$: (-100) + (-120) + 0 + 100 + 160 = -220 + 260 = 40)*

**Calculation:**
$$\bar{X} = A + \frac{\sum fd}{N}$$
$$\bar{X} = 25 + \frac{40}{50}$$
$$\bar{X} = 25 + 0.8$$
$$\bar{X} = 25.8$$

**Answer:** The mean marks are 25.8. (The same as the Direct Method).

---

### Method 3: Step Deviation Method (for Continuous Series)

This is the most common and easiest method for continuous series, as the class interval ($i$) is always the common factor.

**Formula:**
$$\bar{X} = A + \left( \frac{\sum fd'}{N} \right) \times i$$
Where $d' = \frac{m - A}{i}$ and $i$ = class interval (in this case, 10).

**Steps:**
1.  Find mid-points ($m$).
2.  Choose $A$ (Let's use $A = 25$).
3.  The common factor $i$ is the class width (10-0 = 10; 20-10 = 10). So, $i = 10$.
4.  Calculate step deviations ($d' = \frac{m - A}{10}$).
5.  Multiply $f$ by $d'$ to get the $fd'$ column.
6.  Find the sums $\sum fd'$ and $N$.
7.  Apply the formula.

**Solution Table:**

(Using $A = 25$ and $i = 10$)

| Marks (Class) | No. of Students ($f$) | Mid-point ($m$) | Deviation ($d = m - A$) | Step Deviation ($d' = \frac{d}{10}$) | $fd'$ ($f \times d'$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0-10 | 5 | 5 | -20 | -2 | 5 $\times$ -2 = -10 |
| 10-20 | 12 | 15 | -10 | -1 | 12 $\times$ -1 = -12 |
| 20-30 | 15 | 25 | 0 | 0 | 15 $\times$ 0 = 0 |
| 30-40 | 10 | 35 | 10 | 1 | 10 $\times$ 1 = 10 |
| 40-50 | 8 | 45 | 20 | 2 | 8 $\times$ 2 = 16 |
| **Total** | **$N = \sum f = 50$** | | | | **$\sum fd' = 4$** |

*(Check $\sum fd'$: (-10) + (-12) + 0 + 10 + 16 = -22 + 26 = 4)*

**Calculation:**
$$\bar{X} = A + \left( \frac{\sum fd'}{N} \right) \times i$$
$$\bar{X} = 25 + \left( \frac{4}{50} \right) \times 10$$
$$\bar{X} = 25 + \frac{40}{50}$$
$$\bar{X} = 25 + 0.8$$
$$\bar{X} = 25.8$$

**Answer:** The mean marks are 25.8. All three methods produce the same result, but the calculations in the final column ($fd'$) were the simplest.