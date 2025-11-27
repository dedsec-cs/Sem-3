### Moments

The **$r$-th moment** of a distribution is a measure used to describe the shape of the distribution. It can be measured about an arbitrary point $A$ (raw moment, $\mu'_r$) or about the mean $\bar{X}$ (central moment, $\mu_r$).

-----

**Example:**

  * Find the first four moments for the following individual series: 3, 6, 8, 10, 18.

**Solution:**
Data ($N=5$): 3, 6, 8, 10, 18.
$$\text{Mean } (\bar{X}) = \frac{3 + 6 + 8 + 10 + 18}{5} = \frac{45}{5} = \mathbf{9.0}$$

|               Moment                |             Value              |
| :---------------------------------: | :----------------------------: |
|  **Moments about Mean ($\mu_r$)**   |     $\mu_1 = \mathbf{0.0}$     |
|         $\mu_2$ (Variance)          |        $\mathbf{25.6}$         |
|               $\mu_3$               |        $\mathbf{97.2}$         |
|               $\mu_4$               |       $\mathbf{1588.0}$        |
| **Moments about Origin ($\mu'_r$)** | $\mu'_1$ (Mean) $\mathbf{9.0}$ |
|              $\mu'_2$               |        $\mathbf{106.6}$        |
|              $\mu'_3$               |       $\mathbf{1517.4}$        |
|              $\mu'_4$               |       $\mathbf{24089.8}$       |

-----

**Example:**

  * Find the first four moments for the following frequency distribution:

| Marks | 5-15 | 15-25 | 25-35 | 35-45 | 45-55 | 55-65 |
|---|---|---|---|---|---|---|
| No. of students ($F$) | 10 | 20 | 25 | 20 | 15 | 10 |

**Solution:**
Midpoints ($m$): 10, 20, 30, 40, 50, 60. $N=100$. $\sum Fm = 3400$.
$$\text{Mean } (\bar{X}) = \frac{3400}{100} = \mathbf{34.0}$$

We calculate the first four central moments ($\mu_r$).

| Moment | Formula | Value |
|:---:|:---:|:---:|
| $\mu_1$ | $\frac{\sum F(m - \bar{X})}{N}$ | $\mathbf{0.0}$ |
| $\mu_2$ (Variance) | $\frac{\sum F(m - \bar{X})^2}{N}$ | $\mathbf{214.0}$ |
| $\mu_3$ | $\frac{\sum F(m - \bar{X})^3}{N}$ | $\mathbf{468.0}$ |
| $\mu_4$ | $\frac{\sum F(m - \bar{X})^4}{N}$ | $\mathbf{96712.0}$ |

-----

**Example:**

  * The first three moments of a distribution about the value "2" of the variable are 1, 16 and -40. Show that the mean is 3, variance is 15 and the third central moment is -86.

**Solution:**
Given: Arbitrary point $A=2$. Raw moments: $\mu'_1=1, \mu'_2=16, \mu'_3=-40$.

**1. Mean ($\bar{X}$):**
$$\bar{X} = A + \mu'_1 = 2 + 1 = \mathbf{3}$$
*(Mean is 3. **Shown**)*

**2. Variance ($\mu_2$):**
$$\mu_2 = \mu'_2 - (\mu'_1)^2 = 16 - (1)^2 = 16 - 1 = \mathbf{15}$$
*(Variance is 15. **Shown**)*

**3. Third Central Moment ($\mu_3$):**
$$\mu_3 = \mu'_3 - 3\mu'_2 \mu'_1 + 2(\mu'_1)^3$$
$$\mu_3 = -40 - 3(16)(1) + 2(1)^3$$
$$\mu_3 = -40 - 48 + 2 = \mathbf{-86}$$
*(Third central moment is -86. **Shown**)*

-----

**Example:**

  * The first moments of a distribution about the value "35" are -1.8, 240, -1020 and 144000. Find the values of $\mu_{1}, \mu_{2}, \mu_{3}, \mu_{4}$.

**Solution:**
Given: $\mu'_1=-1.8, \mu'_2=240, \mu'_3=-1020, \mu'_4=144000$.

  * $\mathbf{\mu_1}$ (First Central Moment): By definition, the first moment about the mean is always zero.
    $$\mu_1 = \mathbf{0}$$
  * $\mathbf{\mu_2}$ (Variance):
    $$\mu_2 = \mu'_2 - (\mu'_1)^2 = 240 - (-1.8)^2 = 240 - 3.24 = \mathbf{236.76}$$
  * $\mathbf{\mu_3}$ (Third Central Moment):
    $$\mu_3 = \mu'_3 - 3\mu'_2 \mu'_1 + 2(\mu'_1)^3$$
    $$\mu_3 = -1020 - 3(240)(-1.8) + 2(-1.8)^3$$
    $$\mu_3 = -1020 + 1296 - 11.664 = \mathbf{264.336}$$
  * $\mathbf{\mu_4}$ (Fourth Central Moment):
    $$\mu_4 = \mu'_4 - 4\mu'_3 \mu'_1 + 6\mu'_2 (\mu'_1)^2 - 3(\mu'_1)^4$$
    $$\mu_4 = 144000 - 4(-1020)(-1.8) + 6(240)(-1.8)^2 - 3(-1.8)^4$$
    $$\mu_4 = 144000 - 7344 + 4665.6 - 34.992 = \mathbf{141290.1072}$$

-----

**Example:**

  * Calculate the variance and third central moment from the following data:

| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| f | 1 | 9 | 26 | 59 | 72 | 52 | 29 | 7 | 1 |

**Solution:**
$N = \sum F = 256$. $\sum FX = 1017$.
$$\text{Mean } (\bar{X}) = \frac{1017}{256} \approx \mathbf{3.9727}$$

**1. Variance ($\mu_2$):**
$$\text{Variance } (\mu_2) = \frac{\sum F(X - \bar{X})^2}{N} \approx \mathbf{1.9797}$$

**2. Third Central Moment ($\mu_3$):**
$$\mu_3 = \frac{\sum F(X - \bar{X})^3}{N} \approx \mathbf{0.0179}$$

-----

**Example:**

  * The first four moments of a distribution about the value '4'of the variable are -1.5, 17, -30 and 108. Find the moments about mean, about origin.

**Solution:**
Given: $A=4$. $\mu'_1=-1.5, \mu'_2=17, \mu'_3=-30, \mu'_4=108$.

**1. Moments about Mean ($\mu_r$):**

  * $\mu_1 = \mathbf{0}$
  * $\mu_2 = 17 - (-1.5)^2 = 17 - 2.25 = \mathbf{14.75}$
  * $\mu_3 = -30 - 3(17)(-1.5) + 2(-1.5)^3 = -30 + 76.5 - 6.75 = \mathbf{39.75}$
  * $\mu_4 = 108 - 4(-30)(-1.5) + 6(17)(-1.5)^2 - 3(-1.5)^4$
    $$\mu_4 = 108 - 180 + 229.5 - 15.1875 = \mathbf{142.3125}$$

**2. Moments about Origin ($\mu''_r$, where $A=0$):**

  * $\mu''_1$ (Mean) $= A + \mu'_1 = 4 + (-1.5) = \mathbf{2.5}$
  * $\mu''_2 = \mu'_2 + 2\mu'_1 A + A^2 = 17 + 2(-1.5)(4) + 4^2 = 17 - 12 + 16 = \mathbf{21.0}$
  * $\mu''_3 = \mu'_3 + 3\mu'_2 A + 3\mu'_1 A^2 + A^3 = -30 + 3(17)(4) + 3(-1.5)(4^2) + 4^3$
    $$\mu''_3 = -30 + 204 - 72 + 64 = \mathbf{166.0}$$
  * $\mu''_4 = \mu'_4 + 4\mu'_3 A + 6\mu'_2 A^2 + 4\mu'_1 A^3 + A^4$
    $$\mu''_4 = 108 + 4(-30)(4) + 6(17)(4^2) + 4(-1.5)(4^3) + 4^4$$
    $$\mu''_4 = 108 - 480 + 1632 - 384 + 256 = \mathbf{1132.0}$$

-----

**Example:**

  * Compute first four moments of the data 3, 5, 7, 9 about mean. Also, compute the first four moments about the point 4.

**Solution:**
Data ($N=4$): 3, 5, 7, 9. $\sum X=24$.
$$\text{Mean } (\bar{X}) = \frac{24}{4} = \mathbf{6.0}$$

**1. Moments about Mean ($\mu_r$):**

| $X$ | $X - \bar{X}$ | $(X - \bar{X})^2$ | $(X - \bar{X})^3$ | $(X - \bar{X})^4$ |
|:---:|:---:|:---:|:---:|:---:|
| 3 | -3 | 9 | -27 | 81 |
| 5 | -1 | 1 | -1 | 1 |
| 7 | 1 | 1 | 1 | 1 |
| 9 | 3 | 9 | 27 | 81 |
| **Sum** | 0 | 20 | 0 | 164 |

  * $\mu_1 = \mathbf{0.0}$
  * $\mu_2 = 20 / 4 = \mathbf{5.0}$
  * $\mu_3 = 0 / 4 = \mathbf{0.0}$
  * $\mu_4 = 164 / 4 = \mathbf{41.0}$

**2. Moments about $A=4$ ($\mu'_r$):**

| $X$ | $X - 4$ | $(X - 4)^2$ | $(X - 4)^3$ | $(X - 4)^4$ |
|:---:|:---:|:---:|:---:|:---:|
| 3 | -1 | 1 | -1 | 1 |
| 5 | 1 | 1 | 1 | 1 |
| 7 | 3 | 9 | 27 | 81 |
| 9 | 5 | 25 | 125 | 625 |
| **Sum** | 8 | 36 | 152 | 708 |

  * $\mu'_1 = 8 / 4 = \mathbf{2.0}$
  * $\mu'_2 = 36 / 4 = \mathbf{9.0}$
  * $\mu'_3 = 152 / 4 = \mathbf{38.0}$
  * $\mu'_4 = 708 / 4 = \mathbf{177.0}$

-----

**Example:**

  * The first four moments about mean of a distribution are 1, 3, 7, 9, 10.

**Solution:**
The moments about the mean ($\mu_r$) are:

  * $\mu_1$ (First Central Moment) is always $\mathbf{0}$.
  * $\mu_2 = \mathbf{1}$ (Variance)
  * $\mu_3 = \mathbf{3}$
  * $\mu_4 = \mathbf{7}$

*(The remaining values, 9 and 10, are extraneous, as only four central moments exist up to $\mu_4$)*

-----

**Example:**

  * The first four moments of a distribution about 2 are 1, 2.5, 5.5 and 16 respectively. Calculate the four moments about mean and about the origin.

**Solution:**
Given: $A=2$. $\mu'_1=1, \mu'_2=2.5, \mu'_3=5.5, \mu'_4=16$.

**1. Moments about Mean ($\mu_r$):**

  * $\mu_1 = \mathbf{0}$
  * $\mu_2 = \mu'_2 - (\mu'_1)^2 = 2.5 - (1)^2 = \mathbf{1.5}$
  * $\mu_3 = \mu'_3 - 3\mu'_2 \mu'_1 + 2(\mu'_1)^3 = 5.5 - 3(2.5)(1) + 2(1)^3 = 5.5 - 7.5 + 2 = \mathbf{0.0}$
  * $\mu_4 = \mu'_4 - 4\mu'_3 \mu'_1 + 6\mu'_2 (\mu'_1)^2 - 3(\mu'_1)^4$
    $$\mu_4 = 16 - 4(5.5)(1) + 6(2.5)(1)^2 - 3(1)^4$$
    $$\mu_4 = 16 - 22 + 15 - 3 = \mathbf{6.0}$$

**2. Moments about Origin ($\mu''_r$):**

  * $\mu''_1$ (Mean) $= A + \mu'_1 = 2 + 1 = \mathbf{3}$
  * $\mu''_2 = \mu'_2 + 2\mu'_1 A + A^2 = 2.5 + 2(1)(2) + 2^2 = 2.5 + 4 + 4 = \mathbf{10.5}$
  * $\mu''_3 = \mu'_3 + 3\mu'_2 A + 3\mu'_1 A^2 + A^3 = 5.5 + 3(2.5)(2) + 3(1)(2^2) + 2^3$
    $$\mu''_3 = 5.5 + 15 + 12 + 8 = \mathbf{40.5}$$
  * $\mu''_4 = \mu'_4 + 4\mu'_3 A + 6\mu'_2 A^2 + 4\mu'_1 A^3 + A^4 = 16 + 4(5.5)(2) + 6(2.5)(2^2) + 4(1)(2^3) + 2^4$$
    $$\mu''_4 = 16 + 44 + 60 + 32 + 16 = \mathbf{168.0}$$

-----

**Example:**

  * The First four moments of a distribution about are Find the first four moments about mean. Discuss the Skewness and Kurtosis and also comment upon the nature of the distribution.

**Solution (Using results from P6/P11 for Skewness and Kurtosis demonstration):**
We use the central moments ($\mu_r$) derived from the distribution where $\mu_2=14.75$, $\mu_3=39.75$, and $\mu_4=142.3125$.

**1. Skewness ($\beta_1, \gamma_1$):**
Skewness measures the degree of asymmetry of a distribution.
$$\beta_1 = \frac{\mu_3^2}{\mu_2^3} = \frac{39.75^2}{14.75^3} \approx \mathbf{0.492}$$
$$\gamma_1 = \sqrt{\beta_1} \approx \mathbf{0.702}$$
Since $\gamma_1 > 0$, the distribution has **Positive Skewness** (or is skewed to the right).

**2. Kurtosis ($\beta_2, \gamma_2$):**
Kurtosis measures the "peakedness" or "tailedness" of a distribution relative to a normal distribution ($\beta_2=3$).
$$\beta_2 = \frac{\mu_4}{\mu_2^2} = \frac{142.3125}{14.75^2} \approx \mathbf{0.654}$$
$$\gamma_2 = \beta_2 - 3 = 0.654 - 3 = \mathbf{-2.346}$$

**3. Comment on Nature of Distribution:**

  * **Skewness:** The distribution is **Positively Skewed** ($\gamma_1 > 0$). The longer tail is towards the positive (right) side.
  * **Kurtosis:** Since $\beta_2 < 3$ (or $\gamma_2 < 0$), the distribution is **Platykurtic**. It is flatter than the normal distribution, meaning it has lighter tails and a less pronounced peak.