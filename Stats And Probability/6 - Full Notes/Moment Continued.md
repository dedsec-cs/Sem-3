## Moments Continued

### Relations Between Raw Moments And Central Moments

As previously discussed, **Raw Moments ($\mu'_r$)** are calculated about an arbitrary point 'A' (often the origin, $A=0$), while **Central Moments ($\mu_r$)** are calculated about the **mean ($\bar{x}$)**.

Raw moments are often easier to calculate. We can then convert them into the more descriptive central moments using a set of standard relationships.

Let $\mu'_1, \mu'_2, \mu'_3, \mu'_4$ be the first four raw moments calculated about an arbitrary point 'A'.
Let $\bar{x}$ be the true mean of the data.

First, we establish the distance between the arbitrary point 'A' and the true mean $\bar{x}$.
Let $d = \bar{x} - A$.
We know that $\bar{x} = A + \mu'_1$ (from the definition of $\mu'_1$), so $d = \mu'_1$.

The relationships to convert the first four raw moments to central moments are:

* **First Central Moment ($\mu_1$):**
    $$
    \mu_1 = 0
    $$
    This is true by definition. The sum of deviations from the mean is always zero.

* **Second Central Moment ($\mu_2$):**
    $$
    \mu_2 = \mu'_2 - (\mu'_1)^2
    $$
    This is the most famous relationship. It states: **Variance = (Second raw moment) - (First raw moment squared)**.

* **Third Central Moment ($\mu_3$):**
    $$
    \mu_3 = \mu'_3 - 3\mu'_1\mu'_2 + 2(\mu'_1)^3
    $$

* **Fourth Central Moment ($\mu_4$):**
    $$
    \mu_4 = \mu'_4 - 4\mu'_1\mu'_3 + 6(\mu'_1)^2\mu'_2 - 3(\mu'_1)^4
    $$

These formulas are the tools that allow us to use a simpler calculation method (raw moments) to find the more meaningful values (central moments) used to describe variance, skewness, and kurtosis.

---

### Skewness

**Definition:** Skewness is a measure of the **asymmetry** or **lopsidedness** of a probability distribution. A perfectly symmetrical distribution (like a bell curve) has zero skewness.

* **Symmetrical Distribution (Zero Skewness):** The data values are evenly distributed on both sides of the center.
    * **Mean = Median = Mode**

* **Positively Skewed Distribution (Skewed Right):**
    * The "tail" of the distribution is longer on the **right side**.
    * This means there are a few unusually **high** values that pull the mean to the right.
    * **Mean > Median > Mode**

* **Negatively Skewed Distribution (Skewed Left):**
    * The "tail" of the distribution is longer on the **left side**.
    * This means there are a few unusually **low** values that pull the mean to the left.
    * **Mode > Median > Mean**

Skewness tells us the direction and relative magnitude of a distribution's deviation from symmetry.

---

### Karl Pearson's Coefficient of skewnesss

This is a **relative measure** of skewness, meaning it gives a single number that can be compared across different datasets (regardless of their units). It is based on the relationship between the mean, median, and mode.

**Formula 1 (Based on Mode):**
$$
Sk_p = \frac{\text{Mean} - \text{Mode}}{\text{Standard Deviation}}
$$

* **Interpretation:**
    * If $\text{Mean} > \text{Mode}$, the coefficient is positive (positively skewed).
    * If $\text{Mean} < \text{Mode}$, the coefficient is negative (negatively skewed).
    * If $\text{Mean} = \text{Mode}$, the coefficient is $0$ (symmetrical).

**Formula 2 (Based on Median):**
This formula is preferred when the mode is ill-defined (e.g., multimodal data). It uses the empirical relationship: $\text{Mode} \approx 3 \times \text{Median} - 2 \times \text{Mean}$.

$$
Sk_p = \frac{3 (\text{Mean} - \text{Median})}{\text{Standard Deviation}}
$$

* **Note:** The value of Pearson's coefficient typically lies between **-3 and +3**. For most distributions, it lies between -1 and +1.

---

### Bowley's Method

Bowley's coefficient of skewness is also a relative measure, but it is based on the **quartiles** ($Q_1, Q_2, Q_3$). It measures skewness based on the middle $50\%$ of the data, which makes it **robust to outliers** (not affected by extreme values).

**Definition:** It compares the distance of the third quartile ($Q_3$) from the median ($Q_2$) with the distance of the median ($Q_2$) from the first quartile ($Q_1$).

* In a symmetrical distribution, $\text{Median} - Q_1 = Q_3 - \text{Median}$.
* In a positively skewed distribution, $Q_3 - \text{Median} > \text{Median} - Q_1$.
* In a negatively skewed distribution, $Q_3 - \text{Median} < \text{Median} - Q_1$.

**Formula:**
$$
Sk_b = \frac{(Q_3 - Q_2) - (Q_2 - Q_1)}{Q_3 - Q_1}
$$
This simplifies to:
$$
Sk_b = \frac{Q_3 + Q_1 - 2Q_2}{Q_3 - Q_1}
$$
(Where $Q_2$ is the Median)

* **Interpretation:** The value of Bowley's coefficient always lies between **-1 and +1**.
    * $Sk_b > 0$: Positively skewed
    * $Sk_b < 0$: Negatively skewed
    * $Sk_b = 0$: Symmetrical

---

### Method Of Moments

This is the most mathematically precise method for measuring skewness. It uses the **third central moment ($\mu_3$)**, which is inherently a measure of asymmetry.

We know $\mu_3 = \frac{\sum f_i (x_i - \bar{x})^3}{N}$.

* If the distribution is symmetrical, the positive and negative deviations $(x_i - \bar{x})^3$ will cancel each other out, and $\mu_3 = 0$.
* If the distribution is positively skewed, the large positive deviations (cubed) will overpower the negative ones, and $\mu_3 > 0$.
* If the distribution is negatively skewed, the large negative deviations (cubed) will overpower the positive ones, and $\mu_3 < 0$.

However, $\mu_3$ is an **absolute measure**. Its value depends on the units of the data (e.g., $\text{cm}^3$). To make it a **relative measure** that is unit-free, we standardize it by dividing by the cube of the standard deviation ($\sigma^3$). This leads to the coefficient of skewness based on moments.

---

### Kurtosis

**Definition:** Kurtosis measures the **"peakedness"** or **"tailedness"** of a distribution compared to a **Normal Distribution** (the standard bell curve). It describes how concentrated the data is around the mean and how heavy the tails are.

Kurtosis is measured by the **fourth central moment ($\mu_4$)**.

We classify distributions into three types based on their kurtosis:

1.  **Mesokurtic:**
    * This is the benchmark. The distribution has the same peakedness and tail weight as a **Normal Distribution**.
    * Kurtosis value (see coefficient below) is $3$.

2.  **Leptokurtic:**
    * The distribution is **more peaked** (lepto = "slender") than a normal distribution.
    * It has a sharper peak and **heavier tails**. This means there is a higher concentration of values near the mean, *and* a higher probability of extreme outlier values.
    * Kurtosis value is $> 3$.

3.  **Platykurtic:**
    * The distribution is **flatter** (platy = "broad") than a normal distribution.
    * It has a lower, wider peak and **lighter tails**. This means there is a lower concentration of values near the mean and a lower probability of extreme values.
    * Kurtosis value is $< 3$.

---

### Coefficient Of Skewness and Kurtosis Based On Moments

These are the unit-free, relative measures of skewness and kurtosis derived from the central moments. They are often denoted by the Greek letters Beta ($\beta$) and Gamma ($\gamma$).

**Coefficient of Skewness ($\beta_1$ and $\gamma_1$):**

This coefficient is derived from the third central moment ($\mu_3$) and the second central moment ($\mu_2$, which is variance).

$$
\beta_1 = \frac{\mu_3^2}{\mu_2^3}
$$

* $\beta_1$ is always positive (due to squaring $\mu_3$), so it only measures the *magnitude* of skewness, not the direction.
* For a symmetrical distribution, $\mu_3 = 0$, so $\beta_1 = 0$.

To get the direction (positive or negative), we use $\gamma_1$ (gamma one), which is the square root of $\beta_1$:

$$
\gamma_1 = \sqrt{\beta_1} = \frac{\mu_3}{\sqrt{\mu_2^3}} = \frac{\mu_3}{\sigma^3}
$$
(The sign of $\gamma_1$ is taken from the sign of $\mu_3$)

* **Interpretation ($\gamma_1$):**
    * $\gamma_1 > 0$: Positively skewed
    * $\gamma_1 < 0$: Negatively skewed
    * $\gamma_1 = 0$: Symmetrical

**Coefficient of Kurtosis ($\beta_2$ and $\gamma_2$):**

This coefficient is derived from the fourth central moment ($\mu_4$) and the second central moment ($\mu_2$).

$$
\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{\mu_4}{\sigma^4}
$$

* This is the primary measure of kurtosis.
* **Interpretation ($\beta_2$):**
    * $\beta_2 = 3$: **Mesokurtic** (Normal distribution)
    * $\beta_2 > 3$: **Leptokurtic** (Peaked, heavy tails)
    * $\beta_2 < 3$: **Platykurtic** (Flat, light tails)

**Excess Kurtosis ($\gamma_2$):**
Often, statisticians prefer to measure kurtosis *relative to* the normal distribution (which has $\beta_2 = 3$). This is called "excess kurtosis."

$$
\gamma_2 = \beta_2 - 3
$$

* **Interpretation ($\gamma_2$):**
    * $\gamma_2 = 0$: **Mesokurtic**
    * $\gamma_2 > 0$: **Leptokurtic**
    * $\gamma_2 < 0$: **Platykurtic**
    * This is why you will often see "Kurtosis = 0" as the benchmark; it is referring to the *excess kurtosis*.