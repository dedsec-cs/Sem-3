# Arithmetic Mean

### Definition

The **arithmetic mean**, also known as the **average**, is the most common measure of central tendency. It's calculated by summing all the values in a dataset and then dividing that sum by the number of values in the dataset. It provides a single value that represents the central point of the data.

#### In Case of Frequency Distribution

When data is presented in a **frequency distribution**, it means you have a list of values and the number of times each value appears. The formula for the arithmetic mean changes slightly to account for this. Instead of adding up each individual value, you multiply each value by its frequency, sum these products, and then divide by the total number of values (which is the sum of the frequencies).

The formula for the arithmetic mean ($\bar{x}$) is:

$$\bar{x} = \frac{\sum (x_i \cdot f_i)}{\sum f_i}$$

Where:
* $\bar{x}$ = Arithmetic Mean
* $x_i$ = The $i$-th value or midpoint of the class
* $f_i$ = The frequency of the $i$-th value
* $\sum$ = The Greek letter **sigma**, which means "sum of"

---

### All Question Cases Covered With Example

Let's break down how to calculate the arithmetic mean for different types of data presentation.

#### 1. Individual Series (Raw Data)

This is the simplest case, where you have a list of individual data points.

**Example:** A student's scores on 5 tests are 85, 90, 78, 92, and 88. Calculate the mean score.

**Formula:**
$\bar{x} = \frac{\sum x}{n}$

Where:
* $\sum x$ = Sum of all values
* $n$ = Number of values

**Calculation:**
$\bar{x} = \frac{85 + 90 + 78 + 92 + 88}{5} = \frac{433}{5} = 86.6$

The average test score is **86.6**.

---

#### 2. Discrete Series (Frequency Distribution)

In a discrete series, the data has a clear value and a corresponding frequency.

**Example:** The number of cars sold per day at a dealership over 20 days is given below. Calculate the mean number of cars sold per day.

| Number of Cars ($x_i$) | Number of Days (Frequency, $f_i$) |
| :--- | :--- |
| 0 | 2 |
| 1 | 5 |
| 2 | 8 |
| 3 | 3 |
| 4 | 2 |
| **Total** | **$\sum f_i = 20$** |

**Calculation:**
To solve this, we need to create a new column, $f_i \cdot x_i$.

| Number of Cars ($x_i$) | Number of Days (Frequency, $f_i$) | $f_i \cdot x_i$ |
| :--- | :--- | :--- |
| 0 | 2 | $0 \times 2 = 0$ |
| 1 | 5 | $1 \times 5 = 5$ |
| 2 | 8 | $2 \times 8 = 16$ |
| 3 | 3 | $3 \times 3 = 9$ |
| 4 | 2 | $4 \times 2 = 8$ |
| **Total** | **$\sum f_i = 20$** | **$\sum(f_i \cdot x_i) = 38$** |

**Formula:**
$\bar{x} = \frac{\sum (x_i \cdot f_i)}{\sum f_i}$

**Calculation:**
$\bar{x} = \frac{38}{20} = 1.9$

The mean number of cars sold per day is **1.9**.

---

#### 3. Continuous Series (Grouped Frequency Distribution)

In a continuous series, the data is grouped into classes or ranges. To calculate the mean, you must first find the **midpoint** of each class. The midpoint serves as the value ($x_i$) for that class.

**Example:** Calculate the mean height from the following data.

| Height (cm) | Number of Students (Frequency, $f_i$) |
| :--- | :--- |
| 150-155 | 6 |
| 155-160 | 10 |
| 160-165 | 15 |
| 165-170 | 8 |
| 170-175 | 4 |
| **Total** | **$\sum f_i = 43$** |

**Calculation:**
First, find the midpoint ($x_i$) for each class by adding the lower and upper limits and dividing by 2.

* Midpoint of 150-155 = $(150 + 155) / 2 = 152.5$
* Midpoint of 155-160 = $(155 + 160) / 2 = 157.5$
* ...and so on.

Now, create a new table with the midpoints and a column for $f_i \cdot x_i$.

| Height (cm) | Midpoint ($x_i$) | Frequency ($f_i$)   | $f_i \cdot x_i$                    |
| :---------- | :--------------- | :------------------ | :--------------------------------- |
| 150-155     | 152.5            | 6                   | $152.5 \times 6 = 915$             |
| 155-160     | 157.5            | 10                  | $157.5 \times 10 = 1575$           |
| 160-165     | 162.5            | 15                  | $162.5 \times 15 = 2437.5$         |
| 165-170     | 167.5            | 8                   | $167.5 \times 8 = 1340$            |
| 170-175     | 172.5            | 4                   | $172.5 \times 4 = 690$             |
| **Total**   |                  | **$\sum f_i = 43$** | **$\sum(f_i \cdot x_i) = 6957.5$** |


**Formula:**
$\bar{x} = \frac{\sum (x_i \cdot f_i)}{\sum f_i}$

**Calculation:**
$\bar{x} = \frac{6957.5}{43} \approx 161.79$

The mean height of the students is approximately **161.79 cm**.

---

### Key Properties of Arithmetic Mean

* **Uniqueness:** For any given dataset, there is only one unique arithmetic mean.
* **Sensitivity to Outliers:** The mean is heavily influenced by **outliers**, which are extremely high or low values. A single outlier can significantly skew the mean. 
* **Sum of Deviations is Zero:** The sum of the deviations of each data point from the mean is always zero. This is a fundamental property. $\sum(x_i - \bar{x}) = 0$
* **Algebraic Treatment:** The mean can be used in further algebraic calculations, which is a key advantage over other measures like the median or mode.

## Solved Examples: Mean

Yes, let's work through six examples that comprehensively cover the different scenarios for calculating the arithmetic mean.

***

### Example 1: Individual Series (Simple Average)
**Problem:** A bowler's scores in five different matches are 15, 20, 25, 30, and 35. What is the mean score?

**Solution:**
For an individual series, you simply sum all the values and divide by the total number of values.
**Formula:** $\bar{x} = \frac{\sum x}{n}$
* **Sum of scores ($\sum x$):** $15 + 20 + 25 + 30 + 35 = 125$
* **Number of matches ($n$):** 5
* **Mean ($\bar{x}$):** $\frac{125}{5} = 25$

The mean score is **25**.

***

### Example 2: Discrete Series (Frequency Distribution)
**Problem:** The number of hours a group of students spends studying each week is shown in the table below. Calculate the mean number of study hours.

| Hours Studied ($x_i$) | Number of Students ($f_i$) |
| :--- | :--- |
| 2 | 3 |
| 4 | 5 |
| 6 | 7 |
| 8 | 2 |
| 10 | 1 |

**Solution:**
When you have a frequency distribution, you multiply each value by its frequency, sum those products, and then divide by the total frequency.
**Formula:** $\bar{x} = \frac{\sum (x_i \cdot f_i)}{\sum f_i}$

**Step-by-step Calculation:**
1.  **Create a new column for $x_i \cdot f_i$:**

| Hours Studied ($x_i$) | Number of Students ($f_i$) | $x_i \cdot f_i$ |
| :--- | :--- | :--- |
| 2 | 3 | $2 \times 3 = 6$ |
| 4 | 5 | $4 \times 5 = 20$ |
| 6 | 7 | $6 \times 7 = 42$ |
| 8 | 2 | $8 \times 2 = 16$ |
| 10 | 1 | $10 \times 1 = 10$ |
| **Total** | **$\sum f_i = 18$** | **$\sum(x_i \cdot f_i) = 94$** |

2.  **Calculate the mean:** $\bar{x} = \frac{94}{18} \approx 5.22$

The mean number of study hours is approximately **5.22**.

***

### Example 3: Continuous Series (Grouped Frequency Distribution)
**Problem:** Find the mean weight of students from the data below.

| Weight (kg) | Number of Students ($f_i$) |
| :--- | :--- |
| 40-50 | 5 |
| 50-60 | 10 |
| 60-70 | 15 |
| 70-80 | 8 |
| 80-90 | 2 |

**Solution:**
For grouped data, we use the midpoint of each class as the representative value.
**Formula:** $\bar{x} = \frac{\sum (x_i \cdot f_i)}{\sum f_i}$

**Step-by-step Calculation:**
1.  **Find the midpoint ($x_i$) of each class:**
    * $40-50 \implies \frac{40+50}{2} = 45$
    * $50-60 \implies \frac{50+60}{2} = 55$
    * ...and so on.

2.  **Create a new table with midpoints and $x_i \cdot f_i$:**

| Weight (kg) | Midpoint ($x_i$) | Frequency ($f_i$) | $x_i \cdot f_i$ |
| :--- | :--- | :--- | :--- |
| 40-50 | 45 | 5 | $45 \times 5 = 225$ |
| 50-60 | 55 | 10 | $55 \times 10 = 550$ |
| 60-70 | 65 | 15 | $65 \times 15 = 975$ |
| 70-80 | 75 | 8 | $75 \times 8 = 600$ |
| 80-90 | 85 | 2 | $85 \times 2 = 170$ |
| **Total** | | **$\sum f_i = 40$** | **$\sum(x_i \cdot f_i) = 2520$** |

3.  **Calculate the mean:** $\bar{x} = \frac{2520}{40} = 63$

The mean weight is **63 kg**.

***

### Example 4: Finding a Missing Value
**Problem:** The mean of the numbers 10, 15, $x$, 25, and 30 is 21. Find the value of $x$.

**Solution:**
We can use the basic formula for the mean and work backward.
**Formula:** $\bar{x} = \frac{\sum x}{n}$
* **Mean ($\bar{x}$):** 21
* **Number of values ($n$):** 5
* **Sum of values ($\sum x$):** $10 + 15 + x + 25 + 30 = 80 + x$

**Calculation:**
$21 = \frac{80 + x}{5}$
$21 \times 5 = 80 + x$
$105 = 80 + x$
$x = 105 - 80 = 25$

The missing value, $x$, is **25**.

***

### Example 5: Combined Mean
**Problem:** Class A has 25 students with a mean score of 68. Class B has 30 students with a mean score of 72. What is the combined mean score of both classes?

**Solution:**
To find the combined mean, you need the total sum of all scores and the total number of students.
**Formula:** Combined Mean = $\frac{\sum(\text{Class A scores}) + \sum(\text{Class B scores})}{\text{Total students}}$

**Step-by-step Calculation:**
1.  **Find the total sum of scores for each class:**
    * **Class A:** $\text{Sum} = \text{Mean} \times \text{Number of students} = 68 \times 25 = 1700$
    * **Class B:** $\text{Sum} = \text{Mean} \times \text{Number of students} = 72 \times 30 = 2160$
2.  **Find the total sum and total number of students:**
    * **Total Sum:** $1700 + 2160 = 3860$
    * **Total Students:** $25 + 30 = 55$
3.  **Calculate the combined mean:**
    * $\text{Combined Mean} = \frac{3860}{55} \approx 70.18$

The combined mean score for both classes is approximately **70.18**.

***

### Example 6: Effect of Adding/Subtracting a Constant
**Problem:** The mean of a set of 10 numbers is 50. If each number in the set is decreased by 5, what is the new mean?

**Solution:**
A key property of the arithmetic mean is that if every value in a dataset is **increased or decreased by a constant**, the mean will also **increase or decrease by the same constant**.

**Calculation:**
* **Original Mean:** 50
* **Constant Decrease:** 5
* **New Mean:** $50 - 5 = 45$

The new mean is **45**. This holds true without having to calculate the individual numbers or their new sum.

# Median

The **median** is the middle value in a dataset when the data is arranged in ascending or descending order. Unlike the mean, the median is not affected by extreme values (outliers), making it a useful measure of central tendency for skewed data.

-----

### Ungrouped Data

For a simple list of numbers, also known as **raw data**, the method to find the median depends on whether the total number of observations is odd or even. The first and most critical step is always to **arrange the data in ascending (or descending) order**.

| Number of Observations ($n$) | Formula                                                                              | Example                                                                                                                                                                                                                                                                                                                                                                           |
| :--------------------------- | :----------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Odd**                      | Median = Value of the $(\frac{n+1}{2})^{th}$ observation                             | **Problem:** Find the median of: 10, 5, 20, 15, 25.  <br>**Solution:**<br>1. Arrange the data: 5, 10, **15**, 20, 25.<br>2. Total observations ($n$) = 5. Since $n$ is odd, the median is the $(\frac{5+1}{2})^{th}$ = $3^{rd}$ observation.<br>3. The $3^{rd}$ value is **15**.                                                                                                  |
| **Even**                     | Median = Average of the $(\frac{n}{2})^{th}$ and $(\frac{n}{2}+1)^{th}$ observations | **Problem:** Find the median of: 12, 8, 16, 20. <br><br> **Solution:**<br>1. Arrange the data: 8, **12, 16**, 20.<br>2. Total observations ($n$) = 4. Since $n$ is even, the median is the average of the $(\frac{4}{2})^{th}$ and $(\frac{4}{2}+1)^{th}$ observations, which are the $2^{nd}$ and $3^{rd}$ observations.<br>3. Median = $\frac{12 + 16}{2} = \frac{28}{2} = 14$. |

-----

### Discrete Frequency Distribution

A discrete frequency distribution lists specific values and how often each value occurs. To find the median, you need to calculate the **cumulative frequency (cf)**. The cumulative frequency for a value is the sum of its frequency and the frequencies of all preceding values.

**Steps:**

1.  Add a **Cumulative Frequency (cf)** column to the table.
2.  Find the total number of observations ($N$) by summing all frequencies ($\sum f$).
3.  The median is the value that corresponds to the first cumulative frequency that is greater than or equal to $N/2$.

| Hours Studied ($x_i$) | Frequency ($f_i$) | Cumulative Frequency (cf) |
| :-------------------- | :---------------- | :------------------------ |
| 2                     | 3                 | 3                         |
| 4                     | 5                 | $3+5=8$                   |
| 6                     | 7                 | $8+7=15$                  |
| 8                     | 2                 | $15+2=17$                 |
| 10                    | 1                 | $17+1=18$                 |

**Problem:** Find the median of the data in the table above.

**Solution:**

1.  **Total Frequency ($N$)**: $3 + 5 + 7 + 2 + 1 = 18$.
2.  **Median Position**: $N/2 = 18/2 = 9$.
3.  **Locate Median**: We look for the first cumulative frequency that is greater than or equal to 9. The cf of 15 is the first one to be greater than 9.
4.  **Identify Median Value**: The value ($x_i$) corresponding to the cf of 15 is 6.

The median is **6** hours.

-----

### Continuous Frequency Distribution

For a continuous series, data is grouped into class intervals. You cannot find the exact median value, but you can estimate it using a specific formula. This requires identifying the **median class** and then applying a formula that interpolates the median's position within that class.

**Steps:**

1.  Create a **Cumulative Frequency (cf)** column.

2.  Find the total frequency ($N = \sum f$).

3.  Determine the **median class**, which is the first class interval whose cumulative frequency is greater than or equal to $N/2$.

4.  Apply the following formula:
    **Median** $= L + (\frac{\frac{N}{2} - cf}{f}) \times h$

    Where:

      * **$L$** = Lower boundary of the median class.
      * **$N$** = Total frequency.
      * **$cf$** = Cumulative frequency of the class **preceding** the median class.
      * **$f$** = Frequency of the median class.
      * **$h$** = Class size (upper limit - lower limit) of the median class.

| Weight (kg) | Frequency ($f_i$) | Cumulative Frequency (cf) |
| :---------- | :----------------- | :------------------------ |
| 40-50       | 5                  | 5                         |
| 50-60       | 10                 | 15                        |
| **60-70**   | **15**             | **30**                    |
| 70-80       | 8                  | 38                        |
| 80-90       | 2                  | 40                        |

**Problem:** Find the median of the data in the table above.

**Solution:**

1.  **Total Frequency ($N$)**: $\sum f = 40$.
2.  **Median Position**: $N/2 = 40/2 = 20$.
3.  **Identify Median Class**: The first cumulative frequency greater than or equal to 20 is 30, which corresponds to the class **60-70**.
4.  **Extract Formula Values**:
      * $L = 60$ (lower limit of the median class)
      * $N/2 = 20$
      * $cf = 15$ (cf of the class before the median class)
      * $f = 15$ (frequency of the median class)
      * $h = 70 - 60 = 10$ (class size)
5.  **Apply Formula**:
    Median $= 60 + (\frac{20 - 15}{15}) \times 10$
    Median $= 60 + (\frac{5}{15}) \times 10$
    Median $= 60 + 0.333 \times 10$
    Median $= 60 + 3.333 = 63.333$

The median is approximately **63.33 kg**.


---
## Solved Examples: Median

### Example 1: Ungrouped Data (Odd Number of Observations)
**Problem:** Find the median of the following set of data representing the number of goals scored by a soccer team in 7 matches: 2, 0, 5, 1, 3, 4, 1.

**Solution:**
**Step 1:** Arrange the data in ascending order.
0, 1, 1, **2**, 3, 4, 5
**Step 2:** Identify the number of observations ($n$).
$n = 7$ (which is an odd number).
**Step 3:** Use the formula for an odd number of observations: Value of the $(\frac{n+1}{2})^{th}$ observation.
Median = Value of the $(\frac{7+1}{2})^{th}$ observation = Value of the $4^{th}$ observation.
**Step 4:** Find the $4^{th}$ value in the ordered list.
The $4^{th}$ value is **2**.

The median is **2**.

---

### Example 2: Ungrouped Data (Even Number of Observations)
**Problem:** Find the median of the following numbers representing the ages of 6 students in a club: 18, 17, 20, 19, 21, 16.

**Solution:**
**Step 1:** Arrange the data in ascending order.
16, 17, **18, 19**, 20, 21
**Step 2:** Identify the number of observations ($n$).
$n = 6$ (which is an even number).
**Step 3:** Use the formula for an even number of observations: Average of the $(\frac{n}{2})^{th}$ and $(\frac{n}{2}+1)^{th}$ observations.
Median = Average of the $(\frac{6}{2})^{th}$ and $(\frac{6}{2}+1)^{th}$ observations = Average of the $3^{rd}$ and $4^{th}$ observations.
**Step 4:** Find the average of the $3^{rd}$ and $4^{th}$ values in the ordered list.
Median = $\frac{18 + 19}{2} = \frac{37}{2} = 18.5$

The median is **18.5**.

---

### Example 3: Discrete Frequency Distribution
**Problem:** Find the median number of siblings from the data below.

| Number of Siblings ($x_i$) | Number of Families ($f_i$) |
| :--- | :--- |
| 0 | 5 |
| 1 | 8 |
| 2 | 12 |
| 3 | 7 |
| 4 | 3 |

**Solution:**
**Step 1:** Create a cumulative frequency (cf) column.

| Number of Siblings ($x_i$) | Number of Families ($f_i$) | Cumulative Frequency (cf) |
| :--- | :--- | :--- |
| 0 | 5 | 5 |
| 1 | 8 | $5+8=13$ |
| 2 | 12 | $13+12=25$ |
| 3 | 7 | $25+7=32$ |
| 4 | 3 | $32+3=35$ |

**Step 2:** Find the total number of observations ($N$).
$N = \sum f_i = 35$
**Step 3:** Find the median position ($N/2$).
$N/2 = 35/2 = 17.5$
**Step 4:** Locate the first cumulative frequency that is greater than or equal to the median position.
The first cf that is $\ge 17.5$ is 25.
**Step 5:** Identify the corresponding value.
The value ($x_i$) corresponding to the cf of 25 is **2**.

The median is **2** siblings.

---

### Example 4: Continuous Frequency Distribution
**Problem:** The table below shows the marks of 50 students in a test. Find the median mark.

| Marks | Number of Students ($f_i$) |
| :--- | :--- |
| 0-10 | 4 |
| 10-20 | 8 |
| 20-30 | 12 |
| 30-40 | 15 |
| 40-50 | 7 |
| 50-60 | 4 |

**Solution:**
**Step 1:** Create a cumulative frequency (cf) column.

| Marks | Number of Students ($f_i$) | Cumulative Frequency (cf) |
| :--- | :--- | :--- |
| 0-10 | 4 | 4 |
| 10-20 | 8 | 12 |
| 20-30 | 12 | 24 |
| **30-40** | **15** | **39** |
| 40-50 | 7 | 46 |
| 50-60 | 4 | 50 |

**Step 2:** Find the total number of observations ($N$).
$N = \sum f_i = 50$
**Step 3:** Find the median position ($N/2$).
$N/2 = 50/2 = 25$
**Step 4:** Identify the median class.
The first cf that is $\ge 25$ is 39, so the median class is **30-40**.
**Step 5:** Extract the values for the formula.
* **L** (lower boundary of median class) = 30
* **N/2** = 25
* **cf** (cf of the class before median class) = 24
* **f** (frequency of median class) = 15
* **h** (class size) = $40 - 30 = 10$
**Step 6:** Apply the formula: **Median** $= L + (\frac{\frac{N}{2} - cf}{f}) \times h$
Median $= 30 + (\frac{25 - 24}{15}) \times 10$
Median $= 30 + (\frac{1}{15}) \times 10$
Median $= 30 + 0.067 \times 10 = 30 + 0.67 = 30.67$

The median mark is **30.67**.

---

### Example 5: Finding a Missing Frequency
**Problem:** The median of the following data is 40. Find the missing frequency ($x$).

| Class Interval | Frequency |
| :--- | :--- |
| 10-20 | 6 |
| 20-30 | 8 |
| 30-40 | $x$ |
| 40-50 | 12 |
| 50-60 | 4 |

**Solution:**
**Step 1:** Create a cumulative frequency (cf) column.

| Class Interval | Frequency ($f_i$) | Cumulative Frequency (cf) |
| :--- | :--- | :--- |
| 10-20 | 6 | 6 |
| 20-30 | 8 | 14 |
| **30-40** | **$x$** | **$14+x$** |
| 40-50 | 12 | $14+x+12 = 26+x$ |
| 50-60 | 4 | $26+x+4 = 30+x$ |

**Step 2:** Identify the median class and total frequency.
Since the median is given as 40, the median class must be **30-40**.
Total frequency ($N$) = $30 + x$.
**Step 3:** Extract the values from the table.
* **Median** = 40
* **L** (lower boundary of median class) = 30
* **N** = $30+x$
* **cf** (cf of the class before median class) = 14
* **f** (frequency of median class) = $x$
* **h** (class size) = $40 - 30 = 10$
**Step 4:** Apply the formula and solve for $x$.
**Median** $= L + (\frac{\frac{N}{2} - cf}{f}) \times h$
$40 = 30 + (\frac{\frac{30+x}{2} - 14}{x}) \times 10$
$40 - 30 = (\frac{15+0.5x - 14}{x}) \times 10$
$10 = (\frac{1+0.5x}{x}) \times 10$
$10/10 = \frac{1+0.5x}{x}$
$1 = \frac{1+0.5x}{x}$
$x = 1 + 0.5x$
$x - 0.5x = 1$
$0.5x = 1$
$x = 1 / 0.5 = 2$

The missing frequency is **2**.

# Mode

### Mode

The **mode** is the value that appears most frequently in a dataset. A dataset can have one mode (unimodal), more than one mode (bimodal or multimodal), or no mode at all if every value appears with the same frequency. The mode is useful for categorical data where you cannot calculate a mean or median.

***

### Calculation of Mode

#### In Case of Discrete Distribution

For a discrete frequency distribution, finding the mode is straightforward. You simply need to identify the value that has the highest frequency.

**Problem:** Find the mode of the following data, which shows the number of cars sold per day at a dealership over a month.

| Number of Cars | Number of Days (Frequency) |
| :--- | :--- |
| 0 | 5 |
| 1 | 8 |
| **2** | **12** |
| 3 | 6 |
| 4 | 3 |

**Solution:**
Look at the "Number of Days" (frequency) column and find the largest number. The highest frequency is **12**. The value corresponding to this frequency is **2**.

The mode is **2** cars, as it was the most frequent number of cars sold per day.

---

#### In Case of Continuous Frequency Distribution

For continuous frequency distributions (grouped data), you cannot find a single mode value because the data is in ranges. Instead, you find the **modal class** and then use a formula to estimate the mode within that class. The modal class is the class with the highest frequency.

The formula for the mode is:
**Mode** $= L + (\frac{f_m - f_1}{2f_m - f_1 - f_2}) \times h$

Where:
* **$L$** = Lower boundary of the modal class.
* **$f_m$** = Frequency of the modal class.
* **$f_1$** = Frequency of the class **preceding** the modal class.
* **$f_2$** = Frequency of the class **succeeding** the modal class.
* **$h$** = Class size (upper limit - lower limit) of the modal class.

**Problem:** Find the mode of the following data on the height of students.

| Height (cm) | Number of Students (Frequency) |
| :--- | :--- |
| 150-155 | 6 |
| **155-160** | **15** |
| 160-165 | 10 |
| 165-170 | 8 |

**Solution:**
**Step 1:** Identify the modal class.
The highest frequency is 15, which corresponds to the class **155-160**. This is our modal class.

**Step 2:** Extract the values for the formula.
* $L = 155$
* $f_m = 15$
* $f_1 = 6$
* $f_2 = 10$
* $h = 160 - 155 = 5$

**Step 3:** Apply the formula.
Mode $= 155 + (\frac{15 - 6}{2(15) - 6 - 10}) \times 5$
Mode $= 155 + (\frac{9}{30 - 16}) \times 5$
Mode $= 155 + (\frac{9}{14}) \times 5$
Mode $= 155 + (0.643) \times 5$
Mode $= 155 + 3.215 = 158.215$

The mode is approximately **158.22 cm**.

---

### For a symmetrical distribution, mean, median and mode coincide

A **symmetrical distribution** is a dataset where the values are evenly distributed around the center. A classic example is a normal distribution, also known as a bell curve.

In a perfectly symmetrical distribution, the measures of central tendency are all equal:
**Mean = Median = Mode**

This happens because the center is the arithmetic average, the exact middle value, and the most frequent value, all at the same point.

In a skewed distribution, where the data is not symmetrical, the mean, median, and mode will be different. The mean is pulled in the direction of the long tail (outliers), while the median remains a robust measure of the center.
* **Skewed to the right (positive skew):** Mean > Median > Mode
* **Skewed to the left (negative skew):** Mean < Median < Mode

The **empirical mode** is an alternative way to estimate the mode for a grouped (continuous) frequency distribution. It is particularly useful when the modal class is difficult to determine, such as when a distribution has multiple peaks or is highly skewed. The empirical mode is calculated using the relationship between the mean, median, and mode for a moderately skewed distribution. This relationship is often expressed as:

**Mode ≈ 3 × Median − 2 × Mean**

This formula, also known as **Karl Pearson's empirical formula**, provides a good approximation of the mode when the distribution is not perfectly symmetrical.

***

### When to Use the Empirical Mode

You should use the empirical mode in situations where:

* The data is a **continuous frequency distribution**.
* The **modal class cannot be clearly identified** because the highest frequency appears more than once, or the distribution is highly irregular.
* The mean and median are already calculated or are easy to calculate.

**Example:**
Suppose a dataset has a **Mean** of 45 and a **Median** of 48.

**Solution:**
Using the empirical formula:
Empirical Mode ≈ (3 × Median) − (2 × Mean)
Empirical Mode ≈ (3 × 48) − (2 × 45)
Empirical Mode ≈ 144 − 90
Empirical Mode ≈ 54

The estimated mode is **54**.

---

### Comparison: Normal Formula vs. Empirical Formula

| Feature | Direct Calculation (Normal Formula) | Empirical Formula (Mean, Median) |
| :--- | :--- | :--- |
| **Data Type** | Grouped (Continuous) Frequency Distribution | Any dataset where mean and median are available |
| **Basis** | Frequency of the modal class and adjacent classes | Relationship between Mean, Median, and Mode in a moderately skewed distribution |
| **Accuracy** | Generally more accurate for a clear, single-peaked distribution | A good approximation, especially for irregular distributions. It is an estimation, not an exact calculation. |
| **Input Required** | Frequencies of the modal class and its neighbors | Calculated Mean and Median |
## Solved Examples: Mode

Yes, let's cover all the cases for calculating the mode with a variety of examples.

***

### Example 1: Ungrouped Data
**Problem:** Find the mode of the following set of numbers: 5, 8, 9, 8, 10, 8, 7.

**Solution:**
For ungrouped data, the mode is the number that appears most often.
1.  **Count the frequency of each number:**
    * 5: appears 1 time
    * 7: appears 1 time
    * 8: appears **3** times
    * 9: appears 1 time
    * 10: appears 1 time
2.  **Identify the number with the highest frequency.**
    The number **8** has the highest frequency (3).

The mode is **8**.

---

### Example 2: Discrete Frequency Distribution
**Problem:** Find the mode for the following data on the number of books read by students in a month.

| Number of Books | Number of Students (Frequency) |
| :--- | :--- |
| 1 | 5 |
| 2 | 10 |
| **3** | **15** |
| 4 | 8 |
| 5 | 2 |

**Solution:**
In a discrete frequency distribution, the mode is the value with the highest frequency.
1.  **Examine the Frequency column.**
    The highest frequency is **15**.
2.  **Find the corresponding value.**
    The value corresponding to the frequency of 15 is **3**.

The mode is **3** books.

---

### Example 3: Bimodal Data
**Problem:** Find the mode of the following dataset: 1, 2, 2, 3, 4, 4, 5, 6.

**Solution:**
A dataset can have more than one mode. This is called a **bimodal** or **multimodal** distribution.
1.  **Count the frequency of each number:**
    * 1: 1 time
    * 2: **2** times
    * 3: 1 time
    * 4: **2** times
    * 5: 1 time
    * 6: 1 time
2.  **Identify all values with the highest frequency.**
    The numbers **2** and **4** both have the highest frequency (2).

The modes are **2** and **4**.

---

### Example 4: No Mode
**Problem:** Find the mode of the following data: 10, 15, 20, 25, 30.

**Solution:**
A dataset has no mode if all values appear with the same frequency.
1.  **Count the frequency of each number.**
    Each number appears only 1 time.
2.  **Conclusion.**
    There is no value that appears more frequently than the others.

The dataset has **no mode**.

---

### Example 5: Continuous Frequency Distribution (Using the Formula)
**Problem:** Find the mode for the data below.

| Marks | Number of Students (Frequency) |
| :--- | :--- |
| 0-10 | 5 |
| 10-20 | 12 |
| **20-30** | **20** |
| 30-40 | 15 |
| 40-50 | 8 |

**Solution:**
For continuous data, you must use the mode formula.
**Step 1: Identify the modal class.**
The highest frequency is 20, so the modal class is **20-30**.
**Step 2: Extract the values for the formula.**
* $L$ (lower boundary of modal class) = 20
* $f_m$ (frequency of modal class) = 20
* $f_1$ (frequency of preceding class) = 12
* $f_2$ (frequency of succeeding class) = 15
* $h$ (class size) = $30 - 20 = 10$
**Step 3: Apply the formula.**
**Mode** $= L + (\frac{f_m - f_1}{2f_m - f_1 - f_2}) \times h$
Mode $= 20 + (\frac{20 - 12}{2(20) - 12 - 15}) \times 10$
Mode $= 20 + (\frac{8}{40 - 27}) \times 10$
Mode $= 20 + (\frac{8}{13}) \times 10$
Mode $= 20 + (0.615) \times 10 = 20 + 6.15 = 26.15$

The mode is **26.15** marks.