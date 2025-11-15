# Symmetrical Distribution

A distribution is **symmetrical** if the frequencies are evenly distributed on both sides of the central value (the mean). If you were to fold the graph of the distribution at its center, the two halves would match perfectly.

![[Pasted image 20251115163941.png]]

## Relation between Mean, Mode, and Median

In a perfectly symmetrical distribution, all three measures of central tendency are equal.
* The **Mode** is the highest point of the curve (the most frequent value).
* The **Median** is the middle value that divides the area of the curve into two equal halves.
* The **Mean** is the balancing point of the distribution.

Since the distribution is perfectly balanced, all three fall on the same point.

**Key Relation: Mean = Mode = Median**

> Because the mean and mode are equal, there is no pull or "skew" in either direction. This is why a symmetrical distribution is said to have **zero skewness**. ($\mu_3 = 0$ and $\beta_1 = 0$)

---

# Unsymmetrical Distribution (Skewness)

**Skewness** is the term for a "Lack Of Symmetry In A Frequency Distribution."

In a skewed distribution, the data is not evenly distributed. There is a cluster of values on one end and a long "tail" of less frequent values on the other. The mean, median, and mode are not equal.

## Positively Skewed Distribution (Tail On Right)

This occurs when the tail of the distribution is longer on the **right side** (the side of higher, positive values). Most of the data is clustered on the left side (lower values).


![[Pasted image 20251115164002.png]]


* **Why it happens:** A few very high values (outliers) pull the **Mean** to the right.
* The **Mode** remains at the highest peak (the most common value).
* The **Median** (the middle value) is pulled slightly by the tail but not as much as the mean.

**Key Relation: Mean > Median > Mode**

> **Skewness is positive** if the longer tail of the distribution lies toward the right.

---

## Negatively Skewed Distribution (Tail On Left)

This occurs when the tail of the distribution is longer on the **left side** (the side of lower, negative values). Most of the data is clustered on the right side (higher values).

![[Pasted image 20251115164050.png]]
* **Why it happens:** A few very low values (outliers) pull the **Mean** to the left.
* The **Mode** remains at the highest peak (the most common value).
* The **Median** is pulled slightly to the left.

**Key Relation: Mean < Median < Mode**

> **Skewness is negative** if the longer tail of the distribution lies toward the left.

---

# Karl Pearson's Coefficient Of Skewness

A "Measure Of Skewness" or "Coefficient Of Skewness" is a number that indicates the **degree** and **direction** of the skewness.

## Definition

Karl Pearson's coefficient of skewness ($Sk_p$) is a relative measure that quantifies the asymmetry of a distribution. It uses the difference between the Mean and the Mode (or Median) and standardizes this difference by dividing by the standard deviation.

## Formula

There are two main formulas for this coefficient:

**1. Based on Mean and Mode:**
This is the primary formula, used when the Mode is clearly defined and stable.

$$\text{Sk}_p = \frac{\text{Mean} - \text{Mode}}{\text{Standard Deviation}}$$

$$\text{Sk}_p = \frac{\bar{X} - Z}{\sigma}$$

**2. Based on Mean and Median (Empirical Formula):**
This formula is used when the Mode is ill-defined (e.g., in a bimodal or flat distribution) or for moderately skewed distributions. It relies on the empirical relationship: **Mode $\approx$ 3(Median) - 2(Mean)**.

$$\text{Sk}_p = \frac{3 (\text{Mean} - \text{Median})}{\text{Standard Deviation}}$$

$$\text{Sk}_p = \frac{3 (\bar{X} - M)}{\sigma}$$

## Karl Pearson's Coefficient Relation With Skewness

The value of $Sk_p$ tells you the direction and strength of the skew. For most distributions, this value lies between -1 and +1 (though in rare cases it can go as far as -3 or +3).

* **If $Sk_p = 0$:** The distribution is **symmetrical**. (Mean = Mode = Median)
* **If $Sk_p > 0$ (Positive):** The distribution is **positively skewed**. (Mean > Mode)
* **If $Sk_p < 0$ (Negative):** The distribution is **negatively skewed**. (Mean < Mode)

> **Example:** A coefficient of +0.8 would indicate a strong positive skew, while a coefficient of -0.2 would indicate a weak negative skew.


----

Here are 5 practice questions designed to help you master the formulas for Karl Pearson's Coefficient of Skewness and learn how to work with the data.

---

# Questions On Skewness And Karl Pearson's Coefficient

### Example 1: Direct Calculation (Mode Formula)

**Question:** In a data distribution, the Arithmetic Mean is 30, the Mode is 27, and the Standard Deviation is 6. Calculate the Karl Pearson's Coefficient of Skewness and interpret the result.

**Solution:**
We are given:
* Mean ($\bar{X}$) = 30
* Mode ($Z$) = 27
* Standard Deviation ($\sigma$) = 6

We will use the primary Karl Pearson's formula:
$$\text{Sk}_p = \frac{\bar{X} - Z}{\sigma}$$

**Calculation:**
1.  Plug in the values:
    $$\text{Sk}_p = \frac{30 - 27}{6}$$
2.  Solve the numerator:
    $$\text{Sk}_p = \frac{3}{6}$$
3.  Final calculation:
    $$\text{Sk}_p = 0.5$$

**Answer:** The Karl Pearson's Coefficient of Skewness is **+0.5**.
**Interpretation:** Since the coefficient is positive, the distribution is **positively skewed**.

---

### Example 2: Direct Calculation (Median Formula)

**Question:** A survey of worker salaries found that the mean salary is $54,000, the median salary is $52,000, and the standard deviation is $10,000. Calculate the coefficient of skewness.

**Solution:**
We are given:
* Mean ($\bar{X}$) = 54,000
* Median ($M$) = 52,000
* Standard Deviation ($\sigma$) = 10,000

Since the Mode is not given, we use the empirical formula (based on the median):
$$\text{Sk}_p = \frac{3 (\bar{X} - M)}{\sigma}$$

**Calculation:**
1.  Plug in the values:
    $$\text{Sk}_p = \frac{3 (54,000 - 52,000)}{10,000}$$
2.  Solve the parentheses first:
    $$\text{Sk}_p = \frac{3 (2,000)}{10,000}$$
3.  Solve the numerator:
    $$\text{Sk}_p = \frac{6,000}{10,000}$$
4.  Final calculation:
    $$\text{Sk}_p = 0.6$$

**Answer:** The Karl Pearson's Coefficient of Skewness is **+0.6**.
**Interpretation:** The positive value indicates a **positively skewed** distribution, with a few high-earning individuals pulling the mean higher than the median.

---

### Example 3: Finding a Missing Data Piece (Mode)

**Question:** A distribution has a mean of 100 and a standard deviation of 15. If the Karl Pearson's coefficient of skewness is **-0.4**, what is the value of the Mode?

**Solution:**
We are given:
* Mean ($\bar{X}$) = 100
* Standard Deviation ($\sigma$) = 15
* Skewness ($Sk_p$) = -0.4

We use the primary formula and rearrange it to solve for the Mode ($Z$).
$$\text{Sk}_p = \frac{\bar{X} - Z}{\sigma}$$

**Calculation:**
1.  Plug in the known values:
    $$-0.4 = \frac{100 - Z}{15}$$
2.  To solve for $Z$, first multiply both sides by 15:
    $$(-0.4) \times 15 = 100 - Z$$
    $$-6 = 100 - Z$$
3.  Rearrange the equation to isolate $Z$:
    $$Z = 100 + 6$$
    $$Z = 106$$

**Answer:** The value of the Mode is **106**.
**Interpretation:** This makes sense. For a negative skew (as shown by $Sk_p = -0.4$), we expect the Mean (100) to be less than the Mode (106).

---

### Example 4: Finding a Missing Data Piece (Standard Deviation)

**Question:** A dataset is moderately skewed. It has a Mean of 50 and a Median of 46. If the Karl Pearson's coefficient of skewness is **0.8**, what is the Standard Deviation of the data?

**Solution:**
We are given:
* Mean ($\bar{X}$) = 50
* Median ($M$) = 46
* Skewness ($Sk_p$) = 0.8

Since we have Mean and Median, we use the empirical formula and solve for Standard Deviation ($\sigma$).
$$\text{Sk}_p = \frac{3 (\bar{X} - M)}{\sigma}$$

**Calculation:**
1.  Plug in the known values:
    $$0.8 = \frac{3 (50 - 46)}{\sigma}$$
2.  Solve the numerator:
    $$0.8 = \frac{3 (4)}{\sigma}$$
    $$0.8 = \frac{12}{\sigma}$$
3.  Rearrange the equation to solve for $\sigma$:
    $$\sigma \times 0.8 = 12$$
    $$\sigma = \frac{12}{0.8}$$
    $$\sigma = 15$$

**Answer:** The Standard Deviation is **15**.

---

### Example 5: Calculation from a Full Data Set

**Question:** Calculate the Karl Pearson's Coefficient of Skewness for the following frequency distribution.

| $X$ (Marks) | 10 | 20 | 30 | 40 | 50 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $f$ (Students) | 5 | 10 | 25 | 6 | 4 |

**Solution:**
To find $Sk_p$, we need to calculate the Mean ($\bar{X}$), Mode ($Z$), and Standard Deviation ($\sigma$) first.

**Step 1: Find the Mode ($Z$)**
The Mode is the $X$ value with the highest frequency.
* The highest frequency ($f$) is 25.
* The $X$ value corresponding to $f=25$ is 30.
* **Mode ($Z$) = 30**

**Step 2: Find the Mean ($\bar{X}$)**
We need $\sum fX$ and $N = \sum f$.

| $X$ | $f$ | $fX$ |
| :--- | :---: | :---: |
| 10 | 5 | 50 |
| 20 | 10 | 200 |
| 30 | 25 | 750 |
| 40 | 6 | 240 |
| 50 | 4 | 200 |
| **Total** | **$N=50$** | **$\sum fX=1440$** |

* **Mean ($\bar{X}$) = $\frac{\sum fX}{N} = \frac{1440}{50} = 28.8$**

**Step 3: Find the Standard Deviation ($\sigma$)**
$\sigma = \sqrt{\frac{\sum f(d^2)}{N}}$ where $d = (X - \bar{X}) = (X - 28.8)$
*Alternatively, we can use $\sigma = \sqrt{\frac{\sum fX^2}{N} - (\bar{X})^2}$, which is often easier.* Let's use that.

| $X$ | $f$ | $X^2$ | $fX^2$ ($f \times X^2$) |
| :--- | :---: | :---: | :---: |
| 10 | 5 | 100 | 500 |
| 20 | 10 | 400 | 4000 |
| 30 | 25 | 900 | 22500 |
| 40 | 6 | 1600 | 9600 |
| 50 | 4 | 2500 | 10000 |
| **Total** | **$N=50$** | | **$\sum fX^2=46600$** |

* $\sigma = \sqrt{\frac{46600}{50} - (28.8)^2}$
* $\sigma = \sqrt{932 - 829.44}$
* $\sigma = \sqrt{102.56}$
* **$\sigma \approx 10.13$**

**Step 4: Calculate Skewness ($Sk_p$)**
* $\bar{X} = 28.8$
* $Z = 30$
* $\sigma = 10.13$

$$\text{Sk}_p = \frac{\bar{X} - Z}{\sigma}$$
$$\text{Sk}_p = \frac{28.8 - 30}{10.13}$$
$$\text{Sk}_p = \frac{-1.2}{10.13}$$
$$\text{Sk}_p \approx -0.118$$

**Answer:** The Karl Pearson's Coefficient of Skewness is **-0.118**.
**Interpretation:** The distribution is **slightly negatively skewed**. This matches our data, as the mean (28.8) is slightly less than the mode (30).