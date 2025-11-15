# Summary
### Moments About Mean (central moment)

**Central Moments** are calculated using deviations from the **arithmetic mean ($\bar{x}$)**. They are "central" because the mean is the center of gravity of the distribution. They are the most useful moments for describing the shape of a distribution because they are not affected by changes in the data's location (i.e., adding a constant to all values).

The $r^{th}$ central moment is denoted by the Greek letter $\mu_r$ (mu with subscript r).

**Formula for Ungrouped Data:**
$$
\mu_r = \frac{\sum (x_i - \bar{x})^r}{N}
$$

**Formula for Grouped Data:**
$$
\mu_r = \frac{\sum f_i (x_i - \bar{x})^r}{N}
$$
Where:
* $x_i$ = Individual observation (or midpoint of a class)
* $\bar{x}$ = The arithmetic mean
* $f_i$ = Frequency of the observation
* $N$ = Total frequency ($\sum f_i$)
* $r$ = The order of the moment ($1, 2, 3, 4, ...$)

**Interpretation of the First Four Central Moments:**

* **First Central Moment ($\mu_1$):**
    $$
    \mu_1 = \frac{\sum f_i (x_i - \bar{x})^1}{N} = 0
    $$
    The first central moment is **always zero**. This is a fundamental property of the arithmetic mean, as the sum of all deviations from the mean is always zero.

* **Second Central Moment ($\mu_2$):**
    $$
    \mu_2 = \frac{\sum f_i (x_i - \bar{x})^2}{N}
    $$
    This is the **Variance ($\sigma^2$)**. It is the most common measure of the data's dispersion or spread.

* **Third Central Moment ($\mu_3$):**
    $$
    \mu_3 = \frac{\sum f_i (x_i - \bar{x})^3}{N}
    $$
    This moment is used to measure **Skewness** (asymmetry).
    * If $\mu_3 > 0$, the distribution is **positively skewed** (long tail to the right).
    * If $\mu_3 < 0$, the distribution is **negatively skewed** (long tail to the left).
    * If $\mu_3 = 0$, the distribution is **symmetrical**.

* **Fourth Central Moment ($\mu_4$):**
    $$
    \mu_4 = \frac{\sum f_i (x_i - \bar{x})^4}{N}
    $$
    This moment is used to measure **Kurtosis** (peakedness). It describes how "tailed" and "peaked" the distribution is compared to a normal (bell-shaped) distribution.

---

### Moments About Any Arbitrary Number (Raw moment)

**Raw Moments** (also called non-central moments) are calculated using deviations from an **arbitrary point 'A'**. This point 'A' can be any number, but it is often chosen to simplify calculations (this is the basis of the "shortcut method" for calculating variance).

The $r^{th}$ raw moment about point 'A' is denoted by $\mu'_r$ (mu-prime).

**Formula for Ungrouped Data:**
$$
\mu'_r = \frac{\sum (x_i - A)^r}{N}
$$

**Formula for Grouped Data:**
$$
\mu'_r = \frac{\sum f_i (x_i - A)^r}{N}
$$

While easier to compute, raw moments are less descriptive than central moments. Their main purpose is to be used as a stepping stone to find the central moments.

**Relationship between Central and Raw Moments:**
The central moments ($\mu_r$) can be calculated from the raw moments ($\mu'_r$) using the following conversion formulas (these are known as **Sheppard's Corrections** in some contexts, though the formulas themselves are general conversions):

* $\mu_1 = 0$ (by definition)
* $\mu_2 = \mu'_2 - (\mu'_1)^2$
* $\mu_3 = \mu'_3 - 3\mu'_1\mu'_2 + 2(\mu'_1)^3$
* $\mu_4 = \mu'_4 - 4\mu'_1\mu'_3 + 6(\mu'_1)^2\mu'_2 - 3(\mu'_1)^4$

The most important of these is the formula for $\mu_2$:
**$\text{Variance} = (\text{Second raw moment}) - (\text{First raw moment})^2$**

---

### Moments About Origin

**Moments about the Origin** are the most common type of **raw moment**. They are simply a special case where the arbitrary point 'A' is set to **zero ($A=0$)**.

**Formula for Ungrouped Data:**
$$
\mu'_r (\text{about 0}) = \frac{\sum (x_i - 0)^r}{N} = \frac{\sum x_i^r}{N}
$$

**Formula for Grouped Data:**
$$
\mu'_r (\text{about 0}) = \frac{\sum f_i (x_i - 0)^r}{N} = \frac{\sum f_i x_i^r}{N}
$$

**Interpretation of the First Two Raw Moments about the Origin:**

* **First Raw Moment about Origin ($\mu'_1$):**
    $$
    \mu'_1 = \frac{\sum f_i x_i^1}{N} = \frac{\sum f_i x_i}{N}
    $$
    This is the formula for the **Arithmetic Mean ($\bar{x}$)**. Therefore, the first moment about the origin is simply the mean of the distribution.

* **Second Raw Moment about Origin ($\mu'_2$):**
    $$
    \mu'_2 = \frac{\sum f_i x_i^2}{N}
    $$
    This is the "mean of the squares." It doesn't have a simple name on its own, but it is critical for calculating variance.

**Putting It All Together (The "Shortcut Formula" for Variance):**

Let's use the conversion formula we learned earlier: $\mu_2 = \mu'_2 - (\mu'_1)^2$
Now, let's use the moments about the origin ($A=0$):

* $\mu_2$ = **Variance ($\sigma^2$)**
* $\mu'_1$ = First raw moment about origin = **Mean ($\bar{x}$)**
* $\mu'_2$ = Second raw moment about origin = $\frac{\sum f_i x_i^2}{N}$

By substituting these in, we get the standard computational formula for variance:

$$
\sigma^2 = \left( \frac{\sum f_i x_i^2}{N} \right) - (\bar{x})^2
$$

This proves that the "shortcut formula" for variance is just the formula for converting the second raw moment about the origin into the second central moment.

---


# Moment

### Meaning Of Moment

In statistics, a **moment** is a quantitative measure that describes the shape of a data distribution. The term is borrowed from physics, where "moment" refers to a force's tendency to cause rotation around a point (like the center of mass).

In statistics, we use moments to describe the shape of a distribution relative to a point.

* **Moments about the Origin (Raw Moments):** When the moments are calculated around the value '0'. The first raw moment is the Arithmetic Mean ($\bar{X}$).
* **Moments about the Mean (Central Moments):** When the moments are calculated around the Arithmetic Mean ($\bar{X}$). These are more common and are used to describe the *shape* of the distribution, independent of its location.

We will focus on **Central Moments**, denoted by the Greek letter $\mu$ (mu).

* **First Central Moment ($\mu_1$):** Measures the center of gravity. It is always **zero**.
* **Second Central Moment ($\mu_2$):** Measures the **Variance**. It describes the *spread* or *width* of the distribution.
* **Third Central Moment ($\mu_3$):** Measures **Skewness**. It describes the *asymmetry* of the distribution (whether it leans to the left or right).
* **Fourth Central Moment ($\mu_4$):** Measures **Kurtosis**. It describes the *peakedness* and *tail thickness* of the distribution.

---

# Moments About Mean For Individual Series

These are the central moments calculated for ungrouped data (a simple list of values).

### Formula

The **$r$-th moment about the mean** ($\mu_r$) is defined as the mean of the $r$-th power of the deviations from the mean.

$$\mu_r = \frac{\sum (X - \bar{X})^r}{N}$$

* **First Moment ($\mu_1$):**
    $$\mu_1 = \frac{\sum (X - \bar{X})^1}{N}$$
* **Second Moment ($\mu_2$):**
    $$\mu_2 = \frac{\sum (X - \bar{X})^2}{N}$$
* **Third Moment ($\mu_3$):**
    $$\mu_3 = \frac{\sum (X - \bar{X})^3}{N}$$

### Tricks (Key Properties)

1.  The **First Moment about the mean ($\mu_1$) is always zero.** This is because $\sum (X - \bar{X}) = 0$ (the sum of deviations from the mean is always zero), so $\frac{0}{N} = 0$.
2.  The **Second Moment about the mean ($\mu_2$) is the Variance ($\sigma^2$).** This is the definition of variance.

### Relation of Third Moment About Mean And Variance And Standard Deviation

* **Variance ($\sigma^2$):** Is exactly equal to the Second Moment about the mean ($\mu_2$).
    > $\sigma^2 = \mu_2$

* **Standard Deviation ($\sigma$):** Is the square root of the Variance, so it is the square root of the Second Moment about the mean.
    > $\sigma = \sqrt{\mu_2}$

* **Third Moment ($\mu_3$):** This value is used to calculate **skewness**. It is not directly related to variance by a simple formula, but they are both moments of the same distribution.
    * If $\mu_3 = 0$, the distribution is symmetrical.
    * If $\mu_3 > 0$ (positive), the distribution is positively (right) skewed.
    * If $\mu_3 < 0$ (negative), the distribution is negatively (left) skewed.

### Solved Example

**Question:** Find the first three moments about the mean for the following data: 2, 3, 4, 5, 6.

**Solution:**
Here $N = 5$.

**Step 1: Calculate the Mean ($\bar{X}$).**
$$\bar{X} = \frac{\sum X}{N} = \frac{2 + 3 + 4 + 5 + 6}{5} = \frac{20}{5} = 4$$

**Step 2: Create a calculation table.**
We need the sums of the deviations, the squared deviations, and the cubed deviations.
Let $d = (X - \bar{X}) = (X - 4)$.

| $X$ | $d = (X - 4)$ | $d^2 = (X - 4)^2$ | $d^3 = (X - 4)^3$ |
| :--- | :--- | :--- | :--- |
| 2 | -2 | 4 | -8 |
| 3 | -1 | 1 | -1 |
| 4 | 0 | 0 | 0 |
| 5 | 1 | 1 | 1 |
| 6 | 2 | 4 | 8 |
| **Total** | **$\sum d = 0$** | **$\sum d^2 = 10$** | **$\sum d^3 = 0$** |

**Step 3: Calculate the moments.**

* **First Moment ($\mu_1$):**
    $$\mu_1 = \frac{\sum d}{N} = \frac{0}{5} = 0$$

* **Second Moment ($\mu_2$):**
    $$\mu_2 = \frac{\sum d^2}{N} = \frac{10}{5} = 2$$

* **Third Moment ($\mu_3$):**
    $$\mu_3 = \frac{\sum d^3}{N} = \frac{0}{5} = 0$$

**Interpretation:**
* $\mu_1 = 0$, which is always true.
* $\mu_2 = 2$. This means the **Variance ($\sigma^2$) is 2**.
* $\mu_3 = 0$. This indicates that the data is **perfectly symmetrical**, which we can see (4 is the center, 3 and 5 are balanced, 2 and 6 are balanced).

---

# Moments About Mean For Discrete Or Continous Distribution

For data with frequencies, the logic is the same, but we must multiply each deviation by its frequency ($f$).

### Formula

The **$r$-th moment about the mean** ($\mu_r$) for a frequency distribution is:

$$\mu_r = \frac{\sum f(d)^r}{N} \quad \text{where } N = \sum f$$

* For **Discrete Series:** $d = (X - \bar{X})$
* For **Continuous Series:** $d = (m - \bar{X})$, where $m$ is the mid-point.

**Formulas:**
* **First Moment ($\mu_1$):**
    $$\mu_1 = \frac{\sum f(X - \bar{X})}{N} \text{ or } \frac{\sum f(m - \bar{X})}{N}$$
* **Second Moment ($\mu_2$):**
    $$\mu_2 = \frac{\sum f(X - \bar{X})^2}{N} \text{ or } \frac{\sum f(m - \bar{X})^2}{N}$$
* **Third Moment ($\mu_3$):**
    $$\mu_3 = \frac{\sum f(X - \bar{X})^3}{N} \text{ or } \frac{\sum f(m - \bar{X})^3}{N}$$

### Tricks (Key Properties)

These are identical to the individual series:
1.  The **First Moment about the mean ($\mu_1$) is always zero.**
2.  The **Second Moment about the mean ($\mu_2$) is the Variance ($\sigma^2$).**

### Relation of Third Moment About Mean And Variance And Standard Deviation

This relationship is also identical to the individual series:
* **Variance ($\sigma^2$)** = $\mu_2$
* **Standard Deviation ($\sigma$)** = $\sqrt{\mu_2}$
* **Third Moment ($\mu_3$)** is the primary measure used to calculate skewness.

### Solved Example (Discrete Series)

**Question:** Find the first three moments about the mean for the following distribution.

| $X$ | 1 | 2 | 3 | 4 | 5 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $f$ | 2 | 4 | 6 | 4 | 2 |

**Solution:**

**Step 1: Calculate $N$ and the Mean ($\bar{X}$).**
We first need $\sum f$ and $\sum fX$.

| $X$ | $f$ | $fX$ |
| :--- | :--- | :--- |
| 1 | 2 | 2 |
| 2 | 4 | 8 |
| 3 | 6 | 18 |
| 4 | 4 | 16 |
| 5 | 2 | 10 |
| **Total** | **$N = 18$** | **$\sum fX = 54$** |

* **Mean ($\bar{X}$):**
    $$\bar{X} = \frac{\sum fX}{N} = \frac{54}{18} = 3$$

**Step 2: Create the main calculation table.**
Let $d = (X - \bar{X}) = (X - 3)$.

| $X$ | $f$ | $d = (X - 3)$ | $d^2$ | $d^3$ | $fd$ | $fd^2$ | $fd^3$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 2 | -2 | 4 | -8 | 2 $\times$ -2 = -4 | 2 $\times$ 4 = 8 | 2 $\times$ -8 = -16 |
| 2 | 4 | -1 | 1 | -1 | 4 $\times$ -1 = -4 | 4 $\times$ 1 = 4 | 4 $\times$ -1 = -4 |
| 3 | 6 | 0 | 0 | 0 | 6 $\times$ 0 = 0 | 6 $\times$ 0 = 0 | 6 $\times$ 0 = 0 |
| 4 | 4 | 1 | 1 | 1 | 4 $\times$ 1 = 4 | 4 $\times$ 1 = 4 | 4 $\times$ 1 = 4 |
| 5 | 2 | 2 | 4 | 8 | 2 $\times$ 2 = 4 | 2 $\times$ 4 = 8 | 2 $\times$ 8 = 16 |
| **Total** | **$N=18$** | | | | **$\sum fd = 0$** | **$\sum fd^2 = 24$** | **$\sum fd^3 = 0$** |

**Step 3: Calculate the moments.**

* **First Moment ($\mu_1$):**
    $$\mu_1 = \frac{\sum fd}{N} = \frac{0}{18} = 0$$

* **Second Moment ($\mu_2$):**
    $$\mu_2 = \frac{\sum fd^2}{N} = \frac{24}{18} = 1.333$$

* **Third Moment ($\mu_3$):**
    $$\mu_3 = \frac{\sum fd^3}{N} = \frac{0}{18} = 0$$

**Interpretation:**
* $\mu_1 = 0$, as expected.
* $\mu_2 = 1.333$. This means the **Variance ($\sigma^2$) is 1.333**.
* $\mu_3 = 0$. This indicates the distribution is **symmetrical**.


Here are the notes on Moments about the Origin and their relation to Moments about the Mean.

---

# Moments about Origin in Statistics

**Moments about the Origin**, also known as **Raw Moments**, are the moments calculated around the value '0'. They are denoted by a prime symbol ($\mu_r'$).

These moments describe the distribution in its "raw" form, without centering it first. The first moment about the origin is simply the arithmetic mean.

### Formula

The **$r$-th moment about the origin** ($\mu_r'$) is defined as the mean of the $r$-th power of the $X$ values.

* **For Individual Series:**
    $$\mu_r' = \frac{\sum X^r}{N}$$

* **For Discrete/Continuous Series:**
    $$\mu_r' = \frac{\sum fX^r}{N} \text{ or } \frac{\sum fm^r}{N} \quad (\text{where } N = \sum f)$$

**The first four raw moments are:**

1.  **First Moment ($\mu_1'$):**
    $$\mu_1' = \frac{\sum X}{N} = \bar{X} \text{ (The Arithmetic Mean)}$$

2.  **Second Moment ($\mu_2'$):**
    $$\mu_2' = \frac{\sum X^2}{N}$$

3.  **Third Moment ($\mu_3'$):**
    $$\mu_3' = \frac{\sum X^3}{N}$$

4.  **Fourth Moment ($\mu_4'$):**
    $$\mu_4' = \frac{\sum X^4}{N}$$

---

### Solved Example

**Question:** Find the first three moments about the origin for the following data: 2, 3, 4, 5, 6. (This is the same data from our previous example on central moments).

**Solution:**
Here $N = 5$. We need to find the sum of $X$, $X^2$, and $X^3$.

**Calculation Table:**

| $X$ | $X^2$ | $X^3$ |
| :--- | :--- | :--- |
| 2 | 4 | 8 |
| 3 | 9 | 27 |
| 4 | 16 | 64 |
| 5 | 25 | 125 |
| 6 | 36 | 216 |
| **$\sum X = 20$** | **$\sum X^2 = 90$** | **$\sum X^3 = 440$** |

**Calculation:**

* **First Moment ($\mu_1'$):**
    $$\mu_1' = \frac{\sum X}{N} = \frac{20}{5} = 4$$
    *(This is the Arithmetic Mean, $\bar{X}$)*

* **Second Moment ($\mu_2'$):**
    $$\mu_2' = \frac{\sum X^2}{N} = \frac{90}{5} = 18$$

* **Third Moment ($\mu_3'$):**
    $$\mu_3' = \frac{\sum X^3}{N} = \frac{440}{5} = 88$$

**Answer:** The first three moments about the origin are $\mu_1' = 4$, $\mu_2' = 18$, and $\mu_3' = 88$.

---

## Relation between Moment about Mean and Moment about Origin

**Moments about the Mean** (Central Moments, $\mu_r$) can be expressed in terms of **Moments about the Origin** (Raw Moments, $\mu_r'$).

This is extremely useful because it is often easier to calculate the raw moments first (summing $X$, $X^2$, $X^3$, etc.) and then use these conversion formulas to find the central moments, rather than calculating all the deviations $(X - \bar{X})$.

### Formula

Remember that $\mu_1' = \bar{X}$.

* **First Central Moment:**
    $$\mu_1 = 0 \text{ (By definition)}$$

* **Second Central Moment (Variance):**
    $$\mu_2 = \mu_2' - (\mu_1')^2$$
    *(This is the most important one. It means: **Variance = (Mean of the squares) - (Square of the mean)**)*

* **Third Central Moment:**
    $$\mu_3 = \mu_3' - 3(\mu_2')(\mu_1') + 2(\mu_1')^3$$

* **Fourth Central Moment:**
    $$\mu_4 = \mu_4' - 4(\mu_3')(\mu_1') + 6(\mu_2')(\mu_1')^2 - 3(\mu_1')^4$$

---

### Solved Example

**Question:** Using the data from the previous two examples, confirm the relationship between the moments.

**Data:** 2, 3, 4, 5, 6

**From our previous calculations, we know:**
* **Moments about Origin:** $\mu_1' = 4$, $\mu_2' = 18$, $\mu_3' = 88$
* **Moments about Mean:** $\mu_1 = 0$, $\mu_2 = 2$, $\mu_3 = 0$

**Let's use the conversion formulas to see if we get the correct moments about the mean.**

**1. Calculate $\mu_2$ (Variance):**
* **Formula:** $\mu_2 = \mu_2' - (\mu_1')^2$
* **Calculation:**
    $$\mu_2 = 18 - (4)^2$$
    $$\mu_2 = 18 - 16$$
    $$\mu_2 = 2$$
* **Check:** This matches our direct calculation of $\mu_2$ in the previous lesson.

**2. Calculate $\mu_3$:**
* **Formula:** $\mu_3 = \mu_3' - 3(\mu_2')(\mu_1') + 2(\mu_1')^3$
* **Calculation:**
    $$\mu_3 = 88 - 3(18)(4) + 2(4)^3$$
    $$\mu_3 = 88 - 3(72) + 2(64)$$
    $$\mu_3 = 88 - 216 + 128$$
    $$\mu_3 = 216 - 216$$
    $$\mu_3 = 0$$
* **Check:** This also matches our direct calculation of $\mu_3$ in the previous lesson.

This example proves that the conversion formulas work and are a valid alternative method for finding the central moments.



Here are the notes on Karl Pearson's coefficients and practice questions on moments.

---

# Moment About Mean Questions

## Karl Pearson Coefficients

Karl Pearson's coefficients are dimensionless measures used to describe the **shape** of a distribution. They use the central moments ($\mu_r$) to quantify skewness and kurtosis.

### Beta Coefficients

1.  **Beta 1 ($\beta_1$):** This coefficient measures **skewness** (the asymmetry of the distribution). It is based on the square of the third moment, so its value is always non-negative.
    * **Formula:**
        $$\beta_1 = \frac{\mu_3^2}{\mu_2^3}$$
    * **Interpretation:**
        * If $\beta_1 = 0$, the distribution is symmetrical.
        * If $\beta_1 > 0$, the distribution is skewed (asymmetrical). The larger the value, the greater the skewness.

2.  **Beta 2 ($\beta_2$):** This coefficient measures **kurtosis** (the "peakedness" or "tail-heaviness" of the distribution). It compares the distribution's shape to a normal distribution.
    * **Formula:**
        $$\beta_2 = \frac{\mu_4}{\mu_2^2}$$
    * **Interpretation:**
        * If $\beta_2 = 3$, the distribution has the same kurtosis as a normal distribution (mesokurtic).
        * If $\beta_2 > 3$, the distribution is more peaked with heavier tails than a normal distribution (leptokurtic).
        * If $\beta_2 < 3$, the distribution is flatter with lighter tails than a normal distribution (platykurtic).

---

### Gamma Coefficients

Gamma coefficients are related to Beta coefficients but are often preferred for interpretation.

1.  **Gamma 1 ($\gamma_1$):** This is the **coefficient of skewness**. It is the square root of $\beta_1$ and retains the original sign of $\mu_3$. This makes it more descriptive than $\beta_1$.
    * **Formula:**
        $$\gamma_1 = \sqrt{\beta_1} = \frac{\mu_3}{\mu_2^{3/2}} = \frac{\mu_3}{\sigma^3}$$
    * **Interpretation:**
        * If $\gamma_1 = 0$, the distribution is symmetrical.
        * If $\gamma_1 > 0$, it is positively (right) skewed.
        * If $\gamma_1 < 0$, it is negatively (left) skewed.

2.  **Gamma 2 ($\gamma_2$):** This is the **coefficient of excess kurtosis**. It measures kurtosis relative to the normal distribution (which has $\beta_2 = 3$).
    * **Formula:**
        $$\gamma_2 = \beta_2 - 3$$
    * **Interpretation:**
        * If $\gamma_2 = 0$, the distribution is mesokurtic.
        * If $\gamma_2 > 0$, the distribution is leptokurtic.
        * If $\gamma_2 < 0$, the distribution is platykurtic.

---

## Questions Practice

### Question 1

**The First Four Moments Of A Distribution About The Value '4' of the variable are -1.5, 17, -30 and 108. Find The Moments About Mean, About Origin , Beta 1 and Beta 2. Also Find The Moments About The Point x = 2.**

**Solution:**

First, let's identify what is given. These are moments about an arbitrary point (or provisional moments), $A = 4$.
Let's call these provisional moments $\mu_r'(A)$.

* $A = 4$
* $\mu_1'(A) = -1.5$
* $\mu_2'(A) = 17$
* $\mu_3'(A) = -30$
* $\mu_4'(A) = 108$

---

#### 1. Moments About Mean (Central Moments, $\mu_r$)

We use the conversion formulas that relate moments about an arbitrary point $A$ to the central moments ($\mu_r$) about the mean.

* **$\mu_1$:**
    $\mu_1 = 0$ (By definition, the first moment about the mean is always zero).

* **$\mu_2$ (Variance):**
    $$\mu_2 = \mu_2'(A) - (\mu_1'(A))^2$$
    $$\mu_2 = 17 - (-1.5)^2$$
    $$\mu_2 = 17 - 2.25$$
    **$\mu_2 = 14.75$**

* **$\mu_3$:**
    $$\mu_3 = \mu_3'(A) - 3(\mu_2'(A))(\mu_1'(A)) + 2(\mu_1'(A))^3$$
    $$\mu_3 = (-30) - 3(17)(-1.5) + 2(-1.5)^3$$
    $$\mu_3 = -30 - 3(-25.5) + 2(-3.375)$$
    $$\mu_3 = -30 + 76.5 - 6.75$$
    **$\mu_3 = 39.75$**

* **$\mu_4$:**
    $$\mu_4 = \mu_4'(A) - 4(\mu_3'(A))(\mu_1'(A)) + 6(\mu_2'(A))(\mu_1'(A))^2 - 3(\mu_1'(A))^4$$
    $$\mu_4 = 108 - 4(-30)(-1.5) + 6(17)(-1.5)^2 - 3(-1.5)^4$$
    $$\mu_4 = 108 - 4(45) + 6(17)(2.25) - 3(5.0625)$$
    $$\mu_4 = 108 - 180 + 229.5 - 15.1875$$
    **$\mu_4 = 142.3125$**

**Answer (Part 1):** The moments about the mean are $\mu_1 = 0$, $\mu_2 = 14.75$, $\mu_3 = 39.75$, and $\mu_4 = 142.3125$.

---

#### 2. Moments About Origin (Raw Moments, $\mu_r'$)

To find the moments about the origin (0), we first need the true mean ($\bar{X}$).
$\bar{X} = A + \mu_1'(A) = 4 + (-1.5) = 2.5$

The first moment about the origin ($\mu_1'$) is the mean itself:
**$\mu_1' = \bar{X} = 2.5$**

Now we use the formulas to convert *from* central moments ($\mu_r$) *to* raw moments ($\mu_r'$). Here $\mu_1' = \bar{X} = 2.5$.

* **$\mu_2'$ (Raw):**
    $$\mu_2' = \mu_2 + (\mu_1')^2$$
    $$\mu_2' = 14.75 + (2.5)^2$$
    $$\mu_2' = 14.75 + 6.25$$
    **$\mu_2' = 21$**

* **$\mu_3'$ (Raw):**
    $$\mu_3' = \mu_3 + 3(\mu_2)(\mu_1') + (\mu_1')^3$$
    $$\mu_3' = 39.75 + 3(14.75)(2.5) + (2.5)^3$$
    $$\mu_3' = 39.75 + 110.625 + 15.625$$
    **$\mu_3' = 166$**

* **$\mu_4'$ (Raw):**
    $$\mu_4' = \mu_4 + 4(\mu_3)(\mu_1') + 6(\mu_2)(\mu_1')^2 + (\mu_1')^4$$
    $$\mu_4' = 142.3125 + 4(39.75)(2.5) + 6(14.75)(2.5)^2 + (2.5)^4$$
    $$\mu_4' = 142.3125 + 397.5 + 6(14.75)(6.25) + 39.0625$$
    $$\mu_4' = 142.3125 + 397.5 + 553.125 + 39.0625$$
    **$\mu_4' = 1132$**

**Answer (Part 2):** The moments about the origin are $\mu_1' = 2.5$, $\mu_2' = 21$, $\mu_3' = 166$, and $\mu_4' = 1132$.

---

#### 3. Beta 1 ($\beta_1$) and Beta 2 ($\beta_2$)

We use the central moments ($\mu_r$) that we found in the first section.
* $\mu_2 = 14.75$
* $\mu_3 = 39.75$
* $\mu_4 = 142.3125$

* **Beta 1 ($\beta_1$):**
    $$\beta_1 = \frac{\mu_3^2}{\mu_2^3}$$
    $$\beta_1 = \frac{(39.75)^2}{(14.75)^3}$$
    $$\beta_1 = \frac{1580.0625}{3211.546875}$$
    **$\beta_1 \approx 0.492$**

* **Beta 2 ($\beta_2$):**
    $$\beta_2 = \frac{\mu_4}{\mu_2^2}$$
    $$\beta_2 = \frac{142.3125}{(14.75)^2}$$
    $$\beta_2 = \frac{142.3125}{217.5625}$$
    **$\beta_2 \approx 0.654$**

**Answer (Part 3):** $\beta_1 \approx 0.492$ (skewed) and $\beta_2 \approx 0.654$ (very platykurtic, or flat).

---

#### 4. Moments About The Point x = 2

This is a "change of origin" problem. We have moments about $A = 4$ and want to find moments about $B = 2$.
Let $h = A - B = 4 - 2 = 2$.
The relationship between the deviations is $d_B = (X - B) = (X - A) + (A - B) = d_A + h$.
So, $\mu_r'(B) = \frac{\sum(d_A + h)^r}{N}$. This gives us the following conversion formulas:

* **$\mu_1'(B=2)$:**
    $$\mu_1'(B) = \mu_1'(A) + h$$
    $$\mu_1'(B) = -1.5 + 2$$
    **$\mu_1'(B) = 0.5$**

* **$\mu_2'(B=2)$:**
    $$\mu_2'(B) = \mu_2'(A) + 2h\mu_1'(A) + h^2$$
    $$\mu_2'(B) = 17 + 2(2)(-1.5) + (2)^2$$
    $$\mu_2'(B) = 17 - 6 + 4$$
    **$\mu_2'(B) = 15$**

* **$\mu_3'(B=2)$:**
    $$\mu_3'(B) = \mu_3'(A) + 3h\mu_2'(A) + 3h^2\mu_1'(A) + h^3$$
    $$\mu_3'(B) = -30 + 3(2)(17) + 3(2)^2(-1.5) + (2)^3$$
    $$\mu_3'(B) = -30 + 102 + 3(4)(-1.5) + 8$$
    $$\mu_3'(B) = -30 + 102 - 18 + 8$$
    **$\mu_3'(B) = 62$**

* **$\mu_4'(B=2)$:**
    $$\mu_4'(B) = \mu_4'(A) + 4h\mu_3'(A) + 6h^2\mu_2'(A) + 4h^3\mu_1'(A) + h^4$$
    $$\mu_4'(B) = 108 + 4(2)(-30) + 6(2)^2(17) + 4(2)^3(-1.5) + (2)^4$$
    $$\mu_4'(B) = 108 - 240 + 6(4)(17) + 4(8)(-1.5) + 16$$
    $$\mu_4'(B) = 108 - 240 + 408 - 48 + 16$$
    **$\mu_4'(B) = 244$**

**Answer (Part 4):** The moments about the point $x=2$ are 0.5, 15, 62, and 244.

---
---

### Question 2

**The First Three Moments Of A Distribution About The Value '2' of the variable are 1, 16 and -40. Show That The Mean Is 3, Variance is 15 and $\mu_3 = - 86$.**

**Solution:**

First, let's identify the given information. These are provisional moments about $A = 2$.
* $A = 2$
* $\mu_1'(A) = 1$
* $\mu_2'(A) = 16$
* $\mu_3'(A) = -40$

---

#### 1. Show Mean is 3

The formula for the Arithmetic Mean ($\bar{X}$) based on a provisional mean ($A$) is:
$$\bar{X} = A + \mu_1'(A)$$

* **Calculation:**
    $$\bar{X} = 2 + 1$$
    $$\bar{X} = 3$$

**Result: The Mean is 3. (Proven)**

---

#### 2. Show Variance is 15

The Variance ($\sigma^2$) is the second central moment ($\mu_2$). We use the formula to convert from provisional moments to the second central moment.

$$\mu_2 = \mu_2'(A) - (\mu_1'(A))^2$$

* **Calculation:**
    $$\mu_2 = 16 - (1)^2$$
    $$\mu_2 = 16 - 1$$
    $$\mu_2 = 15$$

**Result: The Variance is 15. (Proven)**

---

#### 3. Show $\mu_3 = - 86$

$\mu_3$ is the third central moment. We use the conversion formula.

$$\mu_3 = \mu_3'(A) - 3(\mu_2'(A))(\mu_1'(A)) + 2(\mu_1'(A))^3$$

* **Calculation:**
    $$\mu_3 = (-40) - 3(16)(1) + 2(1)^3$$
    $$\mu_3 = -40 - 48 + 2(1)$$
    $$\mu_3 = -40 - 48 + 2$$
    $$\mu_3 = -88 + 2$$
    $$\mu_3 = -86$$

**Result: $\mu_3 = - 86$. (Proven)**