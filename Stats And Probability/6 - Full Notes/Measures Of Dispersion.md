## Measures Of Dispersion

Measures of **Dispersion** (or variability, scatter, or spread) are statistical values that describe **how spread out** or scattered the data points are in a dataset. They tell you the degree to which individual items in a distribution vary from each other and from the central value (like the mean or median).

* **Low Dispersion:** Data points are closely clustered around the mean, indicating high consistency.
* **High Dispersion:** Data points are widely scattered, indicating low consistency.

![[Pasted image 20251109135738.png]]

![[Pasted image 20251109135744.png]]
While measures of central tendency (mean, median, mode) tell you where the **center** of the data is, measures of dispersion tell you about the **reliability** of that center. 

---

### Interquartile Range (IQR)

The Interquartile Range is a measure of dispersion that focuses only on the **middle 50%** of the data. It is highly valued because it is **not affected by extreme values** (outliers) in the data set.

**Definition**

The Interquartile Range (**IQR**) is the difference between the **Third Quartile ($Q_3$)** and the **First Quartile ($Q_1$)**.

* **Quartiles** are the values that divide an ordered dataset into **four equal parts** (each containing 25% of the data).
    * **$Q_1$ (First Quartile / Lower Quartile):** The value below which $25\%$ of the data lies. It is essentially the median of the lower half of the data.
    * **$Q_2$ (Second Quartile / Median):** The value below which $50\%$ of the data lies.
    * **$Q_3$ (Third Quartile / Upper Quartile):** The value below which $75\%$ of the data lies. It is essentially the median of the upper half of the data.

**Formula**

$$
\text{IQR} = Q_3 - Q_1
$$

**Example: Ungrouped Data**

* **Data:** $5, 7, 10, 12, 15, 18, 20, 22, 25$ ($N=9$)
1.  **Order Data:** $5, 7, 10, 12, 15, 18, 20, 22, 25$
2.  **Find $Q_2$ (Median):** The middle value is the $(9+1)/2 = 5$th term, which is **15**.
3.  **Find $Q_1$:** This is the median of the lower half ($5, 7, 10, 12$). The average of the two middle terms is $(7+10)/2 = \mathbf{8.5}$.
4.  **Find $Q_3$:** This is the median of the upper half ($18, 20, 22, 25$). The average of the two middle terms is $(20+22)/2 = \mathbf{21}$.
5.  **Calculate IQR:** $IQR = Q_3 - Q_1 = 21 - 8.5 = \mathbf{12.5}$.

* **Interpretation:** The middle $50\%$ of the data values are spread over a range of $12.5$ units.

---

### Variance ($\sigma^2$ or $s^2$)

Variance is the **most common** and mathematically robust measure of dispersion. It measures the **average of the squared differences** from the mean.

**Definition**

**Variance** is the average of the squared deviations of each observation from the **Arithmetic Mean ($\bar{x}$ or $\mu$)** of the dataset.

* **Why Square the Differences?**
    1.  To ensure that the deviations are **positive**. If we just sum the raw deviations from the mean, the total sum will always be zero.
    2.  To give **greater weight** to larger deviations, meaning observations that are far away from the mean have a much greater impact on the spread.

* **Population vs. Sample:**
    * **Population Variance ($\sigma^2$ - sigma squared):** Calculated when the data represents the *entire* group of interest. The denominator is $N$ (total observations).
    * **Sample Variance ($s^2$):** Calculated when the data is a *subset* used to estimate the characteristics of a larger population. The denominator is **$n-1$** (degrees of freedom) to provide a better, **unbiased estimate** of the population variance.

#### For An Individual Series (Ungrouped Data)

An individual series is a raw list of observations ($x_i$).

**Formula (Population Variance $\sigma^2$):**

$$
\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}
$$

Where:
* $x_i$ = Each individual observation
* $\mu$ = Population Mean ($\frac{\sum x_i}{N}$)
* $N$ = Total number of observations

**Formula (Sample Variance $s^2$):**

$$
s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1}
$$

Where:
* $\bar{x}$ = Sample Mean ($\frac{\sum x_i}{n}$)
* $n$ = Sample size

**Example (Using Population Variance):**

* **Data ($x_i$):** $2, 4, 6, 8, 10$ ($N=5$)
1.  **Calculate Mean ($\mu$):** $\mu = \frac{2+4+6+8+10}{5} = \frac{30}{5} = \mathbf{6}$
2.  **Calculate Squared Deviations $(x_i - \mu)^2$:**
    * $(2-6)^2 = (-4)^2 = 16$
    * $(4-6)^2 = (-2)^2 = 4$
    * $(6-6)^2 = (0)^2 = 0$
    * $(8-6)^2 = (2)^2 = 4$
    * $(10-6)^2 = (4)^2 = 16$
3.  **Sum of Squared Deviations ($\sum (x_i - \mu)^2$):** $16 + 4 + 0 + 4 + 16 = \mathbf{40}$
4.  **Calculate Variance ($\sigma^2$):** $\sigma^2 = \frac{40}{5} = \mathbf{8}$

#### For A Frequency Distribution (Discrete or Continuous)

When data is presented with frequencies ($f$), the deviation of each value is weighted by how often it occurs.

**Formula (Population Variance $\sigma^2$):**

$$
\sigma^2 = \frac{\sum f_i (x_i - \mu)^2}{N}
$$

Where:
* $f_i$ = Frequency of the observation
* $x_i$ = Observation value (or **Midpoint** for continuous data)
* $\mu$ = Population Mean
* $N$ = Total Frequency ($\sum f_i$)

**Formula (Sample Variance $s^2$):**

$$
s^2 = \frac{\sum f_i (x_i - \bar{x})^2}{n - 1}
$$

Where:
* $\bar{x}$ = Sample Mean
* $n$ = Total Sample Frequency ($\sum f_i$)

**Example (Using Population Variance for Discrete Data):**

| $x_i$ | $f_i$ | $f_i x_i$ | $(x_i - \mu)$ | $(x_i - \mu)^2$ | $f_i (x_i - \mu)^2$ |
| :---: | :---: | :-------: | :-----------: | :-------------: | :-----------------: |
| 10    | 2     | 20        | -20           | 400             | 800                 |
| 20    | 3     | 60        | -10           | 100             | 300                 |
| 30    | 5     | 150       | 0             | 0               | 0                   |
| 40    | 4     | 160       | 10            | 100             | 400                 |
| 50    | 1     | 50        | 20            | 400             | 400                 |
| **Total** | **$N=15$** | **$\sum f_i x_i = 440$** | - | - | **$\sum f_i (x_i - \mu)^2 = 1900$** |

1.  **Calculate Mean ($\mu$):** $\mu = \frac{\sum f_i x_i}{N} = \frac{440}{15} \approx \mathbf{29.33}$
2.  **Calculate Variance ($\sigma^2$):** $\sigma^2 = \frac{1900}{15} \approx \mathbf{126.67}$


### Standard Deviation

* **Advanced Note (Standard Deviation):** The **Standard Deviation ($\sigma$ or $s$)** is simply the **square root of the variance**. It is often preferred because it is expressed in the same units as the original data, making it easier to interpret the spread (e.g., if the mean score is 30, a standard deviation of 5 means a typical score is 5 points away from the mean).

---
